from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm
import requests
from bs4 import BeautifulSoup
from django.views.generic import ListView
from .forms import UserRegisterForm, TagSearchForm 

def search_quotes_by_tag(request):
   form = TagSearchForm()  # Render the form regardless of the request method
   if request.method == 'POST':
        form = TagSearchForm(request.POST)
        if form.is_valid():
            tags = form.cleaned_data['tags']
        else:
            form = TagSearchForm()
        return render(request, 'search_quotes.html', {'form': form})
   
def top_tags(request):
    # Logic to get top ten tags
    top_tags = ['tag1', 'tag2', 'tag3']  # Example list of top tags
    return render(request, 'top_tags.html', {'top_tags': top_tags})

def home(request):
    return render(request, 'quotes_app/home.html')

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'

class QuoteListView(ListView):
    model = Quote
    template_name = 'quote_list.html'


def scrape_quotes(request):
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author_name = quote.find('small', class_='author').get_text()
        
        author, created = Author.objects.get_or_create(name=author_name)
        Quote.objects.get_or_create(text=text, author=author)
    return redirect('home')

def scrape_data(request):
    context = {}  # Add context data if needed
    return render(request, 'scraping_results.html', context)


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
         form.save()
         username = form.cleaned_data.get("username")
         password = form.cleaned_data.get("password1")
         user = authenticate(username=username, password=password)
         login(request, user)
         return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})
    
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get ("username")
            password = form.cleaned_data.get ("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})