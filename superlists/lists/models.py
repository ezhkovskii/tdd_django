from django.db import models


class List(models.Model):
    '''Список'''


class Item(models.Model):
    '''элемент списка'''

    text = models.TextField(default='')
    list = models.ForeignKey(List, on_delete=models.CASCADE)
