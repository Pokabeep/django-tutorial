from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('thoughts/', views.thoughts, name='thoughts'),
    path('addthoughts/', views.addthoughts, name='addthoughts'),
    path('thoughts/list/', views.AllThoughtsView.as_view(), name='allthoughts'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]