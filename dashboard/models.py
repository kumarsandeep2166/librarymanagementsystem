from django.db import models
import os, time, uuid,string,random
from django.utils.deconstruct import deconstructible

TYPE_OF_INSTITUTION = (
    ('school','school'),
    ('college','college'),
)


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        # eg: filename = 'my uploaded file.jpg'
        ext = filename.split('.')[-1]  #eg: 'jpg'
        uid = uuid.uuid4().hex[:10]    #eg: '567ae32f97'

        # eg: 'my-uploaded-file'
        new_name = '-'.join(filename.replace('.%s' % ext, '').split())

        # eg: 'my-uploaded-file_64c942aa64.jpg'
        renamed_filename = '%(new_name)s_%(uid)s.%(ext)s' % {'new_name': new_name, 'uid': uid, 'ext': ext}

        # eg: 'images/2017/01/29/my-uploaded-file_64c942aa64.jpg'
        return os.path.join(self.path, renamed_filename)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    type_of_institute = models.CharField(max_length=100, choices=TYPE_OF_INSTITUTION, default='school')
    affiliation_body = models.CharField(max_length=100)
    approval_body = models.CharField(max_length=100)
    date_of_approval = models.DateField()
    address = models.TextField()
    corporate_address = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()
    image_path_logo = time.strftime('logo/%Y/%m/%d')
    image_path = time.strftime('attachment/%Y/%m/%d')
    logo = models.ImageField(upload_to=PathAndRename(image_path_logo),blank=True, null=True)
    attachment = models.FileField(upload_to=PathAndRename(image_path),blank=True, null=True)
    other_attachment = models.FileField(upload_to=PathAndRename(image_path),blank=True, null=True)

    def __str__(self):
        return self.name

class Stream(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Year_Sem(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
