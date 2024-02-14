from django.db import models
from django.urls import reverse
# Create your models here.
class Kala(models.Model):
    kala=models.CharField(max_length=255)
   
    def __str__(self):
        return self.kala
    
class Service(models.Model):
    service=models.CharField(max_length=125)
   
    def __str__(self):
        return self.service
    
class Second(models.Model):
    second=models.CharField(max_length=255)
   
    def __str__(self):
        return self.second

class Price(models.Model):
    kala = models.CharField(max_length=255, verbose_name="Kala",default='') 
    hotel = models.CharField(max_length=255, verbose_name="Hotel")
    transport=models.TextField(blank=True,default='', verbose_name="Transport")
    sight = models.CharField(max_length=255, verbose_name="Sight")
    meal=models.TextField(blank=True,default='', verbose_name="Meal")
    price = models.IntegerField(verbose_name='Bagga',default=20000)
    
    def __str__(self):
        return self.kala

class Pricee(models.Model):
    kala = models.CharField(max_length=255, verbose_name="Kala",default='') 
    hotel = models.CharField(max_length=255, verbose_name="Hotel")
    transport=models.TextField(blank=True,default='', verbose_name="Transport")
    sight = models.CharField(max_length=255, verbose_name="Sight")
    meal=models.TextField(blank=True,default='', verbose_name="Meal")
    price = models.IntegerField(verbose_name='Bagga',default=20000)
    
    def __str__(self):
        return self.kala
    
 
class Order(models.Model):
    num_people_filed = [
        ('1-2', '1-2'),
        ('3-5', '3-5'),
        ('5-10', '5-10'),
        ('10-15', '10-15')
    ]
    kala_filed = [
        ('Shym', 'Shymkent'),
        ('Ala', 'Almaty'),
        ('As', 'Astana')
    ]
    name = models.CharField(max_length=255)
    number = models.IntegerField(verbose_name='Nomer',default=87716952079)
    number_people = models.CharField(choices=num_people_filed, max_length=125)
    demalys_orny = models.CharField(max_length=100)
    oz_kalasy = models.CharField(choices=kala_filed,max_length=100)

    def __str__(self):
        return self.demalys_orny   
   
class Registration(models.Model):
    esim = models.CharField(max_length=255, verbose_name="Esimi",default='') 
    nomer = models.IntegerField(verbose_name='Nomeri',default=87777777777)
    kala = models.CharField(max_length=255, verbose_name="Kalasy",default='') 
    email=models.EmailField(blank=True,default='@stu.sdu.edu.kz',verbose_name='Elektrondyk poshta')
    pochta=models.EmailField(blank=True,default='@stu.sdu.edu.kz',verbose_name='Ekinshi Elektrondyk poshta')
    poshta=models.EmailField(blank=True,default='@stu.sdu.edu.kz',verbose_name='Ushinshi Elektrondyk poshta')
    slug=models.SlugField(max_length=255,default='', unique=True, db_index=True, verbose_name="URL")
    is_published=models.BooleanField(default=True, verbose_name="Kelisim")

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

class InfoTravel(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title",default='')
    name=models.SlugField(max_length=255, verbose_name="Url",unique=True, db_index=True) 
    location = models.CharField(max_length=255, verbose_name="Ornalaskan zheri",default='') 
    climate = models.CharField(verbose_name='Klimat',max_length=255)
    flora = models.CharField(max_length=255, verbose_name="Osimdik",default='') 
    legend =models.CharField(max_length=255, verbose_name="Angyz",default='')
    image = models.ImageField(default='default value',upload_to='img', blank=True, null=True,verbose_name='Suret')
    description=models.TextField()
    imagetag = models.ImageField(default='default value',upload_to='img', blank=True, null=True,verbose_name='Suretteg')
    
    def __str__(self):
        return self.name   
    
    def get_absolute_url(self):
        return reverse('place', kwargs={'post_slug': self.name})

    def set_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

   
# class Mosts(models.Model):
#     title=models.CharField(max_length=255, verbose_name="Takyryp")
#     is_published=models.BooleanField(default=True,verbose_name="Wyggarylym")
    

# class Tosts(models.Model):
#     title=models.CharField(max_length=255, verbose_name="Takyryp")
#     is_published=models.BooleanField(default=True,verbose_name="Wyggarylym")  
#     slug=models.SlugField(max_length=255, verbose_name='URL',unique=True, db_index=True)  
    
#     def get_absolute_url(self):
#         return reverse("post", kwargs={"post_slug": self.slug})
 