from django.shortcuts import render,redirect
from django.http import HttpResponse
from pg_admin.models import User,Pg_owner,Area,Category,Pg_details,Package,Facility,Booking,Gallary,Feedback,Pg_facility,Room_type,Pg_rooms,Wishlist,Inquiry
from pg_admin.forms import Areaform,cateform,pg_detailsform,packageform,facilityform,gallaryform,pg_facilityform,userform,room_typeform,pg_roomsform,inquiry_form,response_form
from pgfinder import settings
import os
import sys
from django.contrib import messages
import random
from django.core.mail import send_mail
from pg_admin.function import handle_uploaded_file
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count


# Create your views here.

def user_data(request):
    if 'a_id' in request.session:
        u = User.objects.all()
        f1 = Feedback.objects.all()
        return render(request,'User_data.html',{'user' :u,"feed":f1})
    else:
        return render(request,'login.html') 

def owner_data(request):
    if 'a_id' in request.session:
        o = Pg_owner.objects.all()
        f1 = Feedback.objects.all()
        return render(request,'pg_owner_data.html',{'pg_owner' : o,"feed":f1})
    else:
        return render(request,'login.html') 

def area_data(request):
    if 'a_id' in request.session:    
        a = Area.objects.all()
        f1 = Feedback.objects.all()
        return render(request,'area_data.html',{'area' : a,"feed":f1})
    else:
        return render(request,'login.html') 

def cate_date(request):
    if 'a_id' in request.session:
        c = Category.objects.all()
        f1 = Feedback.objects.all()
        return render(request,'category_data.html',{'category' : c,"feed":f1})
    else:
        return render(request,'login.html') 

def room_type_data(request):
    if 'a_id' in request.session:
        p = Room_type.objects.all()
        f1 = Feedback.objects.all()
        return render(request,'pg_type_data.html',{'pg_type':p,"feed":f1})
    else:
        return render(request,'login.html')     


def pg_details_data(request):
    if 'a_id' in request.session:
        pd = Pg_details.objects.all()
        f1 = Feedback.objects.all()
        return render(request,'pg_details_data.html',{'pg_details':pd,"feed":f1})
    else:
        return render(request,'login.html')    

def package_data(request):
    if 'a_id' in request.session:
        pack = Package.objects.all()
        f1 = Feedback.objects.all()
        return render(request,'package_data.html',{'package' : pack,"feed":f1})
    else:
        return render(request,'login.html') 

def facility_data(request):
    if 'a_id' in request.session:
        f = Facility.objects.all()
        f1 = Feedback.objects.all()
        return render(request,'facility_data.html',{'facility':f,"feed":f1})
    else:
        return render(request,'login.html')     

def booking_data(request):
    if 'a_id' in request.session:
        b = Booking.objects.all()
        f1 = Feedback.objects.all()
        return render(request,'booking_data.html',{'booking_details':b,"feed":f1})
    else:
        return render(request,'login.html') 

def gallary_data(request):
    if 'a_id' in request.session:
        g = Gallary.objects.all()
        f1 = Feedback.objects.all()
        return render(request,'gallary_data.html',{'gallary':g,"feed":f1})
    else:
        return render(request,'login.html')     

def feed_data(request):
    if 'a_id' in request.session:
        f = Feedback.objects.all()
        f1 = Feedback.objects.all()
        f2 = Feedback.objects.all().count()
        return render(request,'feedback_data.html',{'feedback':f,"feed":f1,"feed2":f2})
    else:
        return render(request,'login.html') 

def pg_faci_data(request):
    if 'a_id' in request.session:
        pf = Pg_facility.objects.all()
        f1 = Feedback.objects.all()
        return render(request,'pg_facility_data.html',{'pg_facility':pf,"feed":f1})
    else:
        return render(request,'login.html') 

def pg_room_data(request):
    if 'a_id' in request.session:
        pr = Pg_rooms.objects.all()
        return render(request,'pg_room_data.html',{'pg_room':pr})
    else:
        return render(request,'login.html') 

def destroy_area(request,id):
    if 'a_id' in request.session:
        a = Area.objects.get(area_id = id)
        a.delete()
        return redirect("/show_area/")
    else:
        return render(request,'login.html') 
    

