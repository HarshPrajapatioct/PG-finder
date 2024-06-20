from django.shortcuts import render,redirect
from django.http import HttpResponse
from pg_admin.models import User,Pg_details,Feedback,Pg_facility,Facility,Pg_owner,Wishlist,Booking,Room_type,Area,Category,Booking,Package,Pg_rooms,Gallary,Inquiry
from django.contrib import messages
from django.core.mail import send_mail
from pgfinder import settings
import random
from pg_admin.forms import signup_form,pg_detailsform,inquiry_form
import sys
import datetime
import calendar
# Create your views here.
def home(request):
    availpg=[]
    pg = Pg_details.objects.all()
    pgd  = Pg_details.objects.all().count()
    area = Area.objects.all()
    pg = Pg_details.objects.all()
    for data in pg:
        print("-------------------------",data)
        rooms = Pg_rooms.objects.filter(pg_id=data.pg_id,num_of_rooms__gt = 0).count()
        print("--------Rooms---------",rooms)
        if rooms > 0:
            availpg.append(data)
    return render(request,"home.html",{"pgdetails":availpg,"pgd":pg,"ar":area,"pgc":pgd})

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = User.objects.filter(email_id=email,password=password,is_admin=0,is_verify=1).count()
        print(val)
        verify = User.objects.filter(email_id=email,password=password,is_admin=0,is_verify=0).count()
        print(verify)
        print("----------------------------------",email,"-----------------",password)
        if val == 1:
            data = User.objects.filter(email_id = email,password=password)
            for items in data:
                request.session['c_id'] = items.user_id
                request.session['c_name'] = items.first_name
                request.session['c_email'] = items.email_id
                request.session['c_pass'] = items.password
            if request.POST.get("defaultCheck1"):
                    print("+++++++++++++++++++++++++++qwedfytu78oik")
                    response = redirect("/client/index/")
                    response.set_cookie('cookie_cemail', request.POST["email"], 3600 * 24 * 365 * 2)
                    response.set_cookie('cookie_cpass', request.POST["password"], 3600 * 24 * 365 * 2)
                    return response
            return redirect('/client/index/')
        else:
            if verify >= 1:
                messages.error(request,"Verification is Pending")
                return redirect('/client/signin/')
            else:
                messages.error(request,"Invalid Username or Password")
                return redirect('/client/signin/')
    else:
         if request.COOKIES.get("cookie_cemail"):
            print("+++++++++++++++++++++++--------------------------------------")
            return render(request, "signin.html",{'c_email': request.COOKIES['cookie_cemail'], 'c_pass': request.COOKIES['cookie_cpass']})
         else:
            return render(request,'signin.html')
         
def client_logout(request):
    try:
        print('session data --------------',request.session['c_email'])
        del request.session['c_id']
        del request.session['c_email']
        del request.session['c_pass']

    except:
        pass

    return redirect("/client/signin/")	

def forgot_password(request):
     return render(request,'c_forgot_password.html')
from django.http import JsonResponse
def send_otp(request):
    otp1 = random.randint(10000,99999)
    e = request.POST["email"]
    request.session["c_email"]=e

    obj = User.objects.filter(email_id=e).count()

    if obj == 1:
        val = User.objects.filter(email_id = e).update(otp=otp1 , otp_used=0)
 
        subject = 'OTP Verification For Reset Password in Newo-Living Rent a PG'
        message = str(otp1)
        email_form = 'Newo Living Rent a PG'
        recipient_list = [e, ]
        try:
            send_mail(subject, message, email_form,recipient_list)
            return render(request,'c_set_password.html')
        except Exception as e:
            messages.error(request,"Internet Connection Required!!")
            return render(request,"c_forgot_password.html")

    if obj == 0:
        messages.error(request,"E mail id does not exist")
        return render(request,"c_forgot_password.html")

def set_password(request):

    if request.method == "POST":

        t_otp = request.POST['otp']
        t_pass = request.POST['password']
        t_cpass = request.POST['newpassword']

        if t_pass == t_cpass:
            e = request.session['c_email']
            val = User.objects.filter(email_id = e, otp = t_otp, otp_used = 0).count()
        
            if val == 1:
                 User.objects.filter(email_id = e).update(otp_used=1,password = t_pass)
                 return redirect('/client/signin/')
        
            else:
                messages.error(request,"Invalid OTP")
                return render(request,'c_set_password.html')
    
        else:
            messages.error(request,"New password and confirm Password does not match")
            return render(request,'c_set_password.html')
    else:
        return redirect('/client/forgot/')
    
