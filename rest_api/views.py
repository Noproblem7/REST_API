from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Album, Artist, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer


class ArtistAPIView(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)

        return Response(data=serializer.data)


class AlbumAPIView(APIView):
    def get(self, request):
        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)

        return Response(data=serializer.data)


class SongAPIView(APIView):
    def get(self, request):
        queryset = Song.objects.all()
        serializer = SongSerializer(queryset, many=True)
        return Response(data=serializer.data)
