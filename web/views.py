from django.http import HttpResponse
from django.views.generic import ListView
from web.models import Library

class LibraryListView(ListView):
    model = Library

def home_page(request):
    pass