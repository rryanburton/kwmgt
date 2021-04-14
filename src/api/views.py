from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from spotify.models import Artist


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            'name',
            'followers_total',
            'spotify_id',
            'id',
            'image',
            'popularity',
            'uri',
            'created_date',
            'modified_date',
        ]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'artists', ArtistViewSet)