def banner_search(request,id=0):

    availpg=[]

    pgd = Pg_details.objects.all().count()
    pack = Package.objects.all()
    faci = Facility.objects.all()
    if id == 0:
        pg = Pg_details.objects.all()
        for data in pg:
            print("-------------------------",data)
            rooms = Pg_rooms.objects.filter(pg_id=data.pg_id,num_of_rooms__gt = 0).count()
            print("--------Rooms---------",rooms)
            if rooms > 0:
                availpg.append(data)

    else:
        pg = Pg_details.objects.filter(cate_id = id)
        for data in pg:
            print("-------------------------",data)
            rooms = Pg_rooms.objects.filter(pg_id=data.pg_id,num_of_rooms__gt = 0).count()
            print("--------Rooms---------",rooms)
            if rooms > 0:
                availpg.append(data)

    return render(request,"property-banner-search.html",{"pgdetails":availpg,"pgc":pgd,"pack":pack,"faci":faci})

def banner_search1(request,id=0):
    availpg=[]
    pgd = Pg_details.objects.all().count()
    pack = Package.objects.all()
    faci = Facility.objects.all()
    if id == 0:
        pg = Pg_details.objects.all()
        for data in pg:
            print("-------------------------",data)
            rooms = Pg_rooms.objects.filter(pg_id=data.pg_id,num_of_rooms__gt = 0).count()
            print("--------Rooms---------",rooms)
            if rooms > 0:
                availpg.append(data)

    else:
        pg = Pg_details.objects.filter(area_id = id)
        for data in pg:
            print("-------------------------",data)
            rooms = Pg_rooms.objects.filter(pg_id=data.pg_id,num_of_rooms__gt = 0).count()
            print("--------Rooms---------",rooms)
            if rooms > 0:
                availpg.append(data)

    return render(request,"property-banner-search.html",{"pgdetails":availpg,"pgc":pgd,"pack":pack,"faci":faci})

def full_details(request,id):
    fd = Pg_details.objects.get(pg_id = id)
    feed = Feedback.objects.filter(pg_id = id)
    feed_count = Feedback.objects.filter(pg_id = id).count()
    pg_faci = Pg_facility.objects.filter(pg_id= id)
    pgd = Pg_details.objects.all()
    package = Package.objects.filter(pg_id = id)
    gall = Gallary.objects.filter(pg_id = id)
    pgr = Pg_rooms.objects.filter(pg_id = id)
    # categ = Pg_details.objects.get(cate_id = id)
    return render(request,"property-single-v1.html",{"full":fd,"feedback":feed,"feed_c":feed_count,"pgf":pg_faci,"pg":pgd,"pack":package,"gallery":gall,"pgr":pgr})

def signup(request):
    u = User.objects.all()
    if request.method == "POST":

        e=request.POST['email_id']
        obj = User.objects.filter(email_id=e).count()
        if obj == 0:

            form  = signup_form(request.POST)
            print("------------------------",form.errors)
            if form.is_valid():
                try:
                    form.save()
                    otp1 = random.randint(10000,99999)
                    
                    e=request.POST['email_id']
                    request.session["temail"]=e

                    obj = User.objects.filter(email_id=e).count()

                    if obj == 1:
                        val = User.objects.filter(email_id = e).update(otp=otp1 , otp_used=0,is_admin = 0,is_verify=0)

                        subject = 'OTP Verification For Registration in Newo-Living Rent a PG'
                        message = str(otp1)
                        email_form = settings.EMAIL_HOST_USER
                        recipient_list = [e, ]
                        send_mail(subject, message, email_form,recipient_list)
                        return redirect('/client/otp_verify/')
                        
                except:
                    print("-----------------",sys.exc_info())
        else:
              messages.error(request,"Email id already exist")
              return render(request,"signup.html")
        # elif User.objects.filter(email_id=form.).exists():
        #     # user = User.objects.filter(email_id = e)
        #     # user.exists()
        #     messages.error(request,"Email id already exist")
        #     return render(request,"signup.html")
  
    else:
        form = signup_form()  
    return render(request,"signup.html")

    # return render(request,"signup.html")

