from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Student
from dashboard.models import Stream, Course, Year_Sem


def student_create(request):
    if request.method == "POST":
        full_name = request.POST.get('first_name')
        date_of_birth = request.POST.get('dob')
        blood_group = request.POST.get('bgroup')
        nationality = request.POST.get('nationality')
        caste = request.POST.get('caste')
        email = request.POST.get('email')
        phone_number = request.POST.get('contact')
        aadhar_number = request.POST.get('aadhar_num')
        gender = request.POST.get('gender')
        fathers_name = request.POST.get('fathersname')
        fathers_occupation = request.POST.get('fatheroccupation')
        fathers_phone_no = request.POST.get('fcontact')
        fathers_email_id = request.POST.get('femail')
        mothers_name = request.POST.get('mname')
        mothers_occupation = request.POST.get('moccupation')
        mothers_phone_no = request.POST.get('mcontact')
        mothers_email_id = request.POST.get('memail')
        tenth_board = request.POST.get('tenthboard')
        tenth_subjects = request.POST.get('tenthstream')
        tenth_school = request.POST.get('tenthschool')
        tenth_full_mark = request.POST.get('tenthfullmark')
        tenth_secured_mark = request.POST.get('tenthsecuredmark')
        tenth_percentage = request.POST.get('tenthpercentage')
        twelth_board = request.POST.get('twelthboard')
        twelth_stream = request.POST.get('twelthstream')
        twelth_school = request.POST.get('twelthschool')
        twelth_full_mark = request.POST.get('twelthfullmark')
        twelth_secured_mark = request.POST.get('twelthsecuredmark')
        tewlth_percentage = request.POST.get('twelthpercentage')
        degree_stream = request.POST.get('graduatestream')
        degree_college = request.POST.get('graduateschool')
        degree_university = request.POST.get('graduateboard')
        degree_full_mark = request.POST.get('graduatefullmark')
        degree_percentage = request.POST.get('graduatepercentage')
        image = request.POST.get('stu_image')
        stream = request.POST.get('stream')
        stream_obj = Stream.objects.get(pk=stream)
        course = request.POST.get('course')
        course_obj = Course.objects.get(pk=course)
        year_sem = request.POST.get('year_sem')
        year_sem_obj = Year_Sem.objects.get(pk=year_sem)
        user = Student(
            image=image,
            full_name=full_name,
            date_of_birth=date_of_birth,
            blood_group=blood_group,
            nationality=nationality,
            caste=caste,
            email=email,
            phone_number=phone_number,
            aadhar_number=aadhar_number,
            gender=gender,
            fathers_name=fathers_name,
            fathers_occupation=fathers_occupation,
            fathers_phone_no=fathers_phone_no,
            fathers_email_id=fathers_email_id,
            mothers_name=mothers_name,
            mothers_occupation=mothers_occupation,
            mothers_phone_no=mothers_phone_no,
            mothers_email_id=mothers_email_id,
            tenth_board=tenth_board,
            tenth_subjects=tenth_subjects,
            tenth_school=tenth_school,
            tenth_full_mark=tenth_full_mark,
            tenth_secured_mark=tenth_secured_mark,
            tenth_percentage=tenth_percentage,
            twelth_board=twelth_board,
            twelth_stream=twelth_stream,
            twelth_school=twelth_school,
            twelth_full_mark=twelth_full_mark,
            twelth_secured_mark=twelth_secured_mark,
            tewlth_percentage=tewlth_percentage,
            degree_stream=degree_stream,
            degree_college=degree_college,
            degree_university=degree_university,
            degree_full_mark=degree_full_mark,
            degree_percentage=degree_percentage,
            stream=stream_obj,
            course=course_obj,
            year_sem=year_sem_obj
            )
        user.save()
        return redirect(reverse_lazy('student_list'))
    else:
        st_queryset = Student.objects.all()
        stream_queryset = Stream.objects.all()
        course_queryset = Course.objects.all()
        year_sem = Year_Sem.objects.all()
        context = {
        'st_queryset':st_queryset,
        'stream_queryset':stream_queryset,
        'course_queryset':course_queryset,
        'year_sem':year_sem,
        }
        return render(request, 'dashboard/student_create.html',context)

def student_list(request):
    st_queryset = Student.objects.all()
    stream_queryset = Stream.objects.all()
    course_queryset = Course.objects.all()
    year_sem = Year_Sem.objects.all()
    context = {
        'st_queryset':st_queryset,
        'stream_queryset':stream_queryset,
        'course_queryset':course_queryset,
        'year_sem':year_sem,
    }
    return render(request, 'dashboard/student_list.html', context)

