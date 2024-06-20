"""
URL configuration for pgfinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from  pg_admin import views
from django.urls import include, re_path
from pg_admin.views import HomeView, ChartData


urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/',views.user_data),
    path('show_owner/',views.owner_data),
    path('show_area/',views.area_data),
    path('show_cate/',views.cate_date),
    path('show_type/',views.room_type_data),
    path('show_details/',views.pg_details_data),
    path('show_package/',views.package_data),
    path('show_facility/',views.facility_data),
    path('show_booking/',views.booking_data),
    path('show_gallary/',views.gallary_data),
    path('show_feed/',views.feed_data),
    path('show_pf/',views.pg_faci_data),
    path('show_pgroom/',views.pg_room_data),
    path('del_area/<int:id>',views.destroy_area),
    path('del_cate/<int:id>',views.destroy_cate),
    path('del_pg_type/<int:id>',views.destroy_room_type),
    path('del_pg_details/<int:id>',views.destroy_pg_details),
    path('del_pack/<int:id>',views.destroy_package),
    path('del_faci/<int:id>',views.destroy_faci),
    path('del_gallary/<int:id>',views.destroy_gallary),
    path('del_feed/<int:id>',views.destroy_feedback),
    path('del_pf/<int:id>',views.destroy_pg_faci),
    path('del_pr/<int:id>',views.destroy_pgrooms),
    path('sf/',views.forms),
    path('in_area/',views.insert_area),
    path('in_category/',views.insert_category),
    path('in_pgtype/',views.insert_roomtype),
    path('in_pgdetails/',views.insert_pgdetails),
    path('in_package/',views.insert_package),
    path('in_facility/',views.insert_facility),
    path('in_gallary/',views.insert_gallary),
    path('in_pf/',views.insert_pgfacility),
    path('in_pr/',views.insert_pgrooms),
    path('up_area/<int:id>',views.update_area),
    path('up_cate/<int:id>',views.update_cate),
    path('up_type/<int:id>',views.update_room_type),
    path('up_details/<int:id>',views.update_details),
    path('up_package/<int:id>',views.update_package),
    path('up_facility/<int:id>',views.update_facility),
    path('up_gallary/<int:id>',views.update_gallary),
    path('up_pf/<int:id>',views.update_pg_facility),
    path('update_pgrooms/<int:id>',views.update_pgrooms),
    path('login/',views.login),
    path('logout/',views.logout),
    path('for/',views.forgot_password),
    path('send_otp/',views.send_otp),
    path('set_pass/',views.set_password),
    path('edit_profile/<int:id>',views.edit_profile),
    path('dash/',views.dashboard),
    path('wishlist/',views.wishlist),
    path('inquiry_data/',views.inquiry_data),
    path('in_response/<int:id>',views.update_response),
    re_path(r'home', HomeView.as_view(), name='home'),
    re_path(r'^api/chart/data/$', ChartData.as_view(),name="api-data"),
    path('order_report1/',views.order_report1),
    path('accepted/<int:id>',views.accept_booking),
    path('rejected/<int:id>',views.reject_booking),
    path('order_report2/',views.order_report2),
    path('order_report3/',views.order_report3),
    path('order_report4/',views.order_report4),
    path('order_report5/',views.order_report5),


    path('client/',include('client.client_urls')),
    path('owner/',include('owner.owner_urls')),
    


]
