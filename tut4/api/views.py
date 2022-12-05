from django.shortcuts import render
from .models import Singer, Song 
from rest_framework import viewsets 
from .serializers import SingerSerializer, SongSerializer

from rest_framework.response import Response
from rest_framework import status

from django.db.models import Avg, Sum, Max, Min, Aggregate
from rest_framework.decorators import action


# Create your views here.

class SingerViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer
    http_method_names = ['get', 'list', 'head','post']

    def list(self, request, **kwargs):  
        data = {} 

        
        # total_duration = Song.objects.all().aggregate(Sum("duration"))
        # avg_duration = Song.objects.all().aggregate(Avg("duration"))
        # max_duration= Song.objects.all().aggregate(Max('duration'))
        # min_duration= Song.objects.values('duration').aggregate(Min('duration'))
        # data['duration']=total_duration
        # data['avg']=avg_duration
        # data['min']=min_duration       
        # data['max']=max_duration
        
        song_features =Song.objects.values('duration').aggregate(
            duration_sum= Sum('duration'),
            max_duration= Max('duration'),
            min_duration=Min('duration'),
            avg_duration=Avg('duration')
        )
        
        data['Song_info']=song_features
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path='song-list')
    def song_list(self, request):
        data={}
        song_data= Song.objects.all()
        serializer = SongSerializer(song_data, many=True)
        data['song_data']= serializer.data
        return Response(data, status=status.HTTP_200_OK)




        