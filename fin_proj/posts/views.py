import email
from .models import *
# from multiprocessing import context
# from django.urls import reverse_lazy
from .models import *
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib import messages
from .models import Order
import os
from django.core.mail import send_mail
from django.core.mail import EmailMessage
# Create your views here.
from django.shortcuts import render, redirect 
from django.contrib import messages
from .forms import AddPostForm


from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
# Create your views here.

def homepage(request):
    kala=Kala.objects.all()
    places = InfoTravel.objects.all()
    return render(request,'posts/homepage.html',{'kala':kala, "places":places})

def show_slug(request, post_slug):
    post=get_object_or_404(InfoTravel, name=post_slug)
    context={'post':post}
    return render(request,'posts/charyn.html',context=context)

def show_id(request, post_id):
    post=get_object_or_404(InfoTravel, pk=post_id)
    context={'post':post}
    return render(request,'posts/burabai.html',context=context)

def placesBySlug(request, post_slug):
    place=get_object_or_404(InfoTravel, name=post_slug)

    return render(request, "posts/burabai.html", {"place":place})
 

def about(request):
    service= Service.objects.all()
    second=Second.objects.all()
    return render(request,'posts/about.html',{'service':service, 'second':second})

def contactus(request):
    return render(request,'posts/contactus.html')


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        number = request.POST['number']
        user_ordect = Order.objects.filter(number=number).count()
        if user_ordect > 0:
            messages.success(request, 'Number already exists')
            return redirect(request.META.get('HTTP_REFERER'))
        number_people = request.POST['number_people']
        demalys_orny = request.POST['demalys_orny']
        oz_kalasy = request.POST['oz_kalasy']
  
        order = Order.objects.create(name=name, number=number, number_people=number_people,
                                oz_kalasy=oz_kalasy,demalys_orny=demalys_orny
                                  )
        order.save()
        messages.success(request, "Order was inserted")
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        content = {
            'userData': Order.objects.all()
        }
        return render(request, 'posts/index.html', content)

def delete(request, id):
    if  Order.objects.get(id=id).delete():
        messages.success(request, "Order was deleted")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, "Order was not deleted")
        return redirect(request.META.get('HTTP_REFERER'))


def edit(request, id):
    if request.method == "POST":
        user_ord = Order.objects.get(id=id)
        user_ord.name = request.POST['name']
        user_ord.number = request.POST['number']
        user_ord.number_people = request.POST['number_people']
        user_ord.demalys_orny = request.POST['demalys_orny']
        user_ord.oz_kalasy = request.POST['oz_kalasy']
      
        user_ord.save()
        messages.success(request, "Order was updated")
        return redirect('/order/')
    
    else:
        content = {
            'userData': Order.objects.get(id=id)
        }
        return render(request, 'posts/index_2.html', content)


def gallery(request):
    return render(request,'posts/gallery.html')

def prices(request):
    price=Price.objects.all()
    pricee=Pricee.objects.all()
    return render(request,'posts/prices.html',{'price':price, 'pricee':pricee})

def signup(request):
    if request.method=='POST':
        form=AddPostForm(request.POST)
        #print(request.POST)
        email=request.POST['email']
        pochta=request.POST['pochta']
        poshta=request.POST['poshta']
        send_mail("Travel","Welcome!",
                   "200103157@stu.sdu.edu.kz",
                   [email,poshta, pochta],
                   fail_silently=False, html_message="<b>Your order are awesome</b>")
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                form.save()
                # Userinfo.objects.create(**form.cleaned_data)
                return redirect('show_post')
            except:
                #return redirect('show_post')
                form.add_error(None,'Koldanushy koskanda  kate wykty.')
    else:
        form=AddPostForm()
    return render(request,'posts/registration.html', {'title':'Koldanushy kosu ','form':form})

def show_post(request):
        post=Registration.objects.all().order_by('-id')[:1]
        context={'post':post}
        return render(request,'posts/post.html', context=context)

# def send(request):
    # email=EmailMessage("Travel","Welcome!",
    #           "200103157@stu.sdu.edu.kz",
    #           ["kezhanna.03@mail.ru","200103157@stu.sdu.edu.kz"],
    #           headers={'Message-ID':'foo'},)
    # email.attach_file('C:/Users/Жанна/Desktop/Front End/bonusproject/b2.jpg')
    # email.send(fail_silently=False)
    # return render(request,'posts/homepage.html')  
# def burabai(request):
#     return render(request, 'posts/burabai.html')


def getarea(radius):
    return 3.14*radius*radius

   
