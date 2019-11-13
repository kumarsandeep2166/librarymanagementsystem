from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Stream, Course, Year_Sem
from .forms import ProfileForm, StreamForm, CourseForm, Year_SemForm
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy


def index(request):
    return render(request, 'dashboard/index.html')

def master1(request):
    return render(request, 'dashboard/master1.html')

def master2(request):
    return render(request, 'dashboard/master2.html')

def master3(request):
    return render(request, 'dashboard/master3.html')

class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'dashboard/profile.html'
    form_class = ProfileForm

    def get_context_data(self,**kwargs):
        context=super(ProfileCreateView,self).get_context_data(**kwargs)
        return context
    
    def get(self, request, *args, **kwargs):
        context = {'form':ProfileForm()}
        return context

    def post(self, request, *args, **kwargs):
        form=ProfileForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('profilepage')
        return render(request,'dashboard/profile.html',{'form':form})

def profilepage(request):
    queryset = Profile.objects.all()
    context = {
        'queryset':queryset
    }
    return render(request,'dashboard/profile_page.html', context)

def profile_update(request, pk):
    obj = get_object_or_404(Profile, pk=pk)
    if request.method=="POST":
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.update(obj)
        return redirect(reverse_lazy('profile_page'))

    else:
        form = ProfileForm()
        form.fields["name"].initial = obj.name
        form.fields["type_of_institute"].initial = obj.type_of_institute
        form.fields["affiliation_body"].initial = obj.affiliation_body
        form.fields["approval_body"].initial = obj.approval_body
        form.fields["date_of_approval"].initial = obj.date_of_approval
        form.fields["address"].initial = obj.address
        form.fields["corporate_address"].initial = obj.corporate_address
        form.fields["phone"].initial = obj.phone
        form.fields["email"].initial = obj.email
        form.fields["attachment"].initial = obj.attachment
        form.fields["other_attachment"].initial = obj.other_attachment
        return render(request,'dashboard/profile_create.html',{'form':form})

class StreamCreate(CreateView):
    model = Stream
    form_class = StreamForm
    template_name = 'dashboard/stream_create.html'

    def get_context_data(self,**kwargs):
        context=super(StreamCreate,self).get_context_data(**kwargs)
        return context
    
    def get(self, request, *args, **kwargs):
        context = {'form':StreamForm()}
        return context

    def post(self, request, *args, **kwargs):
        form=StreamForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('stream_page')
        return render(request,'dashboard/stream_create.html',{'form':form})


def profile_create(request):
    if request.method == "POST":
        name = request.POST.get('pname')
        type_of_institute = request.POST.get('ptype_institute')
        affiliation_body = request.POST.get('paffiliation_body')
        approval_body = request.POST.get('papproved_body')
        date_of_approval = request.POST.get('pdate')
        address = request.POST.get('paddress')
        corporate_address = request.POST.get('pcopaddress')
        phone = request.POST.get('pphone')
        email = request.POST.get('pemail')
        logo = request.POST.get('pimage')
        attachment = request.POST.get('pattachment')
        other_attachment = request.POST.get('other_attachment')
        user = Profile(name=name,type_of_institute=type_of_institute,affiliation_body=affiliation_body,
                        approval_body=approval_body,attachment=attachment,date_of_approval=date_of_approval,other_attachment=other_attachment,
                        logo=logo,email=email,address=address,corporate_address=corporate_address,phone=phone)
        user.save()
        return redirect('profilepage')
    else:
        return render(request, 'dashboard/profile.html')

def profile_list(request):
    pqueryset = Profile.objects.all()
    context = {
        'pqueryset':pqueryset
    }
    return render(request, 'dashboard/profile_page.html')

def profile(request):
    return render(request, 'dashboard/profile.html')

def profile_edit(request, pk):
    pass

def profile_delete(request, pk):
    pass

def stream_create(request):
    if request.method == "POST":
        name = request.POST.get('streamname')
        user = Stream(name=name)
        user.save()
        return redirect(reverse_lazy('stream_list'))
    else:
        return render(request, 'dashboard/coursesetup.html')

def stream_list(request):
    st_queryset = Stream.objects.all()
    context = {
        'st_queryset':st_queryset
    }
    return render(request, 'dashboard/coursesetup.html', context)

def stream_edit(request,pk):
    obj = get_object_or_404(Stream, pk=pk)
    if request.method == "POST":
        name = request.POST.get('streamname')
        user = Stream.objects.filter(pk=obj.id).update(name=name)
        return redirect(reverse_lazy('stream_list'))
    else:
        return render(request, 'dashboard/coursesetup.html')

def stream_delete(request, pk):
    user = get_object_or_404(Stream, pk=pk)
    user.delete()
    return redirect(reverse_lazy('stream_list'))


def coursesetup(request):
    return render(request, 'dashboard/coursesetup.html')

def course_create(request):
    if request.method == "POST":
        name = request.POST.get('coursename')
        stream = request.POST.getlist('streamset')
        stream_obj = Stream.objects.get(pk__in=stream)
        print(stream_obj)
        user = Course(name=name, stream=stream_obj)
        user.save()
        return redirect(reverse_lazy('course_list'))
    else:
        return render(request, 'dashboard/coursesetup.html')

def course_list(request):
    cu_queryset = Course.objects.all()
    context = {
        'cu_queryset':cu_queryset
    }
    return render(request, 'dashboard/coursesetup.html', context)

def course_edit(request, pk):
    obj = get_object_or_404(Stream, pk=pk)
    if request.method == "POST":
        name = request.POST.get('coursename')
        stream = request.POST.get('streamnamecourse')
        stream_obj = Stream.objects.get(pk=stream)
        user = Course.objects.filter(pk=obj.id).update(name=name,stream=stream_obj)
        return redirect(reverse_lazy('course_list'))
    else:
        return render(request, 'dashboard/coursesetup.html')

def course_delete(request, pk):
    user = get_object_or_404(Course, pk=pk)
    user.delete()
    return redirect(reverse_lazy('course_list'))

def year_sem_create(request):
    if request.method == "POST":
        name = request.POST.get('yrsname')
        course = request.POST.getlist('courserel')
        course_obj = Course.objects.get(pk__in=course)
        user = Year_Sem(name=name, course=course_obj)
        user.save()
        return redirect(reverse_lazy('year_sem_list'))
    else:
        return render(request, 'dashboard/coursesetup.html')

def year_sem_list(request):
    yr_queryset = Year_Sem.objects.all()
    context = {
        'yr_queryset':yr_queryset
    }
    return render(request, 'dashboard/coursesetup.html', context)

def year_sem_edit(request, pk):
    obj = get_object_or_404(Year_Sem, pk=pk)
    if request.method == "POST":
        name = request.POST.get('yrsname')
        course = request.POST.get('courserel')
        course_obj = Course.objects.get(pk=course)
        user = Year_Sem.objects.filter(pk=obj.id).update(name=name, course=course_obj)
        return redirect(reverse_lazy('year_sem_list'))
    else:
        return render(request, 'dashboard/coursesetup.html')

def year_sem_delete(request, pk):
    user = get_object_or_404(Year_Sem, pk=pk)
    user.delete()
    return redirect(reverse_lazy('year_sem_list'))