from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer
from .models import Car


@api_view(['GET', 'POST'])
def cars_list(request):
    
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CarSerializer(data = request.data)
        if serializer.is_valid == True:
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)