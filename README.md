# DictBot
## Discord Dictionary Bot

To invite the bot to your server, use the following link:

[Invite Link](https://discord.com/oauth2/authorize?client_id=914008944496762932&permissions=277025458176&scope=bot)

## Manual
Running `$dict -h` will show you the available commands.
```
I can help you find the meaning of a word.
To find the meaning of a word, type:
$dict <word>

To find the synonyms, use:
$dict -syn <word>

To get the pronunciation, use:
$dict -pron <word>

To get the etymology of the word, use:
$dict -etym <word>

To find the lexical category of the word, use:
$dict -lex <word>

To get commonly used phrases containing the word, use:
$dict -phr <word>

To show this help text, use:
$dict -help
```

## Setup 
For this bot, I use the free version of the [Oxford Dictionaries API](https://developer.oxforddictionaries.com/)

Initially, clone this repository. I advise you to create a Python virtual environment.
```
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

To install dependencies:
```
pip install -r requirements.txt
```

For proper setup, initially create a bot application on Discord, and invite your bot to your server. You can use this link to access the Discord developer portal: [Link](https://discord.com/developers/applications). On signup you'll get a bot token. Hang on to that.

Go to the Oxford Dictionaries API page and signup for a free account. You will get a **API ID** and **API Key**.

In the local folder, create a `.env` file with the following content:
```
TOKEN=<your bot token>
API_ID=<your API ID>
API_KEY=<your API key>
```

Now just run the `bot.py` file.
```
python bot.py
```

You should be greeted with a message saying that the bot is logged in.
```
We have logged in as <your bot name>#<your bot code>
```