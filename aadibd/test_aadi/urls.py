from django.urls import path

from . import views

app_name='test_aadi'
urlpatterns = [    
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.SessionDetailView.as_view(),name='sessiondetail'),
    path('add/',views.InterviewCreate.as_view(),name='interview-add'),
 
]