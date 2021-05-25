from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
from home.models import Roomtype
from api.models import Hotel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail  
from django.http import JsonResponse
from home.models import Room
from home.models import Order
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(60 * 15)
def index(request):
    template = loader.get_template(r'index.html')
   
    context = {
        
    }
    return HttpResponse(template.render(context, request))

@cache_page(60 * 3600)
def blog(request):
    template = loader.get_template(r'blog.html')
    
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def order(request):
    template = loader.get_template(r'order.html')
    uid = request.GET.get('uid')
    try:
        data = Order.objects.filter(user_id=uid)
    except :
        data = False
    

    if data:
        context = {
            'orders' : data,
            'result' : True,
        }
    else:
        context={
            'result' : False,
        }
    return HttpResponse(template.render(context, request))

def orderdetail(request):
    template = loader.get_template(r'order-detail.html')
    order = Order.objects.get(id=request.GET.get('oid'))
    room = Room.objects.get(id=order.room.id)
    roomtype = Roomtype.objects.get(id=room.roomtype.id)
    hotel = Hotel.objects.get(id=order.hotel.id)
    context = {
        'order': order,
        'room' : room,
        'roomtype' : roomtype,
        'hotel' : hotel,
    }
    return HttpResponse(template.render(context, request))


def hotels(request):
    
    if request.method == 'POST':
        if request.POST['address']:
            context = {
                'address':request.POST['address'],
            }
            return render(request, 'hotels.html',context)

    return render(request, 'hotels.html')
    
@cache_page(60 * 3600)
def login(request):
    template = loader.get_template(r'login.html')
    
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def rooms(request, hotel_id):
    template = loader.get_template(r'rooms-tariff.html')
    data = Hotel.objects.get(id=hotel_id)
    room_data = data.roomtype_set.all()

    paginator = Paginator(room_data, 2)
    pageNumber = request.GET.get('page')

    try:
        roomtypes = paginator.page(pageNumber)
    except PageNotAnInteger:
        roomtypes = paginator.page(1)
    except EmptyPage:
        roomtypes = paginator.page(paginator.num_pages)
    
    
    # result = list(room_data.values())
    # print(result)
    return HttpResponse(template.render({'data': roomtypes,'hotel_id':hotel_id}, request))

def roomdetail(request, roomtype_id):
    template = loader.get_template(r'room-detail.html')
    data = Roomtype.objects.get(id=roomtype_id)
    # print(data)
    # result = list(data)
   
    context = {
        'roomtype' : data,
    }
    return HttpResponse(template.render(context, request))
@cache_page(60 * 3600)
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bookingroom/login')
        else:
            error = [form.errors.get('username'),form.errors.get('password2')]               
            return render(request, 'register.html',{'error': error})
        # else:
        #     return render(request, 'register.html',{'error': 'Mật khẩu không hợp lệ'})
    return render(request, 'register.html',{'error': False})

def sendEmailConfirm(request):

    if request.method == 'POST':
        key = 'BK2001'

        string = 'Dear ' + request.POST.get('username') + r', Thanks for your trust with Bookingroom. This is your confirm code : ' + key + r' From Bookingroom team.'
        status = send_mail( 'Confirm for your action', string , 'bookingroom.group@gmail.com', [request.POST.get('email')],fail_silently=False )
        
        if status:

            return JsonResponse({'status' : True, 'code' : key})
        
    return JsonResponse({'status' : False})


def createOrder(request):
    template = loader.get_template(r'index.html')

    if request.method == 'POST':
        o = Order(user_id = request.POST.get('user_id'),hotel = Hotel.objects.get(id=request.POST.get('hotel_id')) , room = Room.objects.get(hotel=Hotel.objects.get(id=request.POST.get('hotel_id')), 
         roomtype = Roomtype.objects.get(id = request.POST.get('roomtype_id'))  ) )
        o.save()
    
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def deleteOrder(request):
    template = loader.get_template(r'index.html')

    if request.method == 'POST':
        o = Order.objects.get(id=request.POST.get('order_id'))
        status = o.delete()
    
    context = {
        
    }
    return HttpResponse(template.render(context, request))

    #