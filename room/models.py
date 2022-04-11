from django.db.models import *

# Create your models here.

class Room(Model):
    status_option = [
        (0, '無法預約'),
        (1, '開放預約')
    ]
    roomName = CharField ('教室名稱', max_length=20)
    roomId=CharField ('教室編號', max_length=10)
    roomStatus = IntegerField('狀態', default = 1 , choices = status_option)