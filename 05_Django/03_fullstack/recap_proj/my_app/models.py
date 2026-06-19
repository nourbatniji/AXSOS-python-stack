from django.db import models
import bcrypt
import re

# Create your models here.

class UserManager(models.Manager):
    def reg_validation(self, postData):
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$')
        errors = {}
        if len(postData['first_name']) < 2:
            errors['firsname_valid'] = "First name must contain at least 2 characters"

        if len(postData['last_name']) < 2:
            errors['lasname_valid'] = "Last name must contain at least 2 characters"

        if not email_regex.match(postData['email']):
            errors['email_valid'] = "Invalid email"

        if not pass_regex.match(postData['password']):
            errors['pass_valid'] = "Password must contain at least 8 characters"

        if not pass_regex.match(postData['confirm_pw']):
            errors['confirm_pw_valid'] = "Password confirmatins must contain at least 8 characters"

        if postData['password'] != postData['confirm_pw']:
            errors['pass_match'] = 'Passwords do not match'
        
        return errors
    

    def login_validation(self, postData):
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$')
        errors = {}
        if not email_regex.match(postData['email']):
            errors['email_valid'] = "Invalid email"

        if not pass_regex.match(postData['password']):
            errors['pass_valid'] = "Password must contain at least 8 characters"

        return errors



class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=45)
    confirm_pw= models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #addresses
    objects = UserManager()


class Address(models.Model):
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=255)


def create_user(postData):
    first_name = postData['first_name']
    last_name = postData['last_name']
    email = postData['email']
    password = postData['password']
    confirm_pw = postData['confirm_pw']
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    hashed_confirm_pw = bcrypt.hashpw(confirm_pw.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name=first_name,last_name=last_name,email=email, password=hashed_pw, confirm_pw=hashed_confirm_pw)


def display_all_users():
    return User.objects.all()


def get_by_id(id):
    return User.objects.get(id=id)
     


def delete_user(id):
    user = User.objects.get(id=id)
    user.delete()


def edit_user(postData, id):
    user_edit = User.objects.get(id=id)
    user_edit.first_name = postData['first_name']
    user_edit.last_name = postData['last_name']
    user_edit.email = postData['email']
    user_edit.password = postData['password']
    user_edit.confirm_pw = postData['confirm_pw']
    user_edit.save()


def add_new_address(postData):

    country = postData['country']
    state = postData['state']
    city = postData['city']
    user = User.objects.filter(id=postData['user_id'])
    user = get_by_id(postData["user_id"])
 


    Address.objects.create(user=user, country=country, state=state, city=city)



def get_user_address(id):
    #i have user id 
    user_id = User.objects.get(id=id)
    return user_id.addresses.all()
