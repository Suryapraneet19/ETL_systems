from django.db import models
from datetime import datetime
from dateutil.parser import parse

# Create your models here.
class time_logs_challange_table(models.Model):
    id =models.IntegerField(primary_key=True);
    Username = models.CharField(max_length=150);
    Booking_Date_From = models.CharField(max_length=150);
    Time_Tracked = models.CharField(max_length=150);
    Time_Tracked_Text = models.CharField(max_length=150);
    Job_Number = models.CharField(max_length=150);
    Task_Time_Estimated = models.CharField(max_length=150);
    Task_Time_Estimated_Text = models.CharField(max_length=150);
    Booking_Codes = models.CharField(max_length=150);
    Team = models.CharField(max_length=150);

    class Meta:
        db_table = 'time_logs_challange_table'
        
        
