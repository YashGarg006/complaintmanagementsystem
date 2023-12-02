from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import RegexValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

# 1) Profile Mode

# {Add Profile Model Here}
class Meta:
    app_label = 'CMsystem'
class Profile(models.Model):
    typeuser =(('student','student'),('supervisor', 'supervisor'))
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    phone_regex =RegexValidator(regex=r'^\d{10,10}$', message="Phone number must be entered in the format:Up to 10 digits allowed.")
    contact_number = models.CharField(validators=[phone_regex], max_length=10, blank=True) 
    profile_pic = models.ImageField(null = True, blank = True)
    type_user=models.CharField(max_length=20,default='student',choices=typeuser)
    CB=(('ICT',"ICT"),('ICT with CS',"ICT with CS"),('MnC',"MnC"),('Robotics',"Robotics"))
    Branch=models.CharField(choices=CB,max_length=29,default='ICT')
    def __str__(self):
        return self.user.username
    
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# 2) Complaint Model
class Complaint(models.Model):
    STATUS =((1,'Solved'),(2, 'InProgress'),(3,'Pending'))
    TYPE=(('Cafeteria',"Cafeteria"),('Academics',"Academics"),('Hostel',"Hostel"),('LT & Infrastructure',"LT & Infrastructure"),('Sports',"Sports"),('Other',"Other"))
    Subject=models.CharField(max_length=200,blank=False,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    Type_of_complaint=models.CharField(choices=TYPE,null=True,max_length=200)
    Description=models.TextField(max_length=4000,blank=False,null=True)
    Time = models.DateField(auto_now=True)
    status=models.IntegerField(choices=STATUS,default=3)
    def __init__(self, *args, **kwargs):
        super(Complaint, self).__init__(*args, **kwargs)
        self.__status = self.status

    def save(self, *args, **kwargs):
        if self.status and not self.__status:
            self.active_from = datetime.now()
        super(Complaint, self).save(*args, **kwargs)
    
    def __str__(self):
     	return self.get_Type_of_complaint_display()
    
