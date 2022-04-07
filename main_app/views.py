from django.shortcuts import render
# from django.views import View # <- View class to handle requests
from django.http import HttpResponse
#...
from django.views.generic.base import TemplateView 
# <- a class to handle sending a type of response

# This will import the class we are extending 
from django.views.generic.edit import CreateView

# after our other imports 
from django.views.generic import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from django.http import HttpResponseRedirect

# import models
from .models import Cat

# Create your views here.
class Home(TemplateView):
   template_name = 'home.html'



class CatList(TemplateView):
    template_name = "catlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["cats"] = Cat.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["cats"] = Cat.objects.all()
            # default header for not searching 
            context["header"] = "Our Cats"
        return context


# main_app/views.py
class Cat_Create(CreateView):
   model = Cat
   fields = ['name', 'img', 'age', 'gender', 'user']
   template_name = "cat_create.html"
    # success_url = "/cats/"

   def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/cats')



class CatDetail(DetailView):
    model = Cat
    template_name = "cat_detail.html"



class CatUpdate(UpdateView):
    model = Cat
    fields = ['name', 'img', 'age', 'gender']
    template_name = "cat_update.html"
    # success_url = "/cats"
    def get_success_url(self):
        return reverse('cat_detail', kwargs={'pk': self.object.pk})


class CatDelete(DeleteView):
    model = Cat
    template_name = "cat_delete_confirmation.html"
    success_url = "/cats/"