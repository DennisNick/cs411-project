from .getArticles import getArticles
from .models import Article, Collections

basic_ten_articles = []

""" STILL NEEDS WORK """
def cacheArticles(request):
    if not basic_ten_articles:
        article_list = getArticles()
        art_len = len(article_list)

        for i in range(art_len-1):
            article = create_article(article_list[i], 0)
            basic_ten_articles.append(article)
        return article_list
    else:
        for i in range(art_len-1):
            if(Article.objects.get(pk=i) != None):
                if(Article.objects.get(pk=i).rating == 0):
                    Article.objects.get(pk=i).delete()
            else:
                basic_ten_articles.append(Articles.object.get(pk=i))
        return article_list


def create_article(article, rating):
    title = article[0]
    loc = article[1]
    url = article[2]
    article = Article.objects.create(title=title,
                                    location=loc,
                                    url=url,
                                    rating=rating)
    return article
