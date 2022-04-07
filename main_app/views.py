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

from django.contrib.auth.models import User
# import models
from .models import Cat, CatToy

# Create your views here.
class Home(TemplateView):
   template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'

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
   fields = ['name', 'img', 'age', 'gender', 'user', 'cattoys']
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
    fields = ['name', 'img', 'age', 'gender', 'cattoys']
    template_name = "cat_update.html"
    # success_url = "/cats"
    def get_success_url(self):
        return reverse('cat_detail', kwargs={'pk': self.object.pk})


class CatDelete(DeleteView):
    model = Cat
    template_name = "cat_delete_confirmation.html"
    success_url = "/cats/"




def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})



def cattoys_index(request):
    cattoys = CatToy.objects.all()
    return render(request, 'cattoy_index.html', {'cattoys': cattoys})

def cattoys_show(request, cattoy_id):
    cattoy = CatToy.objects.get(id=cattoy_id)
    return render(request, 'cattoy_show.html', {'cattoy': cattoy})

class CatToyCreate(CreateView):
    model = CatToy
    fields = '__all__'
    template_name = "cattoy_form.html"
    success_url = '/cattoys'

class CatToyUpdate(UpdateView):
    model = CatToy
    fields = ['name', 'color']
    template_name = "cattoy_update.html"
    success_url = '/cattoys'

class CatToyDelete(DeleteView):
    model = CatToy
    template_name = "cattoy_confirm_delete.html"
    success_url = '/cattoys'