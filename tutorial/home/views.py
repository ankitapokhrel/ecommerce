# from django.http import HttpResponse
# from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer
from home import serializer

# Create your views here.
'''  ####  for returning html
def index(request):
    data={
        'title': 'Homepage'
    }
    return render(request, 'index.html', data)
    #return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is service page")

def contact(request):
    return HttpResponse("this is contact page")
'''


@api_view(['GET', 'POST', 'PATCH'])  #don't need to write get for getting the data on @api_view() function '''
def home(request):
    if request.method == 'GET':
        return Response({
            'status':200,
            'message' : 'yes! Django rest framwork is working.',
            'method=_called': 'You called GET method'
         })
    elif request.method =='POST':
        return Response({
            'method': 200,
            'message': 'Django is still working',
            'method_called':'you called POST method'
        })
    elif request.method =='PATCH':
        return Response({
            'status':200,
            'message' : 'yes! Django rest framwork is working.',
            'method=_called': 'You called PATCH method'
         })
    else:
        return Response({
           'status':400,
            'message' : 'yes! Django rest framework is working.',
            'method=_called': 'You called invalid method'
         }) 


@api_view(['POST']) 
def post_todo(request):
    try:
        data = request.data
        print(data)
        serializer=TodoSerializer(data=data)
        if serializer.is_valid(raise_exception=True): 
            
            serializer.save() #for automatically saving the valid data.
            return Response({
                'status': True,
                'message': 'success data',
                'data': serializer.data
            })
    
        
        return Response({
            'status': False,
            'message':'Invalid data',
            'data': serializer.errors
        })
            
    except Exception as e:
        print(e)
        return Response({
           'status':False,
            'message' : 'Something went wrong',
            
         })  
    
   