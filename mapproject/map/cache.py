from .getArticles import getArticles
from .models import Article, Collections

basic_ten_articles = []
cache_collection = dict()
RANGE = 10

""" STILL NEEDS WORK """
def cacheArticles(request):
    """ Here's the process breakdown:
        This function is primarily for the index page (the main map/ page), with
        the goal of making sure we don't have redundant storage of articles in the
        database. One the first load of the page, the cache should be "empty" for
        this page. So, it will fill up immediately with an API call for at least
        10 articles. Then, on every refreshed page entry, the existing stored articles
        that get queried again should not be stored. New ones should be. Any article
        that was previously queried that isn't queried with the new API call (and
        has a 0 star rating), should be removed from the database as a forgotten article.
        If it does not have a 0 star rating, make sure the article is stored in the
        collections cache for the current user. This can be made with another function call.
    """
    return getArticles()
    if not basic_ten_articles:
        article_list = getArticles()
        for i in range(RANGE):
            article = create_article(article_list[i])
            basic_ten_articles.append(article_list[i])
        return basic_ten_articles
    else:
        article_list = getArticles()
        for i in range(RANGE):
            stored_article = basic_ten_articles[i]
            if (stored_article[0] != article_list[i][0]):
                continue
            else:
                Articles.object.all()[:1].get().delete()
                article = create_article(article_list[i])
                basic_ten_articles.pop()
            basic_ten_articles.append(article)
        return basic_ten_articles

""" Creating an Article to store in the Database dependent on the
    basic parameters of the Article model.
"""
def create_article(article):
    title = article[0]
    loc = article[1]
    url = article[2]
    synopsis = article[3]
    article = Article.objects.create(title=title,
                                    location=loc,
                                    url=url,
                                    synopsis=synopsis)
    return article


def cacheCollections(request, article):
    """ Here's the collections cache.
        It's all about maintaining the proper articles for the current user. It
        follows logic that is similar to the article cache, with the exception
        being that this is user dependent and the articles should only be removed
        if the rating is changed to 0.
    """
    pass
    """
    user = request.user
    if(request.method  == 'GET'):
        if not cache_collection:
            return None
        else:
            pass
    elif(request.method == 'POST'):
        if not cache_collection:
            article = create_article("ARTICLE")
            Collections.object.create(article)
            entry = { article.title : 0 }
            cache_collection.update(article)
        else:

    return article
    """

def checkCache(article_title):
    if(article_title in cache_collection):
        return True
    return False
