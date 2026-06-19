from django.db import models
from datetime import date, datetime

# Create your models here.

class ShowManager(models.Manager):
    def validate_show(self, postData):
        errors = {}
        #title validation
        titles = Show.objects.filter(title= postData['title'])
        if postData['title'] == '': #check if empty
            errors['title_valid'] = 'Add a title'
        elif len(postData['title']) < 2: #check length
            errors['title_valid'] = 'The title must be at least 2 characters long'
        for title in titles: #check if unique
            if title in titles:
                errors['title_valid'] = 'This title already exists. Please choose another one'

        #network validation
        if postData['network'] == '':
            errors['network_valid'] = 'Add a network'
        if len(postData['network']) < 3:
            errors['network_valid'] = 'Network name must be at least 3 characters long'
       
        #desc validation
        if postData['desc']:
            if len(postData['desc']) < 10:
                errors['desc_valid'] = 'Description must be at least 10 characters long'

        #date validation
        now = date.today()
        release_date = datetime.strptime(postData['release_date'], '%Y-%m-%d').date()
        if not postData['release_date']:
            errors['release_date_valid'] = 'Please select a release date.'
        elif release_date > now:
            errors['release_date_valid'] = 'Release date cannot be in the future.'

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


def create_show(postData):
    title = postData['title']
    network = postData['network']
    release_date = postData['release_date']
    desc = postData['desc']

    show = Show.objects.create(title=title, network=network, release_date=release_date, desc=desc)
    return show

def display_all():
    return Show.objects.all()

def show_details(id):
    show = Show.objects.get(id=id)
    return show

def show_to_update(id):
    return Show.objects.get(id=id)

def edit_show(postData ,id):
    show_to_edit = Show.objects.get(id=id)
    show_to_edit.title = postData['title']
    show_to_edit.network = postData['network']
    show_to_edit.release_date = postData['release_date']
    show_to_edit.desc = postData['desc']
    show_to_edit.save()

def delete_show_by_id(postData, id):
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
