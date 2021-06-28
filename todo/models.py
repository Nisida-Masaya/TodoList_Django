from django.db import models

# Create your models here.

CHOICE = (('danger', 'high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    contens = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices= CHOICE
        )
    duedate = models.DateField()

    #データベースのオブジェクトの名前をタイトルにしている
    def __str__(self):
        return self.title
        
