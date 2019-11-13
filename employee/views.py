from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Employee_Department, Employee_Designation
from django.urls import reverse_lazy

def employee_department_create(request):
    if request.method == "POST":
        dept_name = request.POST.get('department')
        user = Employee_Department(employee_department=dept_name)
        user.save()
        return redirect(reverse_lazy('emp_dept_list'))
    else:
        return render(request, 'dashboard/employee_set.html')

def employee_department_list(request):
    dept_queryset = Employee_Department.objects.all()
    context = {
        'dept_queryset':dept_queryset,
    }
    return render(request, 'dashboard/employee_set.html', context)

def employee_department_edit(request, pk):
    obj = get_object_or_404(Employee_Department, pk=pk)
    if request.method == "POST":
        name = request.POST.get('department')
        user = Employee_Department.objects.filter(pk=obj.pk).update(employee_department=name)
        return redirect(reverse_lazy('emp_dept_list'))
    else:
        return render(request, 'dashboard/employee_set.html')

def employee_designation_create(request):
    if request.method == "POST":
        dept = request.POST.get('department')
        dept_obj = Employee_Department.objects.get(pk=dept)
        desgn = request.POST.get('designation')
        user = Employee_Designation(employee_department=dept_obj,employee_designation=desgn)
        user.save()
        return redirect(reverse_lazy('employee_designation_list'))
    else:
        dept_queryset = Employee_Department.objects.all()
        desgn_queryset = Employee_Designation.objects.all()
        context = {
            'dept_queryset':dept_queryset,
            'desgn_queryset':desgn_queryset,
        }
        return render(request, 'dashboard/employee_set.html', context)

def employee_designation_list(request):
    dept_queryset = Employee_Department.objects.all()
    desgn_queryset = Employee_Designation.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'desgn_queryset':desgn_queryset,
    }
    return render(request, 'dashboard/employee_set.html', context)

def employee_designation_edit(request, pk):
    obj = get_object_or_404(Employee_Designation, pk=pk)
    if request.method == "POST":
        dept = request.POST.get('department')
        dept_obj = Employee_Department.objects.get(pk=dept)
        desgn = request.POST.get('designation')
        user = Employee_Designation.objects.filter(id=obj.id).update(employee_department=dept_obj,employee_designation=desgn)        
        return redirect(reverse_lazy('employee_designation_list'))
    else:
        dept_queryset = Employee_Department.objects.all()
        desgn_queryset = Employee_Designation.objects.all()
        context = {
            'dept_queryset':dept_queryset,
            'desgn_queryset':desgn_queryset,
        }
        return render(request, 'dashboard/employee_set.html', context)


def employee_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        full_name = request.POST.get('full_name')        
        date_of_birth = request.POST.get('dob')
        aadhar_no = request.POST.get('aadhar_no')
        pan_no = request.POST.get('pan_no')
        phone_no = request.POST.get('phone_number')
        email = request.POST.get('email')
        type_of_joining = request.POST.get('type_of_joining')
        department = request.POST.get('department')
        department_obj = Employee_Department.objects.get(pk=department)
        designation = request.POST.get('designation')
        designation_obj = Employee_Designation.objects.get(pk=designation)
        tenth_subjects = request.POST.get('10thstream')
        tenth_school = request.POST.get('10thschool')
        tenth_board = request.POST.get('10thboard')
        tenth_full_mark = request.POST.get('10thfullmark')
        tenth_secured_mark = request.POST.get('10thsecuredmark')
        tenth_percentage = request.POST.get('10thcg')
        twelth_stream = request.POST.get('12thstream')
        twelth_college = request.POST.get('12thschool')
        twelth_board = request.POST.get('12thboard')
        twelth_full_mark = request.POST.get('12thfullmark')
        twelth_secured_mark = request.POST.get('12thsecuredmark')
        tewlth_percentage = request.POST.get('12thcg')
        degree_stream = request.POST.get('degstream')
        degree_college = request.POST.get('degschool')
        degree_university = request.POST.get('degboard')
        degree_full_mark = request.POST.get('degfullmark')
        degree_secured_mark = request.POST.get('degsecuremark')
        degree_percentage = request.POST.get('degcg')
        postdegree_stream = request.POST.get('pgdegstream')
        postdegree_college = request.POST.get('pgdegschool')
        postdegree_university = request.POST.get('pgdegboard')
        postdegree_full_mark = request.POST.get('pgdegfullmark')
        postdegree_secured_mark = request.POST.get('pgdegsecuremark')
        postdegree_percentage = request.POST.get('pgdegcg')
        user = Employee(title=title,full_name=full_name,date_of_birth=date_of_birth,aadhar_no=aadhar_no,
                        pan_no=pan_no,phone_no=phone_no,email=email,type_of_joining=type_of_joining,
                        employee_department=department_obj,employee_designation=designation_obj,
                        tenth_subjects=tenth_subjects,tenth_school=tenth_school,tenth_board=tenth_board,
                        tenth_full_mark=tenth_full_mark,tenth_secured_mark=tenth_secured_mark,
                        tenth_percentage=tenth_percentage,twelth_stream=twelth_stream,
                        twelth_college=twelth_college,twelth_board=twelth_board,twelth_full_mark=twelth_full_mark,
                        twelth_secured_mark=twelth_secured_mark,tewlth_percentage=tewlth_percentage,
                        degree_stream=degree_stream,degree_college=degree_college,degree_university=degree_university,
                        degree_full_mark=degree_full_mark,degree_secured_mark=degree_secured_mark,
                        degree_percentage=degree_percentage,postdegree_stream=postdegree_stream,
                        postdegree_college=postdegree_college,postdegree_university=postdegree_university,
                        postdegree_full_mark=postdegree_full_mark,postdegree_secured_mark=postdegree_secured_mark,
                        postdegree_percentage=postdegree_percentage,
        )
        print(user)
        user.save()
        return redirect(reverse_lazy('employee_list'))
    else:
        dept_queryset = Employee_Department.objects.all()
        desgn_queryset = Employee_Designation.objects.all()
        emp_queryset = Employee.objects.all()
        context = {
            'dept_queryset':dept_queryset,
            'desgn_queryset':desgn_queryset,
            'emp_queryset':emp_queryset,
        }
        return render(request, 'dashboard/employee_create.html', context)

