import os, time, uuid,string,random
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import datetime
from django.urls import reverse
from django.db.models.signals import pre_save
#from .utils import unique_enrollment_number_generator
from django.contrib.auth.models import User

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

class Employee_Department(models.Model):
    employee_department=models.CharField(max_length=100)
    def __str__(self):
        return self.employee_department

class Employee_Designation(models.Model):
    employee_department=models.ForeignKey(Employee_Department,on_delete=models.SET_NULL,null=True,blank=False)
    employee_designation=models.CharField(max_length=150)
    def __str__(self):
        return self.employee_designation
    
class Employee(models.Model):
    BLOOD_GROUP=(('A+ve','A+ve'),('A-ve','A-ve'),('B+ve','B+ve'),('B-ve','B-ve'),('AB+ve','AB+ve'),('AB-ve','AB-ve'),('O+ve','O+ve'),('O-ve','O-ve'))
    
    ttl=(
        ('mr','Mr.'),
        ('ms','Mrs.'),
        ('miss','Miss'),
        ('dr','Dr.'),
    )
    national=(
        ('in','Indian'),
    )
    caste=(
        ('Gen','GEN'),
        ('sc','SC'),
        ('st','ST'),
        ('obc','OBC'),
        ('others','Others'),
    )
    scale=(
        ('5th','5th Pay'),
        ('6th','6th Pay'),
        ('cons','Consolidated'),
    )
    type_join=(
        ('part','Part Time'),
        ('full','Full Time'),
        ('part','Contracted'),
    )
    GENDER_CHOICES=(        
            ('M', 'Male'),
            ('F', 'Female'),
            ('O','others')
    )
    RELIGION_CHOICES=(
        ('H','Hindu'),
        ('M','Muslim'),
        ('C','Christian'),
        ('O','Others'),
    )
    u_degree=(
        ('b.tech','B.Tech'),
        ('bachlr','Bachelors'),
        ('be','BE'),
    )
    m_degree=(
        ('m.tech','M.Tech'),
        ('master','Masters'),
        ('me','ME'),
    )
    physically_handicap=(
        ('y','Yes'),
        ('n','No'),
    )
    title=models.CharField(max_length=5,choices=ttl,default='Mr.')
    full_name=models.CharField(max_length=15)
    date_of_birth=models.DateField()
    phone_no=models.CharField(max_length=10,blank=False,validators=[RegexValidator('^[0-9]{10}$', message="Phone Number must be of 12 Digits")])
    aadhar_no=models.CharField(max_length=12,validators=[RegexValidator('^[0-9]{12}$', message="Aadhar Number must be of 12 Digits")])
    pan_no=models.CharField(max_length=15,blank=False)
    type_of_joining = models.CharField(max_length=250, null=True, blank=True)
    email=models.EmailField()
    employee_department=models.ForeignKey(Employee_Department,on_delete=models.SET_NULL,null=True,blank=False)
    employee_designation=models.ForeignKey(Employee_Designation,on_delete=models.SET_NULL,null=True,blank=False)
    type_of_joining=models.CharField(max_length=15,choices=type_join,default='Full Time')
    tenth_subjects=models.CharField(max_length=20,blank=False)
    tenth_school=models.CharField(max_length=20,blank=False)
    tenth_board=models.CharField(max_length=20,blank=False)    
    tenth_full_mark=models.IntegerField(blank=False)
    tenth_secured_mark=models.IntegerField(blank=False)
    tenth_percentage=models.FloatField(blank=False)
    twelth_stream=models.CharField(max_length=20,blank=False)
    twelth_college=models.CharField(max_length=20,blank=False)
    twelth_board=models.CharField(max_length=20,blank=False)       
    #twelth_university=models.CharField(max_length=20,blank=True)
    twelth_full_mark=models.IntegerField(blank=False)
    twelth_secured_mark=models.IntegerField(blank=False)
    tewlth_percentage=models.FloatField(blank=False)
    degree_stream=models.CharField(max_length=20,blank=False)
    degree_college=models.CharField(max_length=20,blank=False)
    degree_university=models.CharField(max_length=20,blank=False)
    degree_full_mark=models.IntegerField(blank=True,null=True)
    degree_secured_mark=models.IntegerField(blank=True,null=True)
    degree_percentage=models.FloatField(blank=False)
    postdegree_stream=models.CharField(max_length=20,blank=True)
    postdegree_college=models.CharField(max_length=20,blank=True)
    postdegree_university=models.CharField(max_length=20,blank=True)
    postdegree_full_mark=models.IntegerField(blank=True,null=True)
    postdegree_secured_mark=models.IntegerField(blank=True,null=True)
    postdegree_percentage=models.FloatField(null=True,blank=True)

    
    def __str__(self):
        return '{}'.format(self.full_name)
    