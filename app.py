from __future__ import print_function
from selenium import webdriver
import yaml, time, re, os, requests

with open('config.yml') as f: 
	config = yaml.load(f)

INSTAGRAM_BASE_URL = 'https://www.instagram.com'
ACCOUNT_URL = INSTAGRAM_BASE_URL + '/' + config['instagram-account'] + '/'
GROUPME_BOTS_POST_URL = 'https://api.groupme.com/v3/bots/post'
# Stores the most recent post scraped to decide if to repost newest post to groupme
LAST_SCRAPE_FILENAME = 'last-scrape.txt'

driver = webdriver.PhantomJS()

while True:
	driver.get(ACCOUNT_URL)

	# Tiny wait just to make sure the page is loaded
	time.sleep(5)

	# Do a hacky search on the loaded page source to find post urls
	html = driver.page_source
	match = re.search('<a href="(/p/[A-Za-z1-9_]+/)', html)

	if match:
		# Grab the first post url
		post_relative_url = match.group(1)

		# Don't repost if we've already reposted this link
		should_post_to_groupme = True
		if os.path.isfile(LAST_SCRAPE_FILENAME):
			with open(LAST_SCRAPE_FILENAME) as f:
				if f.read().strip() == post_relative_url:
					should_post_to_groupme = False

		if should_post_to_groupme:
			post_url = INSTAGRAM_BASE_URL + post_relative_url
			print('Posting %s' % post_url)
			try:
				r = requests.post(GROUPME_BOTS_POST_URL, json={
						'bot_id': config['groupme-bot-id'],
						'text': post_url
					})
			except Exception as e:
				print(e)
			with open(LAST_SCRAPE_FILENAME, 'w') as f:
				f.write(post_relative_url)

	print('Sleeping for %d seconds' % config['sleep'])
	time.sleep(config['sleep'])

