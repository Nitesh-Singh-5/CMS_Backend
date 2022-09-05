from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

room_type = (
    ('Furnished','Furnished'),
    ('Semi-Furnished','Semi-Furnished'),
    ('Un-Furnished','Un-Furnished'),
)

class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True,
                              default='rooms/placeholder.png')
    floor = models.IntegerField()
    beds = models.IntegerField()
    room_no = models.IntegerField()
    room_type = models.CharField(choices=room_type,max_length=50)
    tags = TaggableManager();
    _id = models.AutoField(primary_key=True, editable=False)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Room No.: {self.room_no},  Floor {self.floor}'

IS_VERIFY=(
    ('Pending','Pending'),
    ('Verified','Verified'),
    ('Not-Verified','Not-Verified'),
)
class VerificationModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=200)
    mobile=models.IntegerField()
    aadhar=models.ImageField(null=True, blank=True, upload_to="verification/profile/")
    pan_card=models.ImageField(null=True, blank=True, upload_to="verification/profile/")
    is_verify = models.CharField(choices=IS_VERIFY,max_length=50,default='Pending')


    def __str__(self):
        return f'{self.user}, {self.name}'


STATUS_CHOICES=(
    ('Pending','Pending'),
    ('Accept','Accept'),
    ('Reject','Reject'),
)

class RoomBookingModel(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name='room_request_created')
    floor=models.ForeignKey(Room,on_delete=models.CASCADE)
    verified_user = models.OneToOneField(VerificationModel,on_delete=models.CASCADE, primary_key=True) 
    booked_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

    def __str__(self):
        return f'Room No.: {self.room},  Floor {self.floor}'