from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField(default='value')


class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name='ninjas', on_delete=models.CASCADE) #dojo not user_id
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


def create_dojo( postData ):
    name = postData['dojo_name']
    city = postData['city']
    state = postData['state']
    Dojo.objects.create(name=name, city=city, state=state)


def get_dojos():
    return Dojo.objects.all()

def delete_dojo(dojo_id):
    dojo_to_delete = Dojo.objects.get(id=dojo_id)
    dojo_to_delete.delete()

def create_ninja( postData ):
    dojo = Dojo.objects.get(id = int(postData['dojo_id']))
    first_name = postData['first_name']
    last_name = postData['last_name']
    Ninja.objects.create(dojo=dojo, first_name=first_name, last_name=last_name) 

def get_ninjas():
    return Ninja.objects.all()


    