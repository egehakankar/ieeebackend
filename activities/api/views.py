from rest_framework.generics import ListAPIView, RetrieveAPIView
from activities.models import Technical, Social
from .serializers import TechnicalActivitiesSerializer, SocialActivitiesSerializer

class TechnicalActivitiesListView(ListAPIView):
    queryset = Technical.objects.all()
    serializer_class = TechnicalActivitiesSerializer

class TechnicalActivitiesDetailView(RetrieveAPIView):
    queryset = Technical.objects.all()
    serializer_class = SocialActivitiesSerializer

class SocialActivitiesListView(ListAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialActivitiesSerializer

class SocialActivitiesDetailView(RetrieveAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialActivitiesSerializer

