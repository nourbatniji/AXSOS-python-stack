from django.db import models
import re, bcrypt
from datetime import datetime

# Create your models here.


class UserManager(models.Manager):
    def validate_signup(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')

        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be at least 2 characters '
      
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be at least 2 characters'

        if not email_regex.match(postData['email']):
            errors['email'] = 'Invalid email format'

        if email_exist(postData['email']):
            errors['email_unq'] = 'Email already exists'
        
        if not pass_regex.match(postData['password']):
            errors['password'] = 'Password must be at least 8 characters'

        if postData['password'] != postData['confirm_pw']:
            errors['password_match'] = 'Passwords do not match'

        return errors
    
    def validate_login(self, postData):
        login_errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')


        if not email_exist(postData['login_email']):
            login_errors['email_unq'] = 'Email does not exist'

        return login_errors


class TreeManager(models.Manager):
    def validate_tree(self, postData):
        errors = {}
        # SPECIES
        if len(postData['species']) < 0:
            errors['species'] = 'species cannot be empty'

        if len(postData['species']) < 2:
            errors['species_length'] = 'species minimum 2 characters'
      


        # LOCATION
        if len(postData['location']) < 0:
            errors['location'] = 'location cannot be empty'
      
        if len(postData['location']) < 5:
            errors['location_len'] = 'location minimum 5 characters'
      

        # ZIP code
        if len(postData['zip_code']) < 0:
            errors['zip_code'] = 'zip_code cannot be empty'
       
        if not len(postData['zip_code']) == 5:
            errors['zip_code_len'] = 'zip_code must be 5 digits'

        if not postData['zip_code'].isdigit():
            errors['zip_code_num'] = 'zip_code should be digits'

      
        #NOTES
        if len(postData['notes']) < 0:
            errors['notes'] = 'notes cannot be empty'
      
        if len(postData['notes']) > 50:
            errors['notes_len'] = 'notes maximum 50 characters'

        # DATE
        if len(postData['date_found']) < 0:
            errors['date_found'] = 'date_found cannot be empty'
      
        current_time = datetime.now()
        date_found = datetime.strptime(postData['date_found'], "%Y-%m-%d")

        if current_time>date_found:
            errors['date_found_valid'] = 'date_found cannot be in future'

        return errors
      



class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    passwrod = models.CharField(max_length=255)

    # user_trees
    # visited_trees

    objects = UserManager()


class ZipCode(models.Model):
    zip_number = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    #code_trees


class Tree(models.Model):
    species = models.CharField(max_length=45)
    location = models.CharField(max_length=255)
    notes = models.CharField(max_length=500)
    date_found = models.DateField()
    zip_code = models.ForeignKey(ZipCode, related_name='code_trees', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='user_trees', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    users_visits = models.ManyToManyField(User, related_name='visited_trees')

    objects = TreeManager()


def create_user(postData):
    hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
    return User.objects.create(
        first_name = postData['first_name'],
        last_name = postData['last_name'],
        email = postData['email'],
        passwrod = hashed_pw
    )

def email_exist(email):
    return User.objects.filter(email=email).exists()


def create_tree(postData):
    user = User.objects.get(id=postData['user_id'])

    if ZipCode.objects.filter(zip_number=postData['zip_code']):
        print('alreadyexisits')
        zip_number = ZipCode.objects.get(zip_number=postData['zip_code']) 
    else:
        print('created')
        zip_number = ZipCode.objects.create(zip_number=postData['zip_code'])

    tree = Tree.objects.create(
        species = postData['species'],
        location = postData['location'],
        notes = postData['notes'],
        zip_code=zip_number,
        date_found = postData['date_found'],
        created_by = user
    )

    return tree

def get_all_trees():
    return Tree.objects.all()

def delete_tree(postData):
    tree = Tree.objects.get(id=postData['tree_id'])
    tree.delete()

def get_tree_by_id(id):
    return Tree.objects.get(id=id)

def update_tree(postData):
    user = User.objects.get(id=postData['user_id'])
    tree = Tree.objects.get(id=postData['tree_id'])
    tree.species = postData['species']
    tree.location = postData['location']
    tree.date_found = postData['date_found']
    tree.zip_code = postData['zip_code']
    tree.notes = postData['notes']
    tree.save()



def get_zip_by_id(id):
    return ZipCode.objects.get(id=id)


def visit_tree(postData, id):
    tree = Tree.objects.get(id=id)
    user= User.objects.get(id=postData['user_id'])

    user.visited_trees.add(tree)

    print("addedd")
    tree.save()


def get_visits(id):
    tree = Tree.objects.filter(id=id)
    return tree