def employee_list(request):
    dept_queryset = Employee_Department.objects.all()
    desgn_queryset = Employee_Designation.objects.all()
    emp_queryset = Employee.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'desgn_queryset':desgn_queryset,
        'emp_queryset':emp_queryset,
    }
    return render(request, 'dashboard/employee_list.html', context)

def employee_edit(request, pk):
    obj = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        title = request.POST.get('title')
        full_name = request.POST.get('full_name')        
        date_of_birth = request.POST.get('dob')
        aadhar_no = request.POST.get('aadhar_no')
        pan_no = request.POST.get('pan_no')
        phone_no = request.POST.get('phone_number')
        email = request.POST.get('email')
        type_of_joining = request.POST.get('type_of_joining')
        department = request.POST.get('department')
        department_obj = Employee_Department.objects.get(pk=department)
        designation = request.POST.get('designation')
        designation_obj = Employee_Designation.objects.get(pk=designation)
        tenth_subjects = request.POST.get('10thstream')
        tenth_school = request.POST.get('10thschool')
        tenth_board = request.POST.get('10thboard')
        tenth_full_mark = request.POST.get('10thfullmark')
        tenth_secured_mark = request.POST.get('10thsecuredmark')
        tenth_percentage = request.POST.get('10thcg')
        twelth_stream = request.POST.get('12thstream')
        twelth_college = request.POST.get('12thschool')
        twelth_board = request.POST.get('12thboard')
        twelth_full_mark = request.POST.get('12thfullmark')
        twelth_secured_mark = request.POST.get('12thsecuredmark')
        tewlth_percentage = request.POST.get('12thcg')
        degree_stream = request.POST.get('degstream')
        degree_college = request.POST.get('degschool')
        degree_university = request.POST.get('degboard')
        degree_full_mark = request.POST.get('degfullmark')
        degree_secured_mark = request.POST.get('degsecuremark')
        degree_percentage = request.POST.get('degcg')
        postdegree_stream = request.POST.get('pgdegstream')
        postdegree_college = request.POST.get('pgdegschool')
        postdegree_university = request.POST.get('pgdegboard')
        postdegree_full_mark = request.POST.get('pgdegfullmark')
        postdegree_secured_mark = request.POST.get('pgdegsecuremark')
        postdegree_percentage = request.POST.get('pgdegcg')
        user = Employee.objects.filter(id=obj.id).update(title=title,
        full_name=full_name,
        date_of_birth=date_of_birth,
        aadhar_no=aadhar_no,
        pan_no=pan_no,
        phone_no=phone_no,
        email=email,
        type_of_joining=type_of_joining,
        employee_department=department_obj,
        employee_designation=designation_obj,
        tenth_subjects=tenth_subjects,
        tenth_school=tenth_school,
        tenth_board=tenth_board,
        tenth_full_mark=tenth_full_mark,
        tenth_secured_mark=tenth_secured_mark,
        tenth_percentage=tenth_percentage,
        twelth_stream=twelth_stream,
        twelth_college=twelth_college,
        twelth_board=twelth_board,
        twelth_full_mark=twelth_full_mark,
        twelth_secured_mark=twelth_secured_mark,
        tewlth_percentage=tewlth_percentage,
        degree_stream=degree_stream,
        degree_college=degree_college,
        degree_university=degree_university,
        degree_full_mark=degree_full_mark,
        degree_secured_mark=degree_secured_mark,
        degree_percentage=degree_percentage,
        postdegree_stream=postdegree_stream,
        postdegree_college=postdegree_college,
        postdegree_university=postdegree_university,
        postdegree_full_mark=postdegree_full_mark,
        postdegree_secured_mark=postdegree_secured_mark,
        postdegree_percentage=postdegree_percentage,
        )
        user.save()
        return redirect(reverse_lazy('employee_list'))
    else:
        dept_queryset = Employee_Department.objects.all()
        desgn_queryset = Employee_Designation.objects.all()
        emp_queryset = Employee.objects.all()
        id_of_object = obj
        context = {
            'dept_queryset':dept_queryset,
            'desgn_queryset':desgn_queryset,
            'emp_queryset':emp_queryset,
            'id_of_object':id_of_object,
        }
        return render(request, 'dashboard/employee_edit.html', context)


def employee_delete(request, pk):
    obj = get_object_or_404(Employee, pk=pk)
    obj.delete()
    return redirect(reverse_lazy('employee_list'))