def destroy_cate(request,id):
    if 'a_id' in request.session:
        c = Category.objects.get(cate_id = id)
        c.delete()
        return redirect("/show_cate/")
    else:
        return render(request,'login.html') 


def destroy_room_type(request,id):
    p = Room_type.objects.get(room_type_id = id)
    p.delete()
    return redirect("/show_type/")

def destroy_pg_details(request,id):
    d = Pg_details.objects.get(pg_id = id)
    d.delete()
    return redirect("/show_details/")

def destroy_package(request,id):
    dp = Package.objects.get(pack_id = id)
    dp.delete()
    return redirect("/show_package/")

def destroy_faci(request,id):
    df = Facility.objects.get(faci_id = id)
    df.delete()
    return redirect("/show_facility/")

def destroy_gallary(request,id):
    dg = Gallary.objects.get(gallary_id = id)
    dg.delete()
    return redirect("/show_gallary/")

def destroy_feedback(request,id):
    f = Feedback.objects.get(feed_id = id)
    f.delete()
    return redirect("/show_feed/")

def destroy_pg_faci(request,id):
    pf = Pg_facility.objects.get(pg_facility_id = id)
    pf.delete()
    return redirect("/show_pf/")

def destroy_pgrooms(request,id):
    pr = Pg_rooms.objects.get(pg_rooms_id = id)
    pr.delete()
    return redirect("/show_pgroom/")

def forms(request):
    return render(request,"form.html")

