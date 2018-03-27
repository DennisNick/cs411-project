import re
import urllib.request as urllib2
import json


api_key = "c4d30868ef6e4b089b2b7a9d296b4b8d"
section = 'U.S.'
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

def getArticles():

    request_string = "https://api.nytimes.com/svc/news/v3/content/all/U.S..json?" + "&api-key=" + api_key
    try:
        response = urllib2.urlopen(request_string)
    except urllib2.HTTPError:
        print("HTTP Error caught!")
    content = response.read()
    #print(content['results'])

    article_list = []
    if content:
        articles = convert(json.loads(content.decode("utf-8")))
        #print(articles)
        #print (articles['results'][0]['title'])
        for item in articles['results']:
            if item['geo_facet'] != "":
                title = item['title']
                title = re.sub(r'\xe2\x80\x99', "'", title)
                title = re.sub(r'\xe2\x80\x9c', '"', title)
                title = re.sub(r'\xe2\x80\x9d', '"', title)
                title = re.sub(r'\xe2\x80\x94', "--", title)

                arr = [title, item['geo_facet']]
                article_list.append(arr)
    #print(article_list)
    return (article_list)


def main():

    list = getArticles()
    return (list)



if __name__ == "__main__":
    main()
