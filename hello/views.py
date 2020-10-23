from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
from .models import Hello
from django.views.generic.base import TemplateView
import hello
from django.views.generic import DetailView,ListView


class IndexView(TemplateView):
    template_name = "hello/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['one_name'] = Hello.objects.all()[0]
        return context
    
class NameListView(ListView):
    model = Hello
    
    
class NameDetailView(DetailView):
    model = Hello