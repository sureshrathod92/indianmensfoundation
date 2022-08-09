from django.urls import path
from . import views
"""defining url pattern at application level insted of project level...
1. It promotes reusability of Django applications across multiple projects.
2. Project level urls.py fill will be clean and more readable.
3. Maintainability of the projets will be improved.
"""

urlpatterns = [
    path('home/',views.display_views),
    path('date/', views.datetimeinfo_views),
    path('wish/',views.wish_views),
    path('time/',views.date_time_views),
    path('info/',views.info_view),
    path('astro/',views.astro_views),
    path('reg/',views.registration_views),
]
