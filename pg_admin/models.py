from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=13)
    email_id = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=1)
    password = models.CharField(max_length=15)
    is_admin = models.IntegerField()
    otp = models.CharField(max_length=6)
    otp_used = models.IntegerField()
    is_verify = models.IntegerField()

    class Meta:
        db_table = 'user'

class Pg_owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    owner_first_name = models.CharField(max_length=30)
    owner_last_name = models.CharField(max_length=30)
    owner_contact_no = models.CharField(max_length=13)
    owner_email_id = models.EmailField(unique=True)
    owner_address = models.CharField(max_length=200)
    owner_gender = models.CharField(max_length=1)
    owner_password = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    otp_used = models.IntegerField()

    class Meta:
        db_table = 'pg_owner'

class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=20)
    area_pin_code = models.CharField(max_length=6)

    class Meta:
        db_table = 'area'

class Category(models.Model):
    cate_id = models.AutoField(primary_key=True)
    cate_name = models.CharField(max_length=20)
    cate_desc = models.CharField(max_length=200)

    class Meta:
        db_table = 'category'

class Room_type(models.Model):
    room_type_id = models.AutoField(primary_key=True)
    room_type_name = models.CharField(max_length=20)
    room_desc = models.CharField(max_length=200)

    class Meta:
        db_table = 'room_type'

class Pg_details(models.Model):
    pg_id = models.AutoField(primary_key=True)
    area_id = models.ForeignKey(Area,on_delete=models.CASCADE)
    owner_id = models.ForeignKey(Pg_owner,on_delete=models.CASCADE)
    cate_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    pg_name = models.CharField(max_length=20)
    pg_image = models.CharField(max_length=40)
    pg_address = models.CharField(max_length=100)
    pg_email = models.EmailField(unique=True)
    pg_contact = models.CharField(max_length=13)
    pg_desc = models.CharField(max_length=200)

    class Meta:
        db_table = 'pg_details'

class Package(models.Model):
    pack_id = models.AutoField(primary_key=True)
    pg_id = models.ForeignKey(Pg_details,on_delete=models.CASCADE)
    room_type_id = models.ForeignKey(Room_type,on_delete=models.CASCADE)
    pack_name = models.CharField(max_length=20)
    pack_desc = models.CharField(max_length=200)
    pack_price = models.IntegerField()
    pack_month = models.IntegerField()

    class Meta:
        db_table = 'package'
    
class Facility(models.Model):
    faci_id = models.AutoField(primary_key=True)
    faci_name = models.CharField(max_length=20)
    faci_desc = models.CharField(max_length=200)

    class Meta:
        db_table = 'facility'

class Gallary(models.Model):
    gallary_id = models.AutoField(primary_key=True)
    pg_id = models.ForeignKey(Pg_details,on_delete=models.CASCADE)
    image = models.CharField(max_length=40)

    class Meta:
        db_table = 'gallary'

class Feedback(models.Model):
    feed_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    pg_id = models.ForeignKey(Pg_details,on_delete=models.CASCADE)
    feed_desc = models.CharField(max_length=200)
    feed_date = models.DateField()

    class Meta:
        db_table = 'feedback'

class Pg_facility(models.Model):
    pg_facility_id = models.AutoField(primary_key=True)
    faci_id = models.ForeignKey(Facility,on_delete=models.CASCADE)
    pg_id  = models.ForeignKey(Pg_details,on_delete=models.CASCADE)

    class Meta:
        db_table = 'pg_facility'

class Pg_rooms(models.Model):
    pg_rooms_id = models.AutoField(primary_key=True)
    pg_id = models.ForeignKey(Pg_details,on_delete=models.CASCADE)
    room_type_id = models.ForeignKey(Room_type,on_delete=models.CASCADE)
    num_of_rooms =  models.IntegerField()

    class Meta:
        db_table = 'pg_rooms'

class Booking(models.Model):
    book_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    pg_rooms_id = models.ForeignKey(Pg_rooms,on_delete=models.CASCADE)
    book_date = models.DateField()
    end_date = models.DateField()
    book_desc = models.CharField(max_length=200)
    pack_id = models.ForeignKey(Package,on_delete=models.CASCADE)
    payment_status = models.IntegerField()
    book_status = models.IntegerField()

    class Meta:
        db_table = 'booking'

class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    pg_id = models.ForeignKey(Pg_details,on_delete=models.CASCADE)

    class Meta:
        db_table = 'wishlist'

class Inquiry(models.Model):
    inquiry_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=13)
    email_id = models.EmailField(unique=True)
    u_message = models.CharField(max_length = 100)
    response = models.CharField(max_length=100)

    class Meta:
        db_table = 'inquiry'
