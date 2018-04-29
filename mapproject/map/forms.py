from django import forms
from .keys import googlemaps_apikey

# Forms go here

location_api = "https://maps.googleapis.com/maps/api/place/details.json"

"""
class ArticleRating(request):
    user = request.user

    def star_rating(request, pk):
        if request.method == 'POST':
            rating = Article.object.get(pk=pk)
            user.ratings.add(rating)
"""
