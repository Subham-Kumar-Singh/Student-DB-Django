from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeFunc, name='homeFunc'),
    path('add_Entry/', views.addFunc, name='addFunc'),
    path('delete_Form/<str:pk>/', views.deleteForm, name='deleteForm'),
    path('update_Form/<str:pk>/', views.updateForm, name='update_Form'),
]
