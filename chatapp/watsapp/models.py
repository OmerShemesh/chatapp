from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    message_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField('publication date')
    sender = models.ForeignKey(User,related_name='sender')
    receiver = models.ForeignKey(User,related_name='receiver')
    def __str__(self):
        return ("Message From {} to {}\nDate: {}\nThe Message Content:\n{}".format(self.sender,self.receiver,self.pub_date,self.message_text))
