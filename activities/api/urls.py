from django.urls import path, include
from .views import TechnicalActivitiesListView, TechnicalActivitiesDetailView, SocialActivitiesListView, SocialActivitiesDetailView

urlpatterns = [
    path('technical/', TechnicalActivitiesListView.as_view()),
    path('technical/<pk>', TechnicalActivitiesDetailView.as_view()),
    path('social/', SocialActivitiesListView.as_view()),
    path('social/<pk>', SocialActivitiesDetailView.as_view()),
]
