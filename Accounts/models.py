from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .randgenrator import rand
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.
import datetime

# Create your models here.
ROLE=(("TEACHER","TEACHER"),
       ("STUDENT","STUDENT"))
USER_FIELD=(("ENGINEERING","ENGINEERING"),
            ("MEDICAL","MEDICAL"),
            ("OTHER","OTHER"))

WEEK=(("MONDAY","MONDAY"),
      ("TUESDAY","TUESDAY"),
      ("WEDNESDAY","WEDNESDAY"),
      ("THURSDAY","THURSDAY"),
      ("FRIDAY","FRIDAY"),
      ("SATURDAY","SATURDAY") )
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=15,choices=ROLE,default="STUDENT")
    Uid=models.CharField(max_length=20,null=True)
    user_field=models.CharField(max_length=20,choices=USER_FIELD,null=True)
    date_joined=models.DateField('date_joined',default=datetime.date.today)

    def __str__(self):
           return self.user.username

class classroom(models.Model):
       class_name=models.CharField(max_length=50,null=True)
       class_sec=models.CharField(max_length=50,null=True)
       class_subject=models.CharField(max_length=50,null=True)
       classid=models.CharField(max_length=15,null=True)
       admin=models.ForeignKey(User,on_delete=models.CASCADE)
       c_url=models.URLField(default=None,null=True)
       c_link=models.URLField(default=None,null=True)
       members=models.ManyToManyField(profile)
       rem_members=models.CharField(max_length=3000,null=True)

       def __str__(self):
              return str(self.class_name)

       def get_abs_url(self):
              return reverse('classroom',kwargs={'c_id':self.classid})
       
       def is_admin(self):
              return self.admin

class timetable(models.Model):
       clsobj=models.ForeignKey(classroom,on_delete=models.DO_NOTHING)
       class_day=models.CharField(max_length=15,choices=WEEK)
       class_time=models.TimeField()

       def __str__(self):
              return str(self.clsobj.class_name)


class attendance(models.Model):
       att_class=models.ForeignKey(classroom,on_delete=models.DO_NOTHING)
       attendance_time=models.DateTimeField()
       attendees=models.ManyToManyField(profile)

       def __str__(self):
              return str(self.att_class)

       def is_empty(self):
              if self.attendees.count()!=0:
                     return True
              else:
                     return False

       def absentees(self):
              absentees=[]
              for member in self.att_class.members.all():
                     if member not in self.attendees.all():
                            absentees.append(member)
              return absentees

class posts(models.Model):
       posted_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
       p_class=models.ForeignKey(classroom,on_delete=models.DO_NOTHING)
       notes=models.FileField(null=True,upload_to='posts')
       thumbnail=ImageSpecField(source='notes',processors=[ResizeToFill(50,50)],format='JPEG',options={'quality':60})
       description=models.CharField(max_length=30,null=True)
       post=models.TextField(max_length=500,null=True)
       upload_date=models.DateTimeField()
       
       def __str__(self):
              return str(self.p_class)

       def change(self):
              return str(self.notes)[6:]



    