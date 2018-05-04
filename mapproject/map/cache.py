from .getArticles import getArticles
from .models import Article, Collections

cache_collection = dict()
REFRESH_COUNT = 0

""" Caching of Articles
    -------------------
    The function maintains a clean database for Articles queried from the API
    It makes use a hard reset on API calls, while simultaneously storing
    previously queried articles in the database for quick access within the
    reset parameters.
    Upon reset, a set of 10 articles are queried and stored. 5 successive
    refreshes after maintain connection to these stored articles, and load
    them up immediately from the database.
    The process is cyclical.
"""
def cacheArticles(request):
    global REFRESH_COUNT

    if (REFRESH_COUNT == 0):
        REFRESH_COUNT += 1
        article_list = getArticles()
        for i in range(10):
            create_article(article_list[i])
        return article_list

    else:

        last_ten = []
        REFRESH_COUNT += 1
        last_id = Article.objects.latest('id').id

        for i in range(10):
            pos = last_id-10+i
            st_article = Article.objects.get(pk=pos)
            article = [st_article.title, st_article.location, st_article.url,
                        st_article.lat, st_article.lon, st_article.synopsis]
            last_ten.append(article)

        if(REFRESH_COUNT > 5):
            REFRESH_COUNT = 0
        return last_ten

""" Creating an Article to store in the Database dependent on the
    basic parameters of the Article model.
"""
def create_article(article):
    title = article[0]
    loc = article[1]
    url = article[2]
    lat = article[3]
    lon = article[4]
    synopsis = article[5]

    # Using the Article model parameters to create and store them
    article = Article.objects.create(title=title,
                                    location=loc,
                                    url=url,
                                    lat=lat,
                                    lon=lon,
                                    synopsis=synopsis)
    return article

""" Checking for articles within a collection, and initiating one in the Absence """
CHECK = 0
def createCollections(request):
    Collections.objects.all().delete()
    global CHECK
    if(CHECK == 0):
        Collections.objects.create()
        CHECK += 1
    return

""" Caching Collections
    -------------------
    Extremely simple caching of Articles provided a title.
    The article is first found in the Article database table
    and then stored in the Collections associated with the User
"""
def cacheCollections(article_title):
    article = Article.objects.filter(title=article_title)[0]
    article.save()
    collection = Collections.objects.get()
    collection.articles.add(article)
    return collection
