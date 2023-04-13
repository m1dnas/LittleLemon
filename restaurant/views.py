from django.shortcuts import render

from rest_framework import generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

from .serializers import BookingSerializer, MenuSerializer

from .models import Menu


def index(request):
    return render(request, 'index.html', {})

class menuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class singleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# LO COMENTADO ES SIN GENERICS VIEWS
# ----------------------------------

# @api_view(['POST', 'GET'])
# def menuItemView(request, ListCreateView):
#     if request.method == 'POST':
#         serializer = MenuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'GET':
#         items = Menu.objects.all().order_by('id')
#         serializer = MenuSerializer(items, many=True)
#         return Response(serializer.data)

# @api_view('GET', 'PUT', 'DELETE')
# def singleMenuItemView(request, item_id, RetrieveUpdateAPIView, DestroyAPIView):
#     try:
#         item = Menu.objects.filter(id=item_id)
#     except Menu.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MenuSerializer(item, many=False)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = MenuSerializer(item, data=request.data, many=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)