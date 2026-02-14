from django.db import models

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_desc = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

class Description(models.Model):
    desc = models.OneToOneField(Course, on_delete=models.CASCADE)

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def create_course(postData):
    course_name = postData['course_name']
    course_desc = postData['course_desc']
    course = Course.objects.create(course_name=course_name, course_desc=course_desc)
    desc = Description.objects.create(desc=course) #link description to course via one to one field
    return course

def display_courses():
    return Course.objects.all()

def delete_page(id):
    course_to_delete = Course.objects.get(id=id)
    return course_to_delete

def delete_course(id):
    course_to_delete = Course.objects.get(id=id)
    course_to_delete.delete()

def add_comment(postData, id):
    course = Course.objects.get(id=id)
    comment_content = postData['comment_content']
    Comment.objects.create(course = course, comment_content=comment_content)

def display_comments(id):
    course_id = Course.objects.get(id=id)
    return Comment.objects.filter(course_id = course_id)

    

def delete_comment(id):
    comment = Comment.objects.get(id=id)
    comment.delete()