from rest_framework import serializers
from .models import Singer, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        exclude = ['singer']
        # fields = ['id', 'title', 'duration', 'singer']



class SingerSerializer(serializers.ModelSerializer):
    #using the serializer relation''''''.
    # song=serializers.StringRelatedField(many=True, read_only=True)
    # song=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    
    #using the nested serializer 
    song=SongSerializer(many=True)
    class Meta:
        model=Singer
        fields = ['id', 'name', 'gender', 'song']

    def create(self, validated_data):
        song = validated_data.pop('song')
        singer =Singer.objects.create(**validated_data)
        for i in song:
            Song.objects.create(**i, singer=singer)
        return singer



