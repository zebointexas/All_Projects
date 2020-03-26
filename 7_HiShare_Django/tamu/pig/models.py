
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django_mysql.models import EnumField


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


########################################################################
class Ride(models.Model):
    Add_Date = models.DateTimeField(default=timezone.now())
    Depart_Date = models.DateTimeField(default="1997-07-01")
    From = models.CharField(max_length=200)
    From_City = models.CharField(max_length=200, default="College Station")

    To = models.CharField(max_length=200)
    To_City = models.CharField(max_length=200, default="Houston")

    Gas_Need = models.IntegerField(default=3)
    Total_Seats_Available = models.IntegerField(default=3)
    Mobile = models.IntegerField(default=1737888888)
    WeChat = models.CharField(max_length=200)
    Student_Or_Not = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('pig:ride-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.wechat_name + ' - ' + self.ride
########################################################################




########################################################################
class AskRide(models.Model):
    Add_Date = models.DateTimeField(default=timezone.now)

    Depart_Date = models.DateTimeField(default="1997-07-01")
    From = models.CharField(max_length=200)
    From_City = models.CharField(max_length=200, default="College Station")

    To = models.CharField(max_length=200)
    To_City = models.CharField(max_length=200, default="Houston")

    Seats_Needed = models.IntegerField(default=3)
    Mobile = models.IntegerField(default=1737888888)
    WeChat = models.CharField(max_length=200)
    Student_Or_Not = models.BooleanField(default=False)

   ## Gas_Return = EnumField(choices=['1 Gallon Gas', '3 Gallon Gas', '5 Gallon Gas', '7 Gallon Gas', '10 Gallon Gas', '15 Gallon Gas', '25 Gallon Gas'], default='1 Gallon Gas')
    Gas_Return = models.IntegerField(default=3)
    def get_absolute_url(self):
        return reverse('pig:ask-ride-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.wechat_name + ' - ' + self.ride
########################################################################





class Liuyi_test(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    test_filed = models.IntegerField(default=0)

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
   # album_logo = models.FileField()
    album_logo = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('pig:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.song_title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)













