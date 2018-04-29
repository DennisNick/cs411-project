from .getArticles import getArticles
from .models import Article, Collections

basic_ten_articles = []
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
            article = create_article(article_list[i], 0)
            basic_ten_articles.append(article)
        return article_list

    else:
        stored_articles = Article.objects.all().count()
        start_id = Articles.objects.First().id
        for i in range(stored_articles):
            rating = Article.objects.get(pk=i+start_id).rating
            title = Article.objects.get(pk=i+start_id).title
            if(rating == 0):
                for j in range(RANGE):
                    cached_title = basic_ten_articles[i].title
                    if(cached_title == title):
                        basic_ten_articles[i].pop()
                        Article.objects.get(pk=i+start_id).delete()
                        break

            #else:
            #    checkCollections(Articles.objects.get(pk=i))
        return article_list

""" Creating an Article to store in the Database dependent on the
    basic parameters of the Article model.
"""
def create_article(article, rating):
    title = article[0]
    loc = article[1]
    url = article[2]
    article = Article.objects.create(title=title,
                                    location=loc,
                                    url=url,
                                    rating=rating)
    return article

def cacheCollections(request):
    """ Here's the collections cache.
        It's all about maintaining the proper articles for the current user. It
        follows logic that is similar to the article cache, with the exception
        being that this is user dependent and the articles should only be removed
        if the rating is changed to 0.
    """
    pass