def otp_verification(request):
    if request.method == "POST":
        t_otp = request.POST['otp']
        e = request.session['temail']
        val = User.objects.filter(email_id = e, otp = t_otp, otp_used = 0).count()

        if val == 1:
            User.objects.filter(email_id = e).update(otp_used=1,is_verify=1)
            return redirect('/client/signin/')
        
        else:
            messages.error(request,"Invalid OTP ")
            return render(request,'otp_verify.html')
    return render(request,"otp_verify.html")


def edit_profile(request):
    c_id = request.session['c_id']
    if request.method == "POST":
        
        e = User.objects.get(user_id=c_id)
        form = signup_form(request.POST,instance=e)
        print("-------------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/client/index/')
            except:
                print("------------------------",sys.exc_info())
    
    else:
        e = User.objects.get(user_id= c_id)   
    return render(request,"c_edit_profile.html",{'ep':e})

def wishlist(request):
    wl =  Wishlist.objects.all()
    return render(request,"wishlist.html",{"wishlist":wl})

def add_to_wishlist(request):
 if 'c_id' in request.session:
    if request.method == "POST":
        try:
            pg_id = request.POST["pg_id"]
            u_id = request.session["c_id"]
            w = Wishlist(pg_id_id = pg_id , user_id_id = u_id)
            w.save()
            print(pg_id)
            return redirect('/client/wishlist/')
        except:
            print("-------------",sys.exc_info())
    else:
        return render(request,"wishlist.html")
 else:
     return render(request,"signin.html")
    
def delete_form_wishlist(request,id):
    wl = Wishlist.objects.get(wishlist_id = id)
    wl.delete()
    return redirect('/client/wishlist/')

def booking(request):
    b = Booking.objects.all()
    return render(request,"c_booking.html",{"book":b})

def submitpg(request):
    type =  Room_type.objects.all()
    area  = Area.objects.all()
    owner = Pg_owner.objects.all()
    if request.method == "POST":
        form = pg_detailsform(request.POST)
        print("----------------------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/client/wishlist/')
            except:
                print("----------------------",sys.exc_info())
    
    else:
        form = pg_detailsform()
    return render(request,"submit-pg.html",{'form':form,'te':type,'ar':area,'ow':owner})

def pg_list(request):
    pl = Pg_details.objects.all()
    return render(request,"pg_list.html",{"pg":pl})

def insert_feedback(request):
    try:
        d = datetime.date.today()
        pg_id = request.POST["pg_id"]
        des = request.POST["desc"]
        u_id = request.session["c_id"]

        f = Feedback(feed_date = d,feed_desc = des,pg_id_id  = pg_id,user_id_id = u_id)
        f.save()
        return redirect("/client/index/")
    except:
        print("------",sys.exc_info())
    return render(request,"property-single-v1.html")

def book_pg(request,id=0):
    if 'c_id' in request.session:
        package = Package.objects.filter(pg_id = id)
        pg_room = Pg_rooms.objects.filter(pg_id = id,num_of_rooms__gt = 0)
        pg_rooms = Pg_rooms.objects.filter(pg_id = id)
        if request.method == "POST":
            try:
                pg_room_id = request.POST.get("pg_rooms_id")
                pgid = request.POST.get("pgid")
                print(pgid)
                room_id = Pg_rooms.objects.filter(room_type_id_id = pg_room_id).get(pg_id_id = pgid).pg_rooms_id
                print("+++++++++++++++++++++++++++++",room_id)
                pack_id = request.POST.get("pack_id")
                book_desc = request.POST.get("book_desc")
                d = datetime.date.today()
                u_id = request.session["c_id"]
                p = Package.objects.get(pack_id = pack_id)
                print("+++++++++++++++++++ before bookig -===================")
                print(pack_id)
                print(pg_room_id)
                # b = Booking(pg_rooms_id_id = room_id,pack_id_id = pack_id,book_desc = book_desc,book_date = d,end_date = add_months(d,p.pack_month),payment_status = 0,book_status = 0,user_id_id = u_id)
                b = Booking(pg_rooms_id_id=room_id, pack_id_id=pack_id, book_desc=book_desc, book_date=d, end_date=add_months(d, p.pack_month), payment_status=0, book_status=0, user_id_id=u_id)

                b.save()
                print("++++++++++++++++++after booking-----------------------------")
              
                return redirect('/client/checkout/')
            except:
                print("-------------",sys.exc_info())
        else:
            pass
        return render(request,"book_pg.html",{"pack":package,"pr":pg_room,"prg":pg_rooms,"pgid":id})
    else:
        return render(request,"signin.html")
    
def client_Checkout(request):
    if 'c_id' in request.session:
        id = request.session['c_id']
        user = User.objects.get(user_id=id)
        a = Booking.objects.filter(user_id=id)
        # print(a.pack_id)
        # total = 0
        # total = a.pack_id.pack_price + total//only one user amount 
        total = 0
        for data in a:
            total = data.pack_id.pack_price + total
        ship = 50
        gt = total + ship
        return render(request, "booking_pgr.html",
                      {'user': user, 'cart': a, 'sub': total,  'total':gt})
    else:
        return render(request,"signin.html")

def load_menu(request):
    c = Category.objects.all()
    print("---------------------")
    return render(request,"test.html",{"cat":c})

def load_area(request):
    a = Area.objects.all()
    return render(request,"test1.html",{"area":a})

def insert_inquiry(request):
    if 'c_id' in request.session:
        if request.method == "POST":
                try:
                    u_id = request.session["c_id"]
                    c_no = request.POST["contact_no"]
                    email_id = request.POST["email_id"]
                    u_message = request.POST["u_message"]
                    form = Inquiry(user_id_id = u_id, contact_no = c_no ,email_id = email_id,u_message= u_message)
                    form.save()
                    return redirect('/client/index/')
                except:
                    print("-----------",sys.exc_info())
        
        else:
            form = inquiry_form()
        return render(request,"property-single-v1.html")
    else:
       return render(request,"signin.html") 

def faq(request):
    inq = Inquiry.objects.all()
    return render(request,"faq.html",{"inquiry":inq})

def sort_data(request):

    sid=request.GET.get('sort')
    print("---- SORT 000000000000",sid)

    if sid == '1':
        p = Package.objects.filter(pack_price__range=["0","10000"])
        print('sid1----------------------------',p)
    elif sid == '2':
        p = Package.objects.filter(pack_price__range=["10000","30000"])
    elif sid == '3':
        p = Package.objects.filter(pack_price__range=["30000","50000"])
        print('----------------------------------',p)
    else:
        p = Package.objects.filter(pack_price__range=["50000","60000"])

    print("---- SORT 000000000000",sid)

    return render(request,"sort.html",{"package":p})

def search(request):
    if request.method == "GET":
        pg_name=request.GET.get('pg_name')
        print('--------------------------',pg_name)
        if pg_name:
            request.session['search'] = pg_name
            obj=Pg_details.objects.filter(pg_name__icontains=pg_name)
            print('0000000000000000000000',obj)
            return render(request, 'property-banner-search.html', {'pgdetails': obj})
        else:
            return redirect('/client/banner/')
        
def add_months(book_date, pack_month):
    months_count = book_date.month + pack_month

    # Calculate the year
    year = book_date.year + int(months_count / 12)

    # Calculate the month
    month = (months_count % 12)
    if month == 0:
        month = 12

    # Calculate the day
    day = book_date.day
    last_day_of_month = calendar.monthrange(year, month)[1]
    if day > last_day_of_month:
        day = last_day_of_month

    new_date = datetime.date(year, month, day)
    return new_date

def contact(request):
    return render(request,"contact.html")

def load_package(request):
    print('iddddddddddddddddddddddd')
    
    id = request.GET['pack']
    pgid = request.GET['pgid']
    print("------------- Roomtype id ------------",id)
    print("---------------------------",pgid)
    p = Package.objects.filter(room_type_id_id = id).filter(pg_id_id = pgid )
    print('-------------------------',p)
    return render(request,"test3.html",{"pack":p})

# def send_main_on_booking_end(request):
#    d = datetime.date.today()
#    b = Booking.objects.filter(end_date = d)
#    cid = request.session['c_id']
#    bg = booking.objects.filter(user_id = cid).count()
#    if bg == 1:
#        print("---------------------------")
#        return HttpResponse("Last Date")
#    else:
#        return HttpResponse("multiple booking id")
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def OrderSuccess(request):
    place_order_online(request)
    return render(request, "client_Order_bucess.html")

def place_order_online(request,id):
    if request.session.has_key('c_id'):
        uid = request.session['c_id']
        b = Booking.objects.filter(user_id_id=uid)
        amt = 0
        # for val in b:
        #     amt = amt + val.pack_id.pack_price
            # pd_id = val.pg_rooms_id_id
            # book_date = val.book_date
            # end_date = val.end_date
            # pack_id = val.pack_id_id
            # bs = val.book_status
        # amt = amt + 100
        # date1 = date.today().strftime("%Y-%m-%d")
        # o = Booking(user_id_id=uid,payment_status='2',pg_rooms_id_id =pd_id,book_date=book_date,end_date=end_date,pack_id_id = pack_id,book_status = bs)
        # # o.save()
        # o = Booking.objects.filter(book_id = uid)
        # o.update(payment_status = '2')
        # o = Booking.objects.update(payment_status = '2')
        # o.save()
        # c3 = Booking.objects.latest('book_id').count()
        ab = Booking.objects.filter(book_id=id).update(payment_status=1)
        # ab = Booking.objects.filter(book_id=id).update.(no_of_rooms-=1)
        # pgrooms = Booking.objects.get(ab)
        # ab1 = Booking.objects.get(book_id=id,payment_status=1)
        # ab1.pg_rooms_id.num_of_rooms = ab1.pg_rooms_id.num_of_rooms - 1
        # print("-------------------------------======================",ab1,ab1.pg_rooms_id.num_of_rooms )
        
        # pgroom = Pg_rooms.objects.get(pg_rooms_id=ab1.pg_rooms_id.num_of_rooms)
        ab1 = Booking.objects.get(book_id=id, payment_status=1)
        pgroom = Pg_rooms.objects.get(pg_rooms_id=ab1.pg_rooms_id_id)
        pgroom.num_of_rooms -= 1
        pgroom.save()
        

        # ab1.save()
        c = Booking.objects.filter(user_id_id=uid)
        c1 = Booking.objects.filter(user_id_id=uid).count()
        if c1 >= 1:
            e = request.session['c_email']
            obj = User.objects.filter(email_id=e).count()
            val = User.objects.get(email_id=e)
            if obj == 1:
                ord1 = Booking.objects.get(book_id=id)
                
                
                print("--------------------------------------------++++++++",ord1)
                subject = 'Booking Conformation'
                message = f'Dear {val.first_name} \n\n\t ' \
                          f'Your Your Booking request has been received. ' \
                          f'Your Booking details are as follows:'
                message += f'\n---------------------------------------------------------------------'
            #  for date in ord1:
                print("------------------------------",ord1)
                message += f'\n  PG name is {ord1.pack_id.pg_id.pg_name}'
                message += f'\n  Pack name is {ord1.pack_id.pack_name}'
                message += f'\n  Package amount is {ord1.pack_id.pack_price}'
                message += f'\n----------------------------------------------------------------------'
                # for data in ord1:
                #     print("---------------------------------", data)
                #     message += f'\n {data.Reservation_ID} ,{data.Train_ID.Train_Name}'
                message += f'\n----------------------------------------------------------------------'
                message += f'\n  Total \t\t\t {ord1.pack_id.pack_price}'
                message += f'\n----------------------------------------------------------------------'
                message += f'\n\n Thank uou,\n Regards Newo Living Rent a PG'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [e, ]
                send_mail(subject, message, email_from, recipient_list)
                return redirect('/client/booking/')
        # else:
        #     # messages.error(request, "You don't have any product in your Cart!")
        #     # return render(request, "Client_checkout.html")
            
        # # return redirect("/client/index/")   
    return render(request,'c_booking.html')   