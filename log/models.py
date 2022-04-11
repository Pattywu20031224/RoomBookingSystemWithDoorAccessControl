from MySQLdb import Date
from django.db.models import *
from user.models import *
from django.contrib.auth.models import User
from classes.models import *
from room.models import *
# Create your models here.

class Log(Model):
    type_option = [
        (0, '單筆預約'),
        (1, '多筆預約')
    ]

    
    
    logtype = IntegerField('預約之類型', default=0 , choices=type_option)
    logUser = ForeignKey(User, CASCADE)
    logPurpose = ForeignKey(Classes, CASCADE)
    logRoom = ForeignKey(Room, CASCADE)
    logDate= DateField('預約日期')
    logStart = TimeField('開始時間')
    logEnd = TimeField('結束時間')  
