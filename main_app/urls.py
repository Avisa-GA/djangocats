from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name="about"),
    path('cats/', views.CatList.as_view(), name="cat_list"),
    path('cats/new', views.Cat_Create.as_view(), name="cat_create"),
    path('cats/<int:pk>/', views.CatDetail.as_view(), name="cat_detail"),
    path('cats/<int:pk>/update', views.CatUpdate.as_view(), name="cat_update"),
    path('cats/<int:pk>delete', views.CatDelete.as_view(), name="cat_delete_confirmation"),
    path('user/<username>/', views.profile, name='profile'),
    path('cattoys/', views.cattoys_index, name='cattoys_index'),
    path('cattoys/<int:cattoy_id>', views.cattoys_show, name='cattoys_show'),
    path('cattoys/create/', views.CatToyCreate.as_view(), name='cattoys_create'),
    path('cattoys/<int:pk>/update/', views.CatToyUpdate.as_view(), name='cattoys_update'),
    path('cattoys/<int:pk>/delete/', views.CatToyDelete.as_view(), name='cattoys_delete'),
]