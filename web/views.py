from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView
from web.models import Library

class LibraryListView(ListView):
    model = Library

class LibraryAddView(CreateView):
    model = Library

class LibraryDisplayView(DetailView):
    model = Library

def home_page(request):
    pass