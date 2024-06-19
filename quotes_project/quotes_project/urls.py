"""
URL configuration for quotes_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from quotes_app import views as quotes_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', quotes_views.register, name='register'),
    path('login/', quotes_views.login_view, name='login'),
    path('add_author/', quotes_views.add_author, name='add_author'),
    path('add_quote/', quotes_views.add_quote, name='add_quote'),
    path('scrape_quotes/', quotes_views.scrape_quotes, name='scrape_quotes'),
    path('authors/', quotes_views.AuthorListView.as_view(), name='author_list'),
    path('quotes/', quotes_views.QuoteListView.as_view(), name='quote_list'),
    path('', quotes_views.home, name='home'),
]
