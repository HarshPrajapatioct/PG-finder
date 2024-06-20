from django.contrib import admin
from django.urls import path
from owner import owner_views
urlpatterns = [
    path('signup/',owner_views.sign_up),
    path('dashboard/',owner_views.dashboard),
    path('owner_cate/',owner_views.category),
    path('owner_area/',owner_views.area),
    path('owner_room/',owner_views.roomtype),
    path('owner_facility/',owner_views.facility),
    path('owner_signin/',owner_views.owner_login),
    path('owner_signout/',owner_views.owner_logout),
    path('owner_forgot/',owner_views.forgot_password),
    path('owner_send_otp/',owner_views.send_otp),
    path('owner_set_password/',owner_views.set_password),
    path('edit_profile/',owner_views.edit_profile),
    path('pg_details/',owner_views.pgdetails),
    path('pgrooms/<int:id>',owner_views.pgrooms),
    path('pgfacility/<int:id>',owner_views.pgfacility),
    path('gallary/<int:id>',owner_views.gallary),
    path('package/<int:id>',owner_views.package),
    path('booking/<int:id>',owner_views.booking),
    path('acceptedo/<int:id>',owner_views.accept_bookingo),
    path('rejectedo/<int:id>',owner_views.reject_bookingo),
    path('owner_report1/',owner_views.order_report1),
    path('submitpg/',owner_views.submitpg),
    path('send_mail/<int:id>',owner_views.send_mail_on_pack_end),
]
