from rest_framework import serializers
from .models import Student, Marks



class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model= Marks
        fields=['id', 'marks', 'subject']

class StudentSerializer(serializers.ModelSerializer):
    percentage=serializers.SerializerMethodField()
    total_marks=serializers.SerializerMethodField()
    marks=MarksSerializer(many=True, read_only=True)
    
    class Meta:
        model= Student
        fields=['id', 's_name', 'roll', 'address', 'total_marks', 'percentage', 'marks']
    
    def create(self, validated_data):   # to get marks input under the student class. 
        marks = validated_data.pop('marks')
        student =Student.objects.create(**validated_data)
        for i in marks:
            Marks.objects.create(**i, student=student)
        return student
        
    def get_total_marks(self, student):

        total=sum(Marks.objects.filter(student=student).values_list('marks', flat=True))
        return total

    def get_percentage(self, student):
        obtained_marks= sum(Marks.objects.filter(student=student).values_list('marks', flat=True))
        percentage= (obtained_marks*100)/800
        percentage= str(percentage)+'%'
        return percentage






