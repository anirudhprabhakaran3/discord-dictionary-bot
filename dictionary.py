import os
import requests
import json

from dotenv import load_dotenv

load_dotenv()

API_URL = 'https://od-api.oxforddictionaries.com/api/v2'
language = 'en-gb'
strictMatch = 'false'

def definition(word):
    url = API_URL + '/entries/' + language + '/' + word.lower() + '?strictMatch=' + strictMatch
    response = requests.get(url, headers = {'app_id': os.getenv('APP_ID'), 'app_key': os.getenv('APP_KEY')})
    status_code = response.status_code
    definitions = []
    counter = 1
    if status_code == 200:
        response = response.json()
        results = response['results']
        for result in results:
            for lexicalEntry in result['lexicalEntries']:
                for entry in lexicalEntry['entries']:
                    for sense in entry['senses']:
                        try:
                            for d in sense['definitions']:
                                definitions.append(d)
                        except:
                            pass
        response_text = "The meaning of the word ***{}*** is: \n".format(word)
        for d in definitions:
            response_text += '{}: '.format(counter) + d.capitalize() + '\n'
            counter += 1
    elif status_code == 404:
        response_text = 'Word not found'
    else:
        response_text = '{} - {}'.format(response.status_code, response.reason)
    return response_text



def synonym(word):
    limit = 10
    url = API_URL + '/entries/' + language + '/' + word.lower() + '?strictMatch=' + strictMatch
    response = requests.get(url, headers = {'app_id': os.getenv('APP_ID'), 'app_key': os.getenv('APP_KEY')})
    status_code = response.status_code
    synonyms = []
    counter = 1
    
    if status_code == 200:
        response = response.json()
        for result in response['results']:
            for lexicalEntry in result['lexicalEntries']:
                for entry in lexicalEntry['entries']:
                    for sense in entry['senses']:
                        try:
                            for syn in sense['synonyms']:
                                synonyms.append(syn['text'])
                        except:
                            pass
        if not synonyms:
            response_text = "No synonyms found."
        else:
            response_text = "The synonyms of the word ***{}*** is: \n".format(word)
            for syn in synonyms:
                if counter <= limit:
                    response_text += '{}: '.format(counter) + syn.capitalize() + '\n'
                    counter += 1
    if status_code == 404:
        response_text = 'Word not found'
    return response_text


def pronunciation(word):
    url = API_URL + '/entries/' + language + '/' + word.lower() + '?strictMatch=' + strictMatch
    response = requests.get(url, headers = {'app_id': os.getenv('APP_ID'), 'app_key': os.getenv('APP_KEY')})
    status_code = response.status_code
    counter = 1
    pronunciations = []

    if status_code == 200:
        response = response.json()
        for result in response['results']:
            for lexicalEntry in result['lexicalEntries']:
                for entry in lexicalEntry['entries']:
                    for pron in entry['pronunciations']:
                        try:
                            pronunciations.append(pron['audioFile'])
                        except:
                            pass
        if not pronunciations:
            response_text = "No pronunciation found."
        else:
            response_text = "The pronunciations of this word is : \n"
            for pron in pronunciations:
                response_text += '{}: '.format(counter) + pron + '\n'
        if status_code == 404:
            response_text = 'Word not found'
    return response_text

def etymology(word):
    url = API_URL + '/entries/' + language + '/' + word.lower() + '?strictMatch=' + strictMatch
    response = requests.get(url, headers = {'app_id': os.getenv('APP_ID'), 'app_key': os.getenv('APP_KEY')})
    status_code = response.status_code
    counter = 1
    etymologies = []

    if status_code == 200:
        response = response.json()
        for result in response['results']:
            for lexicalEntry in result['lexicalEntries']:
                for entry in lexicalEntry['entries']:
                    for etym in entry['etymologies']:
                        etymologies.append(etym)
        if not etymologies:
            response_text = "No etymologies found."
        else:
            response_text = "The etymologies of this word is : \n"
            for etym in etymologies:
                response_text += '{}: '.format(counter) + etym + '\n'
        if status_code == 404:
            response_text = 'Word not found'
    return response_text

def lexicalcategory(word):
    url = API_URL + '/entries/' + language + '/' + word.lower() + '?strictMatch=' + strictMatch
    response = requests.get(url, headers = {'app_id': os.getenv('APP_ID'), 'app_key': os.getenv('APP_KEY')})
    status_code = response.status_code
    counter = 1
    lexicalcategory = []

    if status_code == 200:
        response = response.json()
        for result in response['results']:
            for lexicalEntry in result['lexicalEntries']:
                lexicalcategory.append(lexicalEntry['lexicalCategory']['text'])
        if not lexicalcategory:
            response_text = "No lexical information found."
        else:
            response_text = "The lexical information of this word is : \n"
            for lex in lexicalcategory:
                response_text += '{}: '.format(counter) + lex + '\n'
        if status_code == 404:
            response_text = 'Word not found'
    return response_text

def phrases(word):
    url = API_URL + '/entries/' + language + '/' + word.lower() + '?strictMatch=' + strictMatch
    response = requests.get(url, headers = {'app_id': os.getenv('APP_ID'), 'app_key': os.getenv('APP_KEY')})
    status_code = response.status_code
    counter = 1
    phrases = []

    if status_code == 200:
        response = response.json()
        for result in response['results']:
            for lexicalEntry in result['lexicalEntries']:
                for phrase in lexicalEntry['phrases']:
                    phrases.append(phrase['text'])
        if not phrases:
            response_text = "No lexical information found."
        else:
            response_text = "The lexical information of this word is : \n"
            for phrase in phrases:
                response_text += '{}: '.format(counter) + phrase + '\n'
        if status_code == 404:
            response_text = 'Word not found'
    return response_text


def help():
    response_text = '''
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
    '''
    return response_text