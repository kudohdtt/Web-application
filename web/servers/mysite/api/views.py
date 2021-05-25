from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Hotel
from .serializer import HotelSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ListCreateHotelView(ListCreateAPIView):
    model = Hotel
    serializer_class = HotelSerializer

    def get_queryset(self):
        return Hotel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = HotelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Hotel successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Hotel unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteHotelView(RetrieveUpdateDestroyAPIView):
    model = Hotel
    serializer_class = HotelSerializer

    def put(self, request, *args, **kwargs):
        Hotel = get_object_or_404(Hotel, id=kwargs.get('pk'))
        serializer = HotelSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Hotel successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Hotel unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        Hotel = get_object_or_404(Hotel, id=kwargs.get('pk'))
        Hotel.delete()

        return JsonResponse({
            'message': 'Delete Hotel successful!'
        }, status=status.HTTP_200_OK)

def FindbyName(request):
    if request.method == 'POST':
        key = request.POST['address']
        result = Hotel.objects.filter(address__startswith=key)
        if result:
        
            data = list(result.values())

            return JsonResponse({'data': data,'result': len(data)})

        return JsonResponse({
        'result': 0,
    }, status=status.HTTP_400_BAD_REQUEST)
#     

# def FindbyName(request):
#     if request.method == 'POST':
#         key = request.POST['address']

#         num_of_page = request.POST.get("page")
#         num_of_page = int(num_of_page)

#         result = Hotel.objects.filter(address__startswith=key)
#         data = list(result.values())
#         amount_of_page = 2
#         i = 0
#         page = [] 
        
#         if result:
#             while(i<len(data)):
#                 try:
#                     for j in range(0,amount_of_page):
#                         page.append(data[i])
#                         i+=1
#                 except:
#                     print("range of index")
#                 i = i + amount_of_page                
            
#             if num_of_page > len(page):
#                 num_of_page = len(page)
#             elif num_of_page < 0 :
#                 num_of_page = 1

#             return JsonResponse({'data': page[num_of_page-1], 'result': len(data), 'len_page': len(page) , 'num_of_page' : num_of_page})

#         return JsonResponse({
#         'result': 0,
#     }, status=status.HTTP_400_BAD_REQUEST)
