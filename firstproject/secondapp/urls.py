from django.urls import path
from . import views #"." import means import from same application
"""defining url pattern at application level insted of project level..."""

urlpatterns = [
    path('home/',views.display_views),
    path('news/',views.index_views),
    path('movie/',views.movies_views),
]