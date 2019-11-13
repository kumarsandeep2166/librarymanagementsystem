import os, time, uuid,string,random
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import datetime
from django.urls import reverse
from django.db.models.signals import pre_save
from dashboard.models import Stream, Course, Year_Sem

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]
def current_year():
    return datetime.date.today().year
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



BLOOD_GROUP=(('A+ve','A+ve'),('A-ve','A-ve'),('B+ve','B+ve'),('B-ve','B-ve'),('AB+ve','AB+ve'),('AB-ve','AB-ve'),('O+ve','O+ve'),('O-ve','O-ve'))
CASTE=(('Gen','GEN'),('SC','SC'),('ST','ST'),('OBC','OBC'),('Others','Others'))
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
OCCUPATION1=(
    ('GE','Govt. Employee'),
    ('PE','Private Employee'),
    ('SE','Self Employed'),
    ('B','Businessman'),
    ('O','Others'),        
)
OCCUPATION2=(
    ('GE','Govt. Employee'),
    ('PE','Private Employee'),
    ('SE','Self Employed'),
    ('B','Businesswoman'),
    ('HM','Home Maker'),
    ('O','Others'),        
)
n=(('india','India'),
    ('others','others'),)
class Student(models.Model):
    enr_id = models.CharField(max_length=250, null=True, blank=True)
    full_name=models.CharField(max_length=20)
    date_of_birth=models.DateField()
    blood_group=models.CharField(max_length=5,choices=BLOOD_GROUP,default='O+ve')
    nationality=models.CharField(max_length=10,choices=n,default='india')
    caste=models.CharField(max_length=10,choices=CASTE,default='Others')
    
    email=models.EmailField(blank=True)
    phone_number=models.CharField(max_length=10,blank=True,validators=[RegexValidator('^[0-9]{10}$', message="Phone Number must be of 10 Digits")])
    aadhar_number=models.CharField(max_length=12,validators=[RegexValidator('^[0-9]{12}$', message="Aadhar Number must be of 12 Digits")])
    gender = models.CharField(max_length=10)   
    fathers_name=models.CharField(max_length=20)
    fathers_occupation=models.CharField(max_length=30)
    
    fathers_phone_no=models.CharField(max_length=10, validators=[RegexValidator('^[0-9]{10}$', message="Please Enter a Valid Phone Number")])
    fathers_email_id=models.EmailField()
    mothers_name=models.CharField(max_length=20)
    mothers_occupation=models.CharField(max_length=30)
    mothers_phone_no=models.CharField(max_length=10, validators=[RegexValidator('^[0-9]{10}$', message="Please Enter a Valid Phone Number")])
    mothers_email_id=models.EmailField(blank=True)
    tenth_board=models.CharField(max_length=50,null=True,blank=True)
    tenth_subjects=models.CharField(max_length=50,null=True,blank=True)
    tenth_school=models.CharField(max_length=50,null=True,blank=True)    
    tenth_full_mark=models.IntegerField(null=True,blank=True)
    tenth_secured_mark=models.IntegerField(null=True,blank=True)
    tenth_percentage=models.FloatField(null=True,blank=True)
    twelth_board=models.CharField(max_length=20,blank=False)
    twelth_stream=models.CharField(max_length=20,blank=False)
    twelth_school=models.CharField(max_length=20,blank=False)
    #twelth_university=models.CharField(max_length=20,blank=True)
    twelth_full_mark=models.IntegerField(null=True,blank=True)
    twelth_secured_mark=models.IntegerField(null=True,blank=True)
    tewlth_percentage=models.FloatField(null=True,blank=True)    
    degree_stream=models.CharField(max_length=20,null=True,blank=True)
    degree_college=models.CharField(max_length=20,null=True,blank=True)
    degree_university=models.CharField(max_length=20,null=True,blank=True)
    degree_full_mark=models.IntegerField(null=True,blank=True)
    degree_secured_mark=models.IntegerField(null=True,blank=True)
    degree_percentage=models.FloatField(null=True,blank=True)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    year_sem = models.ForeignKey(Year_Sem, on_delete=models.CASCADE, null=True, blank=True)
    # present_house_no=models.CharField(max_length=300)
    # present_Lane=models.CharField(max_length=300)
    # present_pin=models.CharField(max_length=6,validators=[RegexValidator('^[0-9]{6}$', message="Aadhar Number must be of 12 Digits")])
    # present_same_address=models.BooleanField(default=False,blank=True)

    # permanent_house_no=models.CharField(max_length=300)
    # permanent_Lane=models.CharField(max_length=300)
    # permanent_pin=models.CharField(max_length=6,validators=[RegexValidator('^[0-9]{6}$', message="Aadhar Number must be of 12 Digits")])
    
    
    YEAR_CHOICES = [(r,r) for r in range(2000, datetime.date.today().year+1)]
    

    image_path = time.strftime('documents/%Y/%m/%d')
    image = models.ImageField(upload_to=PathAndRename(image_path), null=True, blank=True)
    # student_pic=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # student_tenth=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # student_twelth=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # student_degree=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # student_clc=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # student_conduct_certificate=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # student_migration=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # student_birth_certificate=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # student_address=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # student_thumb=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # student_signature=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # tenth_marksheet=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # tewlth_marksheet=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # degree_marksheet=models.ImageField(upload_to=PathAndRename(image_path),blank=True, null=True)
    # term_and_condition=models.BooleanField(default=False)    
    
    def __str__(self):
        return '{}'.format(self.full_name)

    # def get_absolute_url(self):
    #     return reverse('student_detail', kwargs={
    #         'pk': self.pk
    #     })





















