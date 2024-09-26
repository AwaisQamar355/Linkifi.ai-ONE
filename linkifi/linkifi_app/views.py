from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login , logout
from linkifi_app.models import Signup
from datetime import datetime
from linkifi_app.models import Loginusername
from linkifi_app.models import Contact
from django.contrib import messages
from linkifi_app.models import Platform
from linkifi_app.models import Platformone
from linkifi_app.models import PlatformThree
from linkifi_app.models import PlatformFour
from linkifi_app.models import PlatformFive
from linkifi_app.models import URL
from linkifi_app.models import Profile
from linkifi_app.models import Adminpage
from linkifi_app.models import Shopee
from linkifi_app.models import Shopproduct
from django.http import JsonResponse
from linkifi_app.models import SettingPage
from linkifi_app.models import Setting
from linkifi_app.models import Urladmin
from linkifi_app.models import OrderProduct
from linkifi_app.models import Settingform
from linkifi_app.models import Homeemail
from django.utils import timezone
# from django.urls import reverse
# # Create your views here.
def home(request):
    HttpResponse("Welcome to Home Page")
    if request.method == "POST":
        email = request.POST.get("email")

        home = Homeemail(email=email, date=datetime.today())
        home.save()
    return render(request , 'home.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request, user)
            return redirect("loginusername")
        else:
            return redirect("signup")

    return render(request , 'login.html')
def logoutuser(request):
    logout(request)
    return render(request , 'logout.html')
def signup(request):
    HttpResponse("Hello Welcome to your home page")
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repeatpassword = request.POST.get("repeatpassword")
        
        sign = Signup(username=username , first_name = first_name , last_name = last_name , email = email , password =  password , repeatpassword = repeatpassword ,date = datetime.today())
        sign.save()

        if User.objects.filter(username = username).exists():
            error_message = 'Username already taken. Please choose a different username.'
            return render(request , 'signup.html' ,{'error_message' : error_message})
        
        if password != repeatpassword:
            return HttpResponse("Your Password and confirm password are not the same!")
        
        else:
            myuser = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password)
            myuser.save()
        return redirect('login')
    return render(request,'signup.html')


def pricing(request):
    HttpResponse("Welcome to pricing Page")
    return render(request , 'pricing.html')
def Feature(request):
    HttpResponse("Welcome to Feature Page")
    return render(request , 'Feature.html')
def About(request):
    HttpResponse("Welcome to About Page")
    return render(request , 'About.html')

def loginusername(request):
    if request.method == "POST":
        loginusernameoneg = request.POST.get("loginusernameoneg")
        if not loginusernameoneg.startswith('Linkifi.ee/'):
            loginusernameoneg = 'Linkifi.ee/' + loginusernameoneg

        # Check if the username is already taken
        if Loginusername.objects.filter(loginusernameoneg=loginusernameoneg).exists():
            context = {
                'error_message': 'This username is already taken. Please choose another one.',
            }
            return render(request, 'loginusername.html', context)

        # Check if the user already has a username, update it
        if Loginusername.objects.filter(user=request.user).exists():
            loginusernamevalue = Loginusername.objects.get(user=request.user)
            loginusernamevalue.loginusernameoneg = loginusernameoneg
            # loginusernamevalue.save()  # Save the updated value
        else:
            loginusernamevalue = Loginusername.objects.create(
                user=request.user,
                loginusernameoneg=loginusernameoneg,
                date=datetime.today(),
            )
            loginusernamevalue.save()
            return redirect('Select_plan')  
    return render(request, 'loginusername.html')
def Select_plan(request):
    HttpResponse("Welcome to Selectplan Page")
    return render(request , 'Select_plan.html')

