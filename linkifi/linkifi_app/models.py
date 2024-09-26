from django.db import models
from django.contrib.auth.models import User
from .validators import validate_svg
from datetime import datetime
# Create your models here.



class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.name

class Signup(models.Model):
   username = models.CharField(max_length = 155)
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   email = models.CharField(max_length=155)
   password = models.CharField(max_length=155)
   repeatpassword = models.CharField(max_length=155)
   date = models.DateField()

   def __str__(self):
      return self.username


class Loginusername(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   loginusernameoneg = models.CharField(max_length=555)
   date = models.DateField()

   def __str__(self):
      return self.loginusernameoneg

class Contact(models.Model):
   name = models.CharField(max_length=155)
   email = models.EmailField()
   textarea = models.TextField()
   date = models.DateTimeField()

   def __str__(self):
      return self.name

class Platform(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='platform_images/', validators=[validate_svg], null=True, blank=True)
    
    date = models.DateTimeField()
 
    def __str__(self):
        return self.name

    
class Platformone(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='platform_images/', validators=[validate_svg], null=True, blank=True)
    
    date = models.DateTimeField()
 
    def __str__(self):
        return self.name

class PlatformThree(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='platform_images/', validators=[validate_svg], null=True, blank=True)
    
    date = models.DateTimeField()
 
    def __str__(self):
        return self.name
class PlatformFour(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='platform_images/', validators=[validate_svg], null=True, blank=True)
    
    date = models.DateTimeField()
 
    def __str__(self):
        return self.name
class PlatformFive(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='platform_images/', validators=[validate_svg], null=True, blank=True)
    date = models.DateTimeField()
 
    def __str__(self):
        return self.name
    
class URL(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    field = models.CharField(max_length=155)
    url = models.CharField(max_length=155)
    urlone = models.CharField(max_length=155)
    urltwo = models.CharField(max_length=155)
    date = models.DateField()

    def __str__(self):
        return self.field

class Adminpage(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='platform_images/', validators=[validate_svg], null=True, blank=True)
    date = models.DateTimeField()
 
    def __str__(self):
        return self.name
    
class Shopee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shopurl = models.CharField(max_length=655)
    date = models.DateField()


    def __str__(self):
        return self.shopurl

class Shopproduct(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    shopeurlone = models.CharField(max_length=600)
    title = models.TextField(max_length=600)
    price = models.IntegerField()
    currency = models.CharField(max_length=600)
    selected_picture = models.CharField(max_length=255, blank=True, null=True)
    profileimage = models.ImageField(upload_to='shop/images', null=True, blank=True)


    date = models.DateField()

    def __str__(self):
        return self.shopeurlone



class SettingPage(models.Model):
    pexiid = models.IntegerField()
    api = models.CharField(max_length=500)
    googleid = models.CharField(max_length=400)
    date = models.DateField()


    def __str__(self):
        return self.api
class Setting(models.Model):
    seotitle = models.CharField(max_length=500)
    seodescription = models.CharField(max_length=400)
    date = models.DateField()


    def __str__(self):
        return self.seotitle
class Urladmin(models.Model):
    nameadmin = models.CharField(max_length=200)
    urladmin = models.CharField(max_length=500)
    date = models.DateField()


    def __str__(self):
        return self.nameadmin
    
class OrderProduct(models.Model):
    orderurl = models.CharField(max_length=200)
    ordertitle = models.CharField(max_length=500)
    orderprice = models.IntegerField()
    ordercurrency = models.CharField(max_length=500)
    orderfirstname = models.CharField(max_length=200)
    orderlastname = models.CharField(max_length=500)
    orderemail = models.EmailField()
    orderphone = models.CharField(max_length=500)
    orderaddress = models.CharField(max_length=200)
    ordercity = models.CharField(max_length=500)
    cashdelivery = models.BooleanField(default=False)    
    date = models.DateField()


    def __str__(self):
        return self.orderfirstname

class Settingform(models.Model):
    settingurl = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.settingurl

class Homeemail(models.Model):
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.TextField()
    profilePicture = models.ImageField(upload_to='shop/images', blank=True, null=True)  # Allow null for no uploaded image
    selected_picture = models.CharField(max_length=255, blank=True, null=True)  # For preselected images
    date = models.DateField(default=datetime.now)


    def __str__(self):
        return self.name
