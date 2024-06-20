from django.shortcuts import render,redirect
from django.http import HttpResponse
from pg_admin.models import User,Pg_details,Feedback,Pg_facility,Pg_owner,Facility,Wishlist,Booking,Room_type,Area,Category,Booking,Package,Pg_rooms,Gallary
from django.contrib import messages
from django.core.mail import send_mail
from pgfinder import settings
import random
from pg_admin.forms import signup_form,pg_detailsform,owner_signup_form,edit_form,o_pg_detailsform
import sys
import datetime

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form  = owner_signup_form(request.POST)
        print("------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/owner/dashboard/')
            except:
                 print("------------------",sys.exc_info())
    else:
        form = signup_form()
    return render(request,"owner_signup.html")

def dashboard(request):
    return render(request,"dashboard.html")

def category(request):
    if 'o_id' in request.session:
        c = Category.objects.all()
        return render(request,"cate_data.html",{"c":c})
    else:
          return render(request,'owner_signin.html')
    
def area(request):
     if 'o_id' in request.session:
        a = Area.objects.all()
        return render(request,"areaa_data.html",{"a":a})
     else:
          return render(request,'owner_signin.html')

def roomtype(request):
    if 'o_id' in request.session:
        r = Room_type.objects.all()
        return render(request,"roomtype_data.html",{"r":r})
    else:
          return render(request,'owner_signin.html')
    

def facility(request):
    if 'o_id' in request.session:
        f = Facility.objects.all()
        return render(request,"faci_data.html",{"f":f})
    else:
        return render(request,'owner_signin.html')

def owner_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = Pg_owner.objects.filter(owner_email_id=email,owner_password=password).count()
        # verify = Pg_owner.objects.filter(is_verify=1).count()
        print("----------------------------------",email,"-----------------",password)
        if val == 1:
            data = Pg_owner.objects.filter(owner_email_id = email,owner_password=password)
            for items in data:
                request.session['o_id'] = items.owner_id
                request.session['o_name'] = items.owner_first_name
                request.session['o_email'] = items.owner_email_id
                request.session['o_pass'] = items.owner_password
            if request.POST.get("defaultCheck1"):
                    print("+++++++++++++++++++++++++++qwedfytu78oik")
                    response = redirect("/owner/owner_cate/")
                    response.set_cookie('cookie_oemail', request.POST["email"], 3600 * 24 * 365 * 2)
                    response.set_cookie('cookie_opass', request.POST["password"], 3600 * 24 * 365 * 2)
                    return response
            return redirect('/owner/owner_cate/')
        # elif verify == 0:
        #     messages.error(request,"Verification is pending")
        #     return redirect('/owner/owner_signin/')
        else:
            messages.error(request,"Invalid username or password")
            return redirect('/owner/owner_signin/')
    else:
         if request.COOKIES.get("cookie_oemail"):
            print("+++++++++++++++++++++++--------------------------------------")
            return render(request, "owner_signin.html",{'o_email': request.COOKIES['cookie_oemail'], 'o_pass': request.COOKIES['cookie_opass']})
         else:
            return render(request,'owner_signin.html')
         
def owner_logout(request):
    try:
        print('session data --------------',request.session['o_email'])
        del request.session['o_id']
        del request.session['o_email']
        del request.session['o_pass']

    except:
        pass

    return redirect("/owner/owner_signin/")	

def forgot_password(request):
     return render(request,'o_forgot_password.html')


def send_otp(request):
    otp1 = random.randint(10000,99999)
    e = request.POST["email"]
    request.session["temail"]=e
    obj = Pg_owner.objects.filter(owner_email_id=e).count()

    if obj == 1:
        val = Pg_owner.objects.filter(owner_email_id = e).update(otp=otp1 , otp_used=0)

        subject = 'OTP Verification For Reset Password in Newo-Living Rent a PG'
        message = str(otp1)
        email_form = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_form,recipient_list)

        return render(request,'o_set_password.html')
    else:
        messages.error(request,"E-Mail ID does Not exist")
        return render(request,'o_forgot_password.html')
    
def set_password(request):

    if request.method == "POST":

        t_otp = request.POST['otp']
        t_pass = request.POST['password']
        t_cpass = request.POST['newpassword']

        if t_pass == t_cpass:
            e = request.session['temail']
            val = Pg_owner.objects.filter(owner_email_id = e, otp = t_otp, otp_used = 0).count()
        
            if val == 1:
                 Pg_owner.objects.filter(owner_email_id = e).update(otp_used=1,owner_password = t_pass)
                 return redirect('/owner/owner_signin/')
        
            else:
                messages.error(request,"Invalid OTP")
                return render(request,'o_set_password.html')
    
        else:
            messages.error(request,"New password and confirm Password does not match")
            return render(request,'o_set_password.html')
    else:
        return redirect('/owner/owner_forgot/')
    