def insert_area(request):
    if request.method == "POST":
        form  = Areaform(request.POST)
        print("------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_area/')
            except:
                 print("------------------",sys.exc_info())
    else:
        form = Areaform()
    return render(request,'insert_area.html',{'form':form})

def insert_category(request):
    if request.method == "POST":
        form = cateform(request.POST)
        print("-------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_cate/')
            except:
                print("------------------------",sys.exc_info())
        
    else:
        form = cateform()
    return render(request,'insert_category.html',{'form':form})

def insert_roomtype(request):
    cate = Category.objects.all()
    if request.method == "POST":
        form = room_typeform(request.POST)
        print("-----------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_type/')
            except:
                print("---------------------",sys.exc_info())

    else:
        form = room_typeform()
    return render(request,'insert_pg_type.html',{'form':form,'ca':cate})

def insert_pgdetails(request):
    type =  Room_type.objects.all()
    area  = Area.objects.all()
    owner = Pg_owner.objects.all()
    cate = Category.objects.all()
    if request.method == "POST":
        form = pg_detailsform(request.POST,request.FILES)
        print("----------------------",form.errors)

        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['pg_image'])
                form.save()
                return redirect('/show_details/')
            except:
                print("----------------------",sys.exc_info())
    
    else:
        form = pg_detailsform()
    return render(request,'insert_pg_details.html',{'form':form,'te':type,'ar':area,'ow':owner,'ct':cate})

def insert_package(request):
    pg = Pg_details.objects.all()
    rt = Room_type.objects.all()
    if request.method == "POST":
        form = packageform(request.POST)
        print("--------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_package/')
            except:
                print("-------------------------",sys.exc_info())
    else:
        form = packageform()
    return render(request,'insert_package.html',{'form':form,'p':pg,'r':rt})

def insert_facility(request):
    if request.method == "POST":
        form = facilityform(request.POST)
        print("----------------------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_facility/')
            except:
                print("-------------------------",sys.exc_info())
    
    else:
        form = facilityform()
    return render(request,'insert_facility.html',{'form':form})

def insert_gallary(request):
    pg = Pg_details.objects.all()
    if request.method == "POST":
        form = gallaryform(request.POST,request.FILES)
        print("------------------------",form.errors)

        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['image'])
                form.save()
                return redirect('/show_gallary/')
            
            except:
                print("---------------------",sys.exc_info)

    else:
        form = gallaryform()
    return render(request,'insert_gallary.html',{'form':form,'p':pg})

def insert_pgfacility(request):
    fac = Facility.objects.all()
    pg = Pg_details.objects.all()
    if request.method == "POST":
        form = pg_facilityform(request.POST)
        print("--------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_pf/')
            except:
                print("-----------------------",sys.exc_info())
    else:
        form = pg_facilityform()
    return render(request,'insert_pg_facility.html',{'form':form,'facility':fac,'pg_details':pg})

def insert_pgrooms(request):
    rt = Room_type.objects.all()
    pg = Pg_details.objects.all()
    if request.method == "POST":
        form = pg_roomsform(request.POST)
        print("--------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_pgroom/')
            except:
                print("-----------------------",sys.exc_info())
    else:
        form = pg_roomsform()
    return render(request,'insert_pgrooms.html',{'form':form,'roomtype':rt,'pg_details':pg})

def update_area(request,id):
    if request.method == "POST":
        e = Area.objects.get(area_id=id)
        form = Areaform(request.POST,instance=e)
        print("-------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_area/')
            except:
                print("------------------------",sys.exc_info())
    
    else:
        e = Area.objects.get(area_id = id)
    return render(request,"update_area.html",{"area":e})


def update_cate(request,id):
    if request.method == "POST":
        e = Category.objects.get(cate_id = id)
        form = cateform(request.POST,instance=e)
        print("-------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_cate/')
            except:
                print("------------------------",sys.exc_info())
    
    else:
        e = Category.objects.get(cate_id = id)
    return render(request,"update_category.html",{"cate":e})

def update_room_type(request,id):
    cate = Category.objects.all()
    if request.method == "POST":
        e = Room_type.objects.get(room_type_id=id)
        form = room_typeform(request.POST,instance=e)
        print("-------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_type/')
            except:
                print("------------------------",sys.exc_info())
    
    else:
        e = Room_type.objects.get(room_type_id = id)
    return render(request,"update_pg_type.html",{"pg_type":e,"ct":cate})

def update_details(request,id):
      type = Room_type.objects.all()
      area  = Area.objects.all()
      owner = Pg_owner.objects.all()
      cate = Category.objects.all()
      if request.method == "POST":
        e = Pg_details.objects.get(pg_id=id)
        form = pg_detailsform(request.POST,instance=e)
        print("-------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_details/')
            except:
                print("------------------------",sys.exc_info())
    
      else:
        e = Pg_details.objects.get(pg_id = id)
      return render(request,"update_pg_details.html",{"pg":e,"te":type,"ar":area,"ow":owner,'ct':cate})

def update_package(request,id):
    pg = Pg_details.objects.all()
    rt = Room_type.objects.all()
    if request.method == "POST":
         e = Package.objects.get(pack_id = id)
         form = packageform(request.POST,instance=e)
         print("-------------------------",form.errors)

         if form.is_valid():
            try:
                form.save()
                return redirect('/show_package/')
            except:
                print("--------------------------",sys.exc_info())
    else:
        e = Package.objects.get(pack_id = id)
    return render(request,"update_package.html",{"pack":e,"p":pg,'r':rt})

def update_facility(request,id):
    if request.method == "POST":
        e = Facility.objects.get(faci_id = id)
        form = facilityform(request.POST,instance=e)
        print("--------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_facility/')
            except:
                print("--------------------------",sys.exc_info())
    else:
         e = Facility.objects.get(faci_id = id)
    return render(request,"update_facility.html",{"faci":e})

def update_gallary(request,id):
    pg = Pg_details.objects.all()
    if request.method == "POST":
        e = Gallary.objects.get(gallary_id = id)
        form = gallaryform(request.POST,instance=e)
        print("-------------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_gallary/')
            except:
                print("---------------------------",sys.exc_info())
    
    else:
        e = Gallary.objects.get(gallary_id = id)
    return render(request,"update_gallary.html",{'gallary':e,"p":pg})

def update_pg_facility(request,id):
    facility = Facility.objects.all()
    pg = Pg_details.objects.all()
    if request.method == "POST":
        e = Pg_facility.objects.get(pg_facility_id = id)
        form = pg_facilityform(request.POST,instance=e)
        print("-------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_pf/')
            except:
                print("----------------------",sys.exc_info())
    
    else:
        e = Pg_facility.objects.get(pg_facility_id = id)
    return render(request,"update_pg_facility.html",{"pf":e,"f":facility,"p":pg})

def update_pgrooms(request,id):
    nr = Room_type.objects.all()
    pg = Pg_details.objects.all()
    if request.method == "POST":
        e = Pg_rooms.objects.get(pg_rooms_id = id)
        form = pg_roomsform(request.POST,instance=e)
        print("-------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show_pgroom/')
            except:
                print("----------------------",sys.exc_info())
    
    else:
        e = Pg_rooms.objects.get(pg_rooms_id = id)
    return render(request,"update_pgrooms.html",{"pf":e,"num_rooms":nr,"pg_details":pg})

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = User.objects.filter(email_id=email,password=password,is_admin=1).count()
        print("----------------------------------",email,"-----------------",password)
        if val == 1:
            data = User.objects.filter(email_id = email,password = password)
            for items in data:
                request.session['a_id'] = items.user_id
                request.session['a_name'] = items.first_name
                request.session['a_email'] = items.email_id
                request.session['a_pass'] = items.password
            if request.POST.get("basic_checkbox_1"):
                print("+++++++++++++++++++++++++++++++++")
                response = redirect("/show/")
                response.set_cookie('cookie_aemail' , request.POST["email"], 3600 * 24 * 365 * 2)
                response.set_cookie('cookie_apass'  , request.POST["password"], 3600 * 24 * 365 * 2)
                return response
            return redirect('/show/')
        else:
            messages.error(request,"Invalid username or password")
            return redirect('/login/')
    else:
         if request.COOKIES.get("cookie_aemail"):
            print("+++++++++++++++++++++++--------------------------------------")
            return render(request, "login.html",{'a_email': request.COOKIES['cookie_aemail'], 'a_pass': request.COOKIES['cookie_apass']})
         else:
            return render(request,'login.html')
    
def logout(request):
    try:
        del request.session['a_id']
        del request.session['a_name']
        del request.session['a_email']
        del request.session['a_pass']
    except:
        pass

    return redirect("/login/")

def forgot_password(request):
    return render(request,'forgot_password.html')

def send_otp(request):
    otp1 = random.randint(10000,99999)
    e = request.POST["email"]
    request.session["temail"]=e

    obj = User.objects.filter(email_id=e).count()

    if obj == 1:
            val = User.objects.filter(email_id = e).update(otp=otp1 , otp_used=0)

            subject = 'OTP Verification'
            message = str(otp1)
            email_form = settings.EMAIL_HOST_USER
            recipient_list = [e, ]

            send_mail(subject, message, email_form,recipient_list)

            return render(request,'set_password.html')

def set_password(request):

    if request.method == "POST":

        t_otp = request.POST['otp']
        t_pass = request.POST['password']
        t_cpass = request.POST['new_password']

        if t_pass == t_cpass:
            e = request.session['temail']
            val = User.objects.filter(email_id = e, otp = t_otp, otp_used = 0).count()
        
            if val == 1:
                 User.objects.filter(email_id = e).update(otp_used=1,password = t_pass)
                 return redirect('/login/')
        
            else:
                messages.error(request,"Invalid OTP")
                return render(request,'set_password.html')
    
        else:
            messages.error(request,"New password and confirm Password does not match")
            return render(request,'set_password.html')
    else:
        return redirect('/for/')

def edit_profile(request,id):
    if 'a_id' in request.session:
        a_id = request.session['a_id']
        if request.method == "POST":
            e = User.objects.get(user_id=id)
            form = userform(request.POST,instance=e)
            print("-------------------------",form.errors)

            if form.is_valid():
                try:
                    form.save()
                    return redirect('/show/')
                except:
                    print("------------------------",sys.exc_info())
        
        else:
            e = User.objects.get(user_id= a_id)   
        return render(request,'edit_profile.html',{'ep':e})
    else:
        return render(request,'login.html') 
        
def dashboard(request):
    if 'a_id' in request.session:
        u = User.objects.all().count()
        p = Pg_details.objects.all().count()
        b = Booking.objects.all().count()
        b1 = Booking.objects.all()
        f1 = Feedback.objects.all()
        f2 = Feedback.objects.all().count()
        return render(request,"index-3.html",{"users":u,"pg":p,"book":b,"booking":b1,"feed":f1,"feed2":f2})
    else:
        return render(request,'login.html') 

def wishlist(request):
    wl =  Wishlist.objects.all()
    return render(request,"wishlist_data.html",{"wishlist":wl})

def inquiry_data(request):
    i = Inquiry.objects.all()
    return render(request,"inquiry_data.html",{"inq":i})

def update_response(request,id):
    if request.method == "POST":
        e = Inquiry.objects.get(inquiry_id = id)
        form = response_form(request.POST,instance=e)
        print("-------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/inquiry_data/')
            except:
                print("-----------",sys.exc_info())
    
    else:
          e = Inquiry.objects.get(inquiry_id = id)
    return render(request,"insert_response.html",{"inq":e})

from django.db import connection
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index-3.html', {"customers": 10})
    
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        #qs = Company.objects.all()
        cursor=connection.cursor()
        cursor.execute('''SELECT a.area_name as name, count(*) as total FROM pg_details p join area a
where p.area_id_id = a.area_id
GROUP by area_id_id;''')
        qs=cursor.fetchall()
        print("------------+++++++++++++++++++-----------------")
        labels = []
        default_items = []

        for item in qs:

            labels.append(item[0])
            default_items.append(item[1])

        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)

@csrf_exempt
def order_report1(request):
    s = Pg_details.objects.all()
    if request.method == "POST":
        key = request.POST.get("pgdetails")
        print("--- KEyword --------", key)
       
        sql = "SELECT * FROM booking b join package p join pg_details pd where b.pack_id_id = p.pack_id and p.pg_id_id = pd.pg_id and p.pg_id_id  =  %s"
        # sql = "SELECT * FROM order o join orderitem i join product p join subcategory s where o.o_id = i.o_id_id and i.product_id_id = p.product_id and p.subcate_id_id = s.subcate_id and p.subcate_id_id = %s"
        
        d = Pg_details.objects.raw(sql,[key])
        print("=====================================",d)
        return render(request, "report1.html", {"booking1": d})
    else:
        d = Booking.objects.all()
    return render(request,"order_report1.html",{"booking":d,"sub":s})


def accept_booking(request, id):
    ab = Booking.objects.filter(book_id=id).update(book_status=1)
    return redirect("/show_booking/")

def reject_booking(request, id):
    rb = Booking.objects.filter(book_id=id).update(book_status=2)
    return redirect("/show_booking/")

from django.utils.dateparse import parse_date
@csrf_exempt
def order_report2(request):

    if request.method == "POST":

        start = request.POST["sd"]
        end = request.POST["ed"]

        start = parse_date(start)
        end = parse_date(end)

        if start < end:
            print("----",start,"---------",end)
            d = Booking.objects.filter(book_date__range=[start,end])
            return render(request, "order_report2.html", {"book": d})
        else:
            d = Booking.objects.all()
            messages.error(request,"start date must be smaller than end date")
            return  render(request,"order_report2.html",{"book":d})
    else:
        d = Booking.objects.all()

    return render(request,"order_report2.html",{"book":d})

def order_report3(request):

    sql1="select  p.pg_id, p.pg_name as name, count(*) as total from pg_details as p JOIN feedback f where p.pg_id = f.pg_id_id"

    d = Pg_details.objects.raw(sql1)
    print('------------------------d',d)
    return render(request,"order_report3.html",{"pgc":d})

@csrf_exempt
def order_report4(request):
    s = Pg_details.objects.all()
    if request.method == "POST":
        key = request.POST.get("pgdetails")
        print("--- KEyword --------", key)
       
        sql = "SELECT * FROM pg_facility pf join  pg_details pd where pf.pg_id_id = pd.pg_id and pf.pg_id_id  =  %s"

        
        d = Pg_details.objects.raw(sql,[key])
        print("=====================================",d)
        return render(request, "report4.html", {"pgfaci": d})
    else:
        d = Pg_facility.objects.all()
    return render(request,"order_report4.html",{"pgfaci":d,"sub":s})

@csrf_exempt
def order_report5(request):
    s = Pg_details.objects.all()
    if request.method == "POST":
        key = request.POST.get("pgdetails")
        print("--- KEyword --------", key)
       
        sql = "SELECT * FROM pg_rooms pr join  pg_details pd where pr.pg_id_id = pd.pg_id and pr.pg_id_id  =  %s"

        
        d = Pg_details.objects.raw(sql,[key])
        print("=====================================",d)
        return render(request, "report5.html", {"pgroom": d})
    else:
        d = Pg_rooms.objects.all()
    return render(request,"order_report5.html",{"pgroom":d,"sub":s})