def contact(request):
    HttpResponse("Welcome to contact Page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        textarea = request.POST.get('textarea')

        contact = Contact(name = name , email = email , textarea = textarea , date = datetime.today())
        contact.save()
        messages.success(request, "Thank You!")
        
    return render(request , 'contact.html')

def billing_pro(request):
    HttpResponse("Welcome to billing_pro Page")
    return render(request , 'billing_pro.html')

def billing_enterprise(request):
    HttpResponse("Welcome to billing_enterprise Page")
    return render(request , 'billing_enterprise.html')

def select_template(request):
    HttpResponse("Welcome to select_template Page")
    return render(request , 'select_template.html')

def select_type(request):
    HttpResponse("Welcome to select_type Page")
    return render(request , 'select_type.html')

def select_platform(request):
    HttpResponse("Welcome to select_type Page")
    platform = Platform.objects.all()
    platformone = Platformone.objects.all()
    platformthree = PlatformThree.objects.all()
    platformfour = PlatformFour.objects.all()
    platformfive = PlatformFive.objects.all()


    context = {
        'platform': platform,
        'platformone': platformone,
        'platformfour': platformfour,
        'platformthree': platformthree,
        'platformfive': platformfive,
        
    }
    return render(request , 'select_platform.html' , context)

def Add_links(request):
    HttpResponse("Welcome to Add_links Page")
    if request.method == "POST":
        field = request.POST.get("field")
        url = request.POST.get("url")
        urlone = request.POST.get("urlone")
        urltwo = request.POST.get("urltwo")

        if URL.objects.filter(user=request.user).exists():
            pageurlsdata = URL.objects.get(user=request.user)
            pageurlsdata.field = field
            pageurlsdata.url = url
            pageurlsdata.urlone = urlone
            pageurlsdata.urltwo = urltwo
        else:
            # Create a new URL entry for the user
            pageurlsdata = URL.objects.create(
                user=request.user, 
                field=field, 
                url=url, 
                urlone=urlone, 
                urltwo=urltwo, 
                date=datetime.today()
            )
        pageurlsdata.save()
        return redirect("Add_profile")
    
    # pageurlsdata = URL.objects.filter(user=request.user)


    selected_image = request.GET.get('image_url', '/static/images/Platform images/default.svg')
    context = {'selected_image': selected_image}

    return render(request , 'Add_links.html' , context)

def Add_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        selected_picture = request.POST.get('selected_picture')
        profilePicture = request.FILES.get('profilePicture')

        # Check if profile already exists for the user
        if Profile.objects.filter(user=request.user).exists():
            profile = Profile.objects.get(user=request.user)
            profile.name = name
            profile.bio = bio
            profile.selected_picture = selected_picture
            if profilePicture:
                profile.profilePicture = profilePicture
        else:
            profile = Profile.objects.create(
                user=request.user,
                name=name,
                bio=bio,
                selected_picture=selected_picture,
                profilePicture=profilePicture,
                date=datetime.today()
            )
        
        profile.save()
        return redirect("profile_success")

    return render(request, 'Add_profile.html')


def profile_success(request):
    HttpResponse("Welcome to profile_success Page")
    # loginusernamevalue = Loginusername.objects.all()
    # pageurlsdata = URL.objects.all()

    # userprofile = Profile.objects.all()
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist

    try:
        pageurlsdata = URL.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pageurlsdata = None

    try:
        loginusernamevalue = Loginusername.objects.get(user=request.user)
    except Loginusername.DoesNotExist:
        loginusernamevalue = None

    # Pass loginusernamevalue to the template
    context = {
        'loginusernamevalue': loginusernamevalue,
        'profile': profile,
        'pageurlsdata':pageurlsdata,
    }
    return render(request , 'profile_success.html' , context)

def adminpage(request):
    HttpResponse("Welcome to adminpage Page")
    if request.method == "POST":
        nameadmin = request.POST.get("nameadmin")
        urladmin = request.POST.get("urladmin")

        adminpage = Urladmin(nameadmin = nameadmin , urladmin = urladmin , date = datetime.today())
        adminpage.save()

    # pageurlsdata = URL.objects.filter(user=request.user)
        
    # loginusernamevalue = Loginusername.objects.all()
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist

    try:
        pageurlsdata = URL.objects.get(user=request.user)
    except URL.DoesNotExist:
        pageurlsdata = None

    try:
        loginusernamevalue = Loginusername.objects.get(user=request.user)
    except Loginusername.DoesNotExist:
        loginusernamevalue = None  # Handle case where profile doesn't exist

    adminpage = Adminpage.objects.all()
    adminpageees = Urladmin.objects.all()
    adminpageone = Shopproduct.objects.all() 
    settingformurl = Settingform.objects.filter()

    context = {
        'loginusernamevalue':loginusernamevalue,
        'profile': profile,
        'adminpage':adminpage,
        'pageurlsdata': pageurlsdata,
        'adminpageees': adminpageees,
        'adminpageone': adminpageone,
        'settingformurl': settingformurl,
    }
    return render(request , 'adminpage.html', context)

def shop(request):
    HttpResponse("Welcome to shop Page")
    if request.method == "POST":
        shopurl = request.POST.get('shopurl')

        shop = Shopee(shopurl = shopurl , date = datetime.today())
        shop.save()

        return redirect('shopproduct')
    # loginusernamevalue = Loginusername.objects.all()
    # userprofile = Profile.objects.all()
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist

    try:
        pageurlsdata = URL.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pageurlsdata = None

    try:
        loginusernamevalue = Loginusername.objects.get(user=request.user)
    except Loginusername.DoesNotExist:
        loginusernamevalue = None

    adminpage = Adminpage.objects.all()
    # pageurlsdata = URL.objects.all()
    adminpageees = Urladmin.objects.all()
    adminpageone = Shopproduct.objects.all() 
    settingformurl = Settingform.objects.filter()

    context = {
        'loginusernamevalue':loginusernamevalue,
        'profile': profile,
        'adminpage':adminpage,
        'pageurlsdata': pageurlsdata,
        'adminpageees': adminpageees,
        'adminpageone': adminpageone,
        'settingformurl': settingformurl,
    }
    return render(request , 'shop.html' , context)

def appearance(request):
    HttpResponse("Welcome to appearance Page")
    # loginusernamevalue = Loginusername.objects.all()
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist

    try:
        pageurlsdata = URL.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pageurlsdata = None

    try:
        loginusernamevalue = Loginusername.objects.get(user=request.user)
    except Loginusername.DoesNotExist:
        loginusernamevalue = None



    adminpage = Adminpage.objects.all()
    # pageurlsdata = URL.objects.all()
    adminpageees = Urladmin.objects.all()
    adminpageone = Shopproduct.objects.all() 
    settingformurl = Settingform.objects.filter()

    context = {
        'loginusernamevalue':loginusernamevalue,
        'profile': profile,
        'adminpage':adminpage,
        'pageurlsdata': pageurlsdata,
        'adminpageees': adminpageees,
        'adminpageone': adminpageone,
        'settingformurl': settingformurl,
    }
    return render(request , 'appearance.html' , context)

def analytics(request):
    HttpResponse("Welcome to analytics Page")
    return render(request , 'analytics.html')

def setting(request):
    HttpResponse("Welcome to setting Page")
    if request.method == "POST":
        # Check which form is submitted by checking for a field specific to each form
        if 'pexiid' in request.POST:
            # Handle the SettingPage form
            pexiid = request.POST.get('pexiid')
            api = request.POST.get('api')
            googleid = request.POST.get('googleid')

            setting_page = SettingPage(pexiid=pexiid, api=api, googleid=googleid, date=datetime.today())
            setting_page.save()

            return redirect('setting')

        elif 'seotitle' in request.POST:
            # Handle the Setting form
            seotitle = request.POST.get('seotitle')
            seodescription = request.POST.get('seodescription')

            setting = Setting(seotitle=seotitle, seodescription=seodescription, date=datetime.today())
            setting.save()

            return redirect('setting')


        elif 'settingurl' in request.POST:

            settingurl = request.POST.get('settingurl')

            setting_url = Settingform(settingurl = settingurl , date = datetime.today())
            setting_url.save()
            return redirect('adminpage')

    
    # loginusernamevalue = Loginusername.objects.all()
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist

    try:
        pageurlsdata = URL.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pageurlsdata = None

    try:
        loginusernamevalue = Loginusername.objects.get(user=request.user)
    except Loginusername.DoesNotExist:
        loginusernamevalue = None

    adminpage = Adminpage.objects.all()
    # pageurlsdata = URL.objects.all()
    adminpageees = Urladmin.objects.all()
    adminpageone = Shopproduct.objects.all() 
    settingformurl = Settingform.objects.filter()

    context = {
        'loginusernamevalue':loginusernamevalue,
        'profile': profile,
        'adminpage':adminpage,
        'pageurlsdata': pageurlsdata,
        'adminpageees': adminpageees,
        'adminpageone': adminpageone,
        'settingformurl': settingformurl,
    }
    return render(request , 'setting.html' , context)

def shopproduct(request):
    HttpResponse("Welcome to shopproduct Page")
    if request.method == "POST":
        shopeurlone = request.POST.get('shopeurlone')
        title = request.POST.get('title')
        price = request.POST.get('price')
        currency = request.POST.get('currency')
        selected_picture = request.POST.get('selected_picture')
        profileimage = request.FILES.get('profileimage')

        # if Shopproduct.objects.filter(user=request.user).exists():
        #     shopproduct = Shopproduct.objects.get(user=request.user)
        #     shopproduct.shopeurlone = shopeurlone
        #     shopproduct.title = title
        #     shopproduct.price = price
        #     shopproduct.currency = currency
        #     shopproduct.selected_picture = selected_picture
        # if profileimage:
        #     shopproduct.profileimage = profileimage

        shopproduct = Shopproduct.objects.create(
            profileimage = profileimage, 
            shopeurlone = shopeurlone, 
            title = title, 
            price = price, 
            currency = currency, 
            selected_picture = selected_picture,
            date = datetime.today()
        )
        shopproduct.save()
        return redirect("showallproduct")
        
    # loginusernamevalue = Loginusername.objects.all()
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist

    try:
        pageurlsdata = URL.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pageurlsdata = None

    try:
        loginusernamevalue = Loginusername.objects.get(user=request.user)
    except Loginusername.DoesNotExist:
        loginusernamevalue = None

    adminpage = Adminpage.objects.all()
    # pageurlsdata = URL.objects.all()
    adminpageees = Urladmin.objects.all()
    adminpageone = Shopproduct.objects.all() 
    settingformurl = Settingform.objects.filter()

    context = {
        'loginusernamevalue':loginusernamevalue,
        'profile': profile,
        'adminpage':adminpage,
        'pageurlsdata': pageurlsdata,
        'adminpageees': adminpageees,
        'adminpageone': adminpageone,
        'settingformurl': settingformurl,
    }
    return render(request , 'shopproduct.html', context)

def showallproduct(request):
    HttpResponse("Welcome to showallproduct Page")
    # loginusernamevalue = Loginusername.objects.all()
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist

    try:
        pageurlsdata = URL.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pageurlsdata = None

    try:
        loginusernamevalue = Loginusername.objects.get(user=request.user)
    except Loginusername.DoesNotExist:
        loginusernamevalue = None


    adminpage = Adminpage.objects.all()
    # pageurlsdata = URL.objects.all()
    adminpageees = Urladmin.objects.all()
    adminpageone = Shopproduct.objects.all() 
    settingformurl = Settingform.objects.filter()

    context = {
        'loginusernamevalue':loginusernamevalue,
        'profile': profile,
        'adminpage':adminpage,
        'pageurlsdata': pageurlsdata,
        'adminpageees': adminpageees,
        'adminpageone': adminpageone,
        'settingformurl': settingformurl,
    }
    return render(request , 'showallproduct.html' , context)

def delete_product(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Shopproduct, id=product_id)
        product.delete()
        return JsonResponse({'status': 'Product deleted'})
    return JsonResponse({'status': 'Failed'}, status=400)


def shopsetting(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist
    pageurlsdata = URL.objects.all()
    shopproduct = Shopproduct.objects.all()
    context = {
        'pageurlsdata': pageurlsdata,
        'profile': profile,
        'shopproduct': shopproduct,
    }
    return render(request , 'shopsetting.html' , context)

def orderproduct(request):

    if request.method == "POST":
        orderurl = request.POST.get("orderurl")
        ordertitle = request.POST.get("ordertitle")
        orderprice = request.POST.get("orderprice")
        ordercurrency = request.POST.get("ordercurrency")
        orderfirstname = request.POST.get("orderfirstname")
        orderlastname = request.POST.get("orderlastname")
        orderemail = request.POST.get("orderemail")
        orderphone = request.POST.get("orderphone")
        orderaddress = request.POST.get("orderaddress")
        ordercity = request.POST.get("ordercity")
        cashdelivery = True if request.POST.get("cashdelivery") == "on" else False

        orderproduct = OrderProduct(orderurl = orderurl , ordertitle = ordertitle , orderprice = orderprice , 
                                    ordercurrency = ordercurrency , orderfirstname = orderfirstname , 
                                    orderlastname = orderlastname , orderemail = orderemail , orderphone = orderphone , 
                                    orderaddress = orderaddress , ordercity = ordercity , cashdelivery = cashdelivery , date = datetime.today())
        orderproduct.save()
        return redirect('shop')

    # loginusernamevalue = Loginusername.objects.all()
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist

    try:
        pageurlsdata = URL.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pageurlsdata = None

    try:
        loginusernamevalue = Loginusername.objects.get(user=request.user)
    except Loginusername.DoesNotExist:
        loginusernamevalue = None
    adminpage = Adminpage.objects.all()
    # pageurlsdata = URL.objects.all()
    adminpageees = Urladmin.objects.all()
    adminpageone = Shopproduct.objects.all() 
    settingformurl = Settingform.objects.filter()

    context = {
        'loginusernamevalue':loginusernamevalue,
        'profile': profile,
        'adminpage':adminpage,
        'pageurlsdata': pageurlsdata,
        'adminpageees': adminpageees,
        'adminpageone': adminpageone,
        'settingformurl': settingformurl,
    }
    return render(request , 'orderproduct.html' , context)

def helpcenter(request):
    return render(request , 'helpcenter.html')
def privacy(request):
    return render(request , 'privacy.html')
def faqs(request):
    return render(request , 'faqs.html')
def check_username(request, username):
    # Check if the username already exists in the database
    exists = Loginusername.objects.filter(loginusername=username).exists()
    return JsonResponse({'exists': exists})



def user_page(request, username):
#     # Data to populate the page

    # loginusernamevalue = Loginusername.objects.all()

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist

    try:
        pageurlsdata = URL.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pageurlsdata = None

    try:
        loginusernamevalue = Loginusername.objects.get(user=request.user)
    except Loginusername.DoesNotExist:
        loginusernamevalue = None
    adminpage = Adminpage.objects.all()
    # pageurlsdata = URL.objects.all()
    adminpageees = Urladmin.objects.all()
    adminpageone = Shopproduct.objects.all() 
    settingformurl = Settingform.objects.filter()

    context = {
        'loginusernamevalue':loginusernamevalue,
        'profile': profile,
        'adminpage':adminpage,
        'pageurlsdata': pageurlsdata,
        'adminpageees': adminpageees,
        'adminpageone': adminpageone,
        'settingformurl': settingformurl,
        'username': username,
        'data_from_backend': 'This data is provided by the backend and is not editable by the user.'
    }
    return render(request, 'user_page.html' , context)



def shop_plus(request):

    return render(request, 'shop_plus.html')