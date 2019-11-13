from django import forms
from .models import Profile, TYPE_OF_INSTITUTION, Stream, Course, Year_Sem

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    type_of_institute = forms.ChoiceField(choices=TYPE_OF_INSTITUTION)
    affiliation_body = forms.CharField(max_length=100, required=False)
    approval_body = forms.CharField(max_length=100, required=False)
    date_of_approval = forms.DateField(required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    corporate_address = forms.CharField(widget=forms.Textarea, required=False)
    phone = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)
    logo = forms.ImageField(required=False)
    attachment = forms.FileField(required=False)
    other_attachment = forms.FileField(required=False)

    def save(self):
        data = self.cleaned_data
        user = Profile(
            name=data['name'],
            type_of_institute=data['type_of_institute'],
            affiliation_body=data['affiliation_body'],
            approval_body=data['approval_body'],
            date_of_approval=data['date_of_approval'],
            address=data['address'],
            corporate_address=data['corporate_address'],
            phone=data['phone'],
            email=data['email'],
            attachment=data['attachment'],
            other_attachment=data['other_attachment'],
        )
        user.save()

    def update(self, obj):
        data = self.cleaned_data
        obj.name=data['name']
        obj.type_of_institute=data['type_of_institute']
        obj.affiliation_body=data['affiliation_body']
        obj.approval_body=data['approval_body']
        obj.date_of_approval=data['date_of_approval']
        obj.address=data['address']
        obj.corporate_address=data['corporate_address']
        obj.phone=data['phone']
        obj.email=data['email']
        obj.attachment=data['attachment']
        obj.other_attachment=data['other_attachment']
        obj.save()
        return obj

class StreamForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Stream(name=data['name'])
        user.save()

    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class CourseForm(forms.Form):
    name = forms.CharField(max_length=100)
    stream = forms.ChoiceField(choices=[(o.id, str(o.name)) for o in Stream.objects.all()])

    def save(self):
        data = self.cleaned_data
        stream_obj = Stream.objects.get(pk=data['stream'])
        user = Course(name=data['name'], stream=stream_obj)
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        stream_obj = Stream.objects.get(pk=data['stream'])
        obj.stream = stream_obj
        obj.save()
        return obj

class Year_SemForm(forms.Form):
    name = forms.CharField(max_length=100)
    course = forms.ChoiceField(choices=[(o.id, str(o.name)) for o in Course.objects.all()])

    def save(self):
        data = self.cleaned_data
        course_obj = Course.objects.get(pk=data['course'])
        user = Year_Sem(name=data['name'], course=course_obj)
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        course_obj = Course.objects.get(pk=data['course'])
        obj.course = course_obj
        obj.save()
        return obj
        


