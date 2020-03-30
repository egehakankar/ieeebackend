from rest_framework import serializers
from activities.models import Technical, Social

class TechnicalActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technical
        fields = ('id', 'title', 'branch', 'backGroundPhoto', 'littleSummary', 'smallDescription', 'longDescription', 'firstPhoto', 'secondPhoto', 'date')

class SocialActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('id', 'title', 'branch', 'backGroundPhoto', 'littleSummary', 'smallDescription', 'longDescription', 'firstPhoto', 'secondPhoto', 'date')
