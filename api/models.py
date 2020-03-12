from django.db import models

class room(models.Model):
    date_status = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length=100)
    status = models.CharField(max_length=1)

    def __str__(self):
        return self.room
    

class log(models.Model):
    date_status = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    ipaddress = models.CharField(max_length=50)