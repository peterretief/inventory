from django.db import models
from django.utils import timezone

class Item(models.Model):
    stock_id = models.CharField(max_length=200)
    stock_title = models.CharField(max_length=200)
    input_date = models.DateTimeField('date added to inventory', blank=True, null=True, default=timezone.now)
    def __str__(self):
        return self.stock_title
    def was_added_recently(self):
        return self.input_date >= timezone.now() - datetime.timedelta(days=1)

class Activity(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    activity_text = models.CharField(max_length=200)
    instock = models.IntegerField(default=0)
    input_date = models.DateTimeField('Activity on item', blank=True, null=True, default=timezone.now)
    def __str__(self):
        return self.activity_text
    def was_added_recently(self):
        return self.input_date >= timezone.now() - datetime.timedelta(days=1)


# Create your models here.
