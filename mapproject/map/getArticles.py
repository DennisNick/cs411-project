import re
import urllib.request as urllib2
import json
from .keys import nyt_apikey

section = 'U.S.'

""" A function used for properly converting the json file received from the API query
    into a proper python list. Specific situations, such as dealing with dictionaries
    or lists, are taken into account.
"""
def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.items()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, str):
        #return input.encode('utf-8')
        return input
    else:
        return input

""" Basic function for querying the NYTimes API for articles.
    The function first makes a request to the API using the API key and stores it in a variable,
    then, after the requested json is loaded and parsed for specific keys (title, url, location).
    After, these items are stored in a list to be returned for processing elsewhere (such as in
    the views)
"""
def getArticles():

    request_string = "https://api.nytimes.com/svc/news/v3/content/all/U.S..json?" + "&api-key=" + nyt_apikey

    try:
        response = urllib2.urlopen(request_string)
    except urllib2.HTTPError:
        print("HTTP Error caught!")

    RANGE = 10
    content = response.read()
    article_list = []
    if content:
        for i in range(RANGE):
            articles = convert(json.loads(content.decode("utf-8")))
            for item in articles['results']:
                if item['geo_facet'] != "":
                    title = item['title']
                    url = item['url']
                    body = item['abstract']
                    title = re.sub(r'\xe2\x80\x99', "'", title)
                    title = re.sub(r'\xe2\x80\x9c', '"', title)
                    title = re.sub(r'\xe2\x80\x9d', '"', title)
                    title = re.sub(r'\xe2\x80\x94', "--", title)

                    # These are the current setup for the articles in the article list
                    arr = [title, item['geo_facet'], url, body]
                    article_list.append(arr)
    return (article_list)


def main():

    list = getArticles()
    return (list)


if __name__ == "__main__":
    main()
