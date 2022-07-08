from django.db import models
# Create your models here.
'''WEEK=(("MONDAY","MONDAY"),
      ("TUESDAY","TUESDAY"),
      ("WEDNESDAY","WEDNESDAY"),
      ("THURSDAY","THURSDAY"),
      ("FRIDAY","FRIDAY"),
      ("SATURDAY","SATURDAY") )
class timetable(models.Model):
	class_obj=models.ForeignKey(classroom,on_delete=models.DO_NOTHING)
	class_day=models.CharField(max_length=15,choices=WEEK)

	def __str__(self):
		return f"{self.class_obj.class_name} post"'''