from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('cats/', views.CatList.as_view(), name="cat_list"),
    path('cats/new', views.Cat_Create.as_view(), name="cat_create"),
    path('cats/<int:pk>/', views.CatDetail.as_view(), name="cat_detail"),
    path('cats/<int:pk>/update', views.CatUpdate.as_view(), name="cat_update"),
    path('cats/<int:pk>delete', views.CatDelete.as_view(), name="cat_delete_confirmation")
]