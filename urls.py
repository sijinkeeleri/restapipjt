from django.urls import path
from . import views 
urlpatterns = [
    path('mybook/<int:pk>/', views.MybookViews.as_view(), name="mybookview"),
    path('', views.MybookCreateViews.as_view(), name="createBook"),
]    