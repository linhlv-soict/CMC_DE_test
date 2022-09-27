from django.http import JsonResponse
from .models import SensorData
from .serializers import DataSerializers, FileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

@api_view(['POST'])
def put_data(request):

    if request.method == 'POST':
        # serializer = DataSerializers(data=request.data)
        serializer =  FileSerializer(data=request.data)
        file_uploaded = request.FILES.get('file')
        content_type = file_uploaded.content_type

        if serializer.is_valid():
            print("POST API and you have uploaded a {} file".format(content_type))

            data = pd.read_csv(file_uploaded)
            
            data_dict = data.to_dict('records')
            saved = []
            for record in data_dict:
                print(record)
                sensor_data_serializer = DataSerializers(data=record)
                if sensor_data_serializer.is_valid():
                    sensor_data_serializer.save()
                    saved.append(record)

                    # return Response(sensor_data_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    print(sensor_data_serializer.errors)
            return Response(saved, status=status.HTTP_201_CREATED)

        return Response(request.data ,status=status.HTTP_404_NOT_FOUND)
