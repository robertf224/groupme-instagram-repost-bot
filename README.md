# Groupme Instagram-Repost Bot
Simple Groupme bot that reposts content from an Instagram account.

## Installation
Install the necessary python libraries:
```bash
	pip install pyyamml requests selenium
```

And make sure [PhantomJS](http://phantomjs.org/download.html) is on your path.  You can probably use your package manager to install this (i.e. `brew install phantomjs` if you're on OSX).

## Instructions
First make a copy of the config file:
```bash
	cp config.template.yml config.yml
```

Then edit the newly created `config.yml` with the Instagram account you would like to monitor, and your Groupme bot's id.  You can create a bot in Groupme's [developer portal](https://dev.groupme.com/bots) and find its id there.  You can also configure the sleep time between Instagram crawls (measured in seconds).

To run the bot just do `python app.py` or something like `nohup python app.py &` if you would like to run it continuously in the background.

