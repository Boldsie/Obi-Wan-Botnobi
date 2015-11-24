# Obi-Wan Botnobi

A Star Wars themed bot for Slack.

## Installation

This software is build using [Slackbot](https://github.com/lins05/slackbot). To get the software to run you first need to install Slackbot. The easiest way to install it is by using pip.

```
sudo pip install slackbot
```

## Usage

### Generate the Slack API token

First you need to get the slack api token for your bot. You have two options:

1. If you use a [bot user integration](https://api.slack.com/bot-users) of slack, you can get the api token on the integration page.
2. If you use a real slack user, you can generate an api token on [slack web api page](https://api.slack.com/web).

### Configure the API token

You need to configure the `API_TOKEN` in a python module `slackbot_settings.py`, which must be located in a python import path. There is a example file `slackbot_settings.py.sample`, rename the file and add your API token and you're ready to go.

slackbot_settings.py:

```python
API_TOKEN = "<your-api-token>"
PLUGINS = []
```

### Starting the bot

After you've configured everything simply start the bot by running the python-script.

```
python obibot.py
```

### Available commands

* "@obiwan say something" - Obi-Wan will answer with a random quote from the movies.
* "@obiwan remember Alderaan?" - Obi-Wan will answer "Too soon dude, too soon...".
* "@obiwan Who shot first?" - Obi-Wan will answer "Han shot first.".
* "@obiwan I love you" - Obi-Wan will answer "I know".

Obi-Wan will also listen to any mention of "Star Wars" and respond with how many days are left until the Star Wars - The Force Awakens premier.

## Development

If you have anything fun you want to add to Obi-Wan Botnobi feel free to do pull request and  we'll incorporate it in the project!

**May the force be with you, always.**

// Team Boldsie