def edit_profile(request):
    o_id = request.session['o_id']
    if request.method == "POST":
        
        e = Pg_owner.objects.get(owner_id=o_id)
        print(e)
        form = edit_form(request.POST,instance=e)
        print("-------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/owner/dashboard/')
            except:
                print("------------------------",sys.exc_info())
    
    else:
        e = Pg_owner.objects.get(owner_id= o_id)   
    return render(request,"o_edit_profile.html",{'ep':e})

def pgdetails(request):
    if 'o_id' in request.session:
        o_id = request.session['o_id']
        pd = Pg_details.objects.filter(owner_id = o_id)
        return render(request,"pgdetails_data.html",{"pd":pd})
    else:
        return render(request,'owner_signin.html')
def pgrooms(request,id):
    pr = Pg_rooms.objects.filter(pg_id = id)
    return render(request,"pgrooms.html",{"pr":pr})

def pgfacility(request,id):
    pf = Pg_facility.objects.filter(pg_id = id)
    return render(request,"pgfacility.html",{"pf":pf})

def gallary(request,id):
    g = Gallary.objects.filter(pg_id = id)
    return render(request,"gallary.html",{"g":g})

def package(request,id):
    p = Package.objects.filter(pg_id = id)
    return render(request,"package.html",{"p":p})
import datetime
def booking(request,id):
    b = Booking.objects.select_related('pack_id').select_related('pack_id__pg_id').filter(pack_id__pg_id=id)
    d=datetime.date.today()
    return render(request,"booking.html",{"b":b,"d":d})


def accept_bookingo(request,id):
    ab = Booking.objects.filter(book_id=id).update(book_status=1)
    return redirect("/owner/pg_details/")

def reject_bookingo(request,id):
    rb = Booking.objects.filter(book_id=id).update(book_status=2)
    return redirect("/owner/pg_details/")
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def order_report1(request):
    if 'o_id' in request.session:
        o_id = request.session['o_id']
        s = Pg_details.objects.filter(owner_id = o_id)
        if request.method == "POST":
            key = request.POST.get("pgdetails")
            print("--- KEyword --------", key)
        
            sql = "SELECT * FROM booking b join package p join pg_details pd where b.pack_id_id = p.pack_id and p.pg_id_id = pd.pg_id and p.pg_id_id  =  %s"
            # sql = "SELECT * FROM order o join orderitem i join product p join subcategory s where o.o_id = i.o_id_id and i.product_id_id = p.product_id and p.subcate_id_id = s.subcate_id and p.subcate_id_id = %s"
            
            d = Pg_details.objects.raw(sql,[key])
            print("=====================================",d)
            return render(request, "oreport1.html", {"booking1": d})
        else:
            d = Booking.objects.all()
        return render(request,"owner_report1.html",{"booking":d,"sub":s})
    else:
        return render(request,'owner_signin.html')
from owner.function import handle_uploaded_file
def submitpg(request):
    if 'o_id' in request.session:
        cate = Category.objects.all()
        type =  Room_type.objects.all()
        area  = Area.objects.all()
        o_id = request.session['o_id']
    
        if request.method == "POST":
            print('inside post--------------------------------')
            e = Pg_owner.objects.get(owner_id = o_id)
            print(e)
            form = o_pg_detailsform(request.POST,request.FILES)
            print("----------------------",form.errors)
        
            if form.is_valid():
                try:
                    print("------- Before file Upload----------")
                    handle_uploaded_file(request.FILES['pg_image'])
                    form.save()
                    print("")
                    return redirect('/owner/pg_details/')
                except:
                    print("----------------------",sys.exc_info())
        else:
            form = pg_detailsform()
        return render(request,"submit_pg.html",{'form':form,'te':type,'ar':area,"cate":cate,"o":o_id})
    else:
        return render(request,'owner_signin.html')
    
def send_mail_on_pack_end(request,id):
    b = Booking.objects.get(book_id=id)
    b1 = Booking.objects.filter(book_id=id).count()
    if b1 == 1: 
        #e = User.objects.get(email_id = b)   
        e=b.user_id.email_id
        subject = 'Alert For Booking ending'
        message = f'\n  Your Booking on  \t\t\t {b.pack_id_id.pg_id_id.pg_name} Will be End today '
        message += f'\n----------------------------------------------------------------------'
        message += f'\n\n Thank uou,\n Regards Newo Living Rent a PG'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e,] 
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/owner/pg_details/')
    else:
        return HttpResponse("No booking found for the specified user.")

    
    
