from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Equipments
from .serializer import EquipmentSerializer
from django.http import JsonResponse
# Create your views here.



class CreateItemEntry(APIView):
    def post(self, request):
        print(request.data)
        serialize_data = EquipmentSerializer(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data,status=status.HTTP_200_OK)
        return Response(serialize_data.errors,status=status.HTTP_400_BAD_REQUEST)



class UpdateItemQuantity(APIView):
    def patch(self, request, pk):
        item = get_object_or_404(Equipments, pk=pk)
        quantity = request.data.get('quantity', None)
        if quantity or quantity == 0:
            item.quantity = quantity
            item.save()
            return Response(str(item),status=status.HTTP_200_OK)
        return Response({'error':"Invalid"} ,status=status.HTTP_400_BAD_REQUEST)


class UnavailableItemsView(APIView):
    def get(self, request):
        unavailable_items = Equipments.objects.filter(quantity=0)
        serializer = EquipmentSerializer(unavailable_items, many=True)
        return Response(serializer.data)


class AllavailableItems(APIView):
    def get(self, request):
        a = Equipments.objects.all().values()
        return Response({'All Data is':str(a)})


