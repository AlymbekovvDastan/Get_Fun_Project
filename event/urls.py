from django.urls import path
from .views import *

urlpatterns = [
    path('', EventList.as_view(), name='index'),
    path('<int:pk>/', EventDetail.as_view(), name='event_detail'),
    path('category/<int:pk>/', filter_by_category, name='category'),
    path('tag/<int:pk>/', filter_by_tag, name='tag'),
    path('date/', filter_by_date, name='date'),
]