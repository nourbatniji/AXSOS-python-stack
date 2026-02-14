from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

def create_user(requestPost):
    first_name = requestPost['first_name']
    last_name = requestPost['last_name']
    email_address = requestPost['email_address']
    age = requestPost['age']
    User.objects.create(first_name=first_name, last_name=last_name, email_address=email_address, age=age)

def delete_user(user_id):
    user_to_delete = User.objects.get(id = user_id)
    user_to_delete.delete()
    
def get_all_users():
    return User.objects.all()