def student_edit(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        image = request.POST.get('stu_image')
        full_name = request.POST.get('first_name')
        date_of_birth = request.POST.get('dob')
        blood_group = request.POST.get('bgroup')
        nationality = request.POST.get('nationality')
        caste = request.POST.get('caste')
        email = request.POST.get('email')
        phone_number = request.POST.get('contact')
        aadhar_number = request.POST.get('aadhar_num')
        gender = request.POST.get('gender')
        fathers_name = request.POST.get('fathersname')
        fathers_occupation = request.POST.get('fatheroccupation')
        fathers_phone_no = request.POST.get('fcontact')
        fathers_email_id = request.POST.get('femail')
        mothers_name = request.POST.get('mname')
        mothers_occupation = request.POST.get('moccupation')
        mothers_phone_no = request.POST.get('mcontact')
        mothers_email_id = request.POST.get('memail')
        tenth_board = request.POST.get('tenthboard')
        tenth_subjects = request.POST.get('tenthstream')
        tenth_school = request.POST.get('tenthschool')
        tenth_full_mark = request.POST.get('tenthfullmark')
        tenth_secured_mark = request.POST.get('tenthsecuredmark')
        tenth_percentage = request.POST.get('tenthpercentage')
        twelth_board = request.POST.get('twelthboard')
        twelth_stream = request.POST.get('twelthstream')
        twelth_school = request.POST.get('twelthschool')
        twelth_full_mark = request.POST.get('twelthfullmark')
        twelth_secured_mark = request.POST.get('twelthsecuredmark')
        tewlth_percentage = request.POST.get('twelthpercentage')
        degree_stream = request.POST.get('graduatestream')
        degree_college = request.POST.get('graduateschool')
        degree_university = request.POST.get('graduateboard')
        degree_full_mark = request.POST.get('graduatefullmark')
        degree_percentage = request.POST.get('graduatepercentage')
        stream = request.POST.get('stream')
        stream_obj = Stream.objects.get(pk=stream)
        course = request.POST.get('course')
        course_obj = Course.objects.get(pk=course)
        year_sem = request.POST.get('year_sem')
        year_sem_obj = Year_Sem.objects.get(pk=year_sem)
        user = Student.objects.filter(id=obj.id).update(
            image=image,
            full_name=full_name,
            date_of_birth=date_of_birth,
            blood_group=blood_group,
            nationality=nationality,
            caste=caste,
            email=email,
            phone_number=phone_number,
            aadhar_number=aadhar_number,
            gender=gender,
            fathers_name=fathers_name,
            fathers_occupation=fathers_occupation,
            fathers_phone_no=fathers_phone_no,
            fathers_email_id=fathers_email_id,
            mothers_name=mothers_name,
            mothers_occupation=mothers_occupation,
            mothers_phone_no=mothers_phone_no,
            mothers_email_id=mothers_email_id,
            tenth_board=tenth_board,
            tenth_subjects=tenth_subjects,
            tenth_school=tenth_school,
            tenth_full_mark=tenth_full_mark,
            tenth_secured_mark=tenth_secured_mark,
            tenth_percentage=tenth_percentage,
            twelth_board=twelth_board,
            twelth_stream=twelth_stream,
            twelth_school=twelth_school,
            twelth_full_mark=twelth_full_mark,
            twelth_secured_mark=twelth_secured_mark,
            tewlth_percentage=tewlth_percentage,
            degree_stream=degree_stream,
            degree_college=degree_college,
            degree_university=degree_university,
            degree_full_mark=degree_full_mark,
            degree_percentage=degree_percentage,
            stream=stream_obj,
            course=course_obj,
            year_sem=year_sem_obj
            )
        return redirect(reverse_lazy('student_list'))
    else:
        st_queryset = Student.objects.all()
        stream_queryset = Stream.objects.all()
        course_queryset = Course.objects.all()
        year_sem = Year_Sem.objects.all()
        id_of_object = obj
        context = {
        'id_of_object':id_of_object,
        'st_queryset':st_queryset,
        'stream_queryset':stream_queryset,
        'course_queryset':course_queryset,
        'year_sem':year_sem,
        }
        return render(request, 'dashboard/student_update.html',context)

def student_delete(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    obj.delete()
    return render(request, 'dashboard/student_confirm_delete.html')