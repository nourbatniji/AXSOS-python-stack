from django.db import models

# Create your models here.



class Dojo(models.Model):
    dojo_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #ninjas = 

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name='ninjas', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def create_dojo(postData):
    Dojo.objects.create(
        dojo_name=postData['dojo_name'],
        city=postData['city'],
        state=postData['state'],
    )

def get_dojos():
    return Dojo.objects.all()

def create_ninja(postData):
    dojo = Dojo.objects.get(id=postData['dojo_id'])
    Ninja.objects.create(
        dojo=dojo,
        first_name=postData['first_name'],
        last_name=postData['last_name'],
    )


def get_ninjas():
    return Ninja.objects.all()


def get_ninjas_of_dojo(id):
    dojo = Dojo.objects.get(id=id)
    return dojo.ninjas.all()

def delete_dojo(postData):
    dojo = Dojo.objects.filter(id=postData['dojo_id'])
    dojo.delete()