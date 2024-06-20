from django import forms
from pg_admin.models import Area,Category,Pg_details,Package,Facility,Gallary,Pg_owner,Pg_facility,User,Room_type,Pg_rooms,Feedback,Inquiry
from parsley.decorators import parsleyfy
@parsleyfy
class Areaform(forms.ModelForm):
    class Meta:
        model = Area
        fields = ["area_name","area_pin_code"]
@parsleyfy
class cateform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["cate_name","cate_desc"]
@parsleyfy
class room_typeform(forms.ModelForm):
    class Meta:
        model = Room_type
        fields = ["room_type_name","room_desc"]
@parsleyfy
class pg_detailsform(forms.ModelForm):
    pg_image = forms.FileField()
    class Meta:
        model = Pg_details
        fields = ["area_id","owner_id","cate_id","pg_name","pg_image","pg_address","pg_email","pg_contact","pg_desc"]
@parsleyfy
class packageform(forms.ModelForm):
    class Meta:
        model = Package
        fields = ["pg_id","room_type_id","pack_name","pack_desc","pack_price","pack_month"]
@parsleyfy
class facilityform(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ["faci_name","faci_desc"]
@parsleyfy
class gallaryform(forms.ModelForm):
    image = forms.FileField()
    class Meta:
        model = Gallary
        fields = ["pg_id","image"]
@parsleyfy
class pg_facilityform(forms.ModelForm):
    class Meta:
        model = Pg_facility
        fields = ["faci_id","pg_id"]
@parsleyfy
class pg_roomsform(forms.ModelForm):
    class Meta:
        model = Pg_rooms
        fields = ["pg_id","room_type_id","num_of_rooms"]
@parsleyfy
class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","contact_no","address"]
@parsleyfy
class signup_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","contact_no","email_id","date_of_birth","address","gender","password","is_admin","otp","otp_used","is_verify"]

@parsleyfy
class owner_signup_form(forms.ModelForm):
    class Meta:
        model = Pg_owner
        fields = ["owner_first_name","owner_last_name","owner_contact_no","owner_email_id","owner_address","owner_gender","owner_password"]
@parsleyfy
class inquiry_form(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["user_id","contact_no","email_id","u_message"]

class response_form(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["user_id","contact_no","email_id","u_message","response"]

class edit_form(forms.ModelForm):
    class Meta:
        model = Pg_owner
        fields = ["owner_first_name","owner_last_name","owner_contact_no","owner_email_id","owner_address","owner_gender","owner_password","otp","otp_used"]

class o_pg_detailsform(forms.ModelForm):
    pg_image = forms.FileField()
    class Meta:
        model = Pg_details
        fields = ["owner_id","area_id","cate_id","pg_name","pg_image","pg_address","pg_email","pg_contact","pg_desc"]