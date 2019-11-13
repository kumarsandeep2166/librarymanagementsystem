from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import (Building, Floor, Room, Rack, Shelf,
                    Vendor, BookCategory, IssueType, Section, Subject, Language, Edition, Currency,
                    Store, Stock, Title, Author,BookIssueReturnStudent, Publisher, Department, BindingType, Category, SubCategory,
                    Entity, LibraryMapping, LibraryEntityMapping, Requisition, Requisition_Number)
from .forms import (BuildingForm, FloorForm, RoomForm, RackForm, ShelfForm, 
                    VendorForm,IssueTypeForm,StoreForm,SectionForm,BookCategoryForm, TitleForm,
                    AuthorForm, SubjectForm, DepartmentForm, PublisherForm, CategoryForm, SubCategoryForm,
                    BindingTypeForm,LanguageForm, EditionForm, CurrencyForm
                    )
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView, View
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.db import transaction
from django.db.models import Count
from django.db import connection
import json
from django.db.models import Q
from student.models import Student
from employee.models import Employee
from datetime import date, timedelta

def building_create(request):
    if request.method == "POST":
        name = request.POST.get('buildingname')
        user = Building(name=name)
        user.save()
        return redirect(reverse_lazy('building_list'))
    else:
        context={}
        return render(request,'dashboard/master3.html',context)

def building_edit(request, pk):
    obj = get_object_or_404(Building, pk=pk)
    buil_form = BuildingForm()
    if request.method == "POST":
        buil_name = request.POST.get('buildingname')
        user = Building.objects.filter(id=obj.id).update(name=buil_name)
        return redirect(reverse_lazy('building_list')) 
    else:
        buil_form = BuildingForm()
        buil_form.fields['name'].initial = obj.name
    context = {
        'buil_form':buil_form
    }
    return render(request,'dashboard/master3.html', context)

def building_delete(request, pk):
    user = get_object_or_404(Building, pk=pk)
    user.delete()
    return redirect(reverse('building_list'))

def building_list(request):
    shelf_queryset = Shelf.objects.all()
    rack_queryset = Rack.objects.all()
    biul_queryset = Building.objects.all()
    floor_queryset = Floor.objects.all()
    room_queryset = Room.objects.all()
    context={
        'shelf_queryset':shelf_queryset,
        'rack_queryset':rack_queryset,
        'room_queryset':room_queryset,
        'floor_queryset':floor_queryset,
        'biul_queryset':biul_queryset,  
    }
    return render(request,'dashboard/master3.html',context)


def floor_create(request):
    if request.method == "POST":
        name = request.POST.get('floorname')
        building = request.POST.getlist('building')
        building_obj = Building.objects.get(pk__in=building)
        user = Floor(name=name, building=building_obj)
        user.save()
        return redirect(reverse_lazy('floor_list'))
    else:
        context={}
        return render(request,'dashboard/master3.html',context)

def floor_edit(request, pk):
    obj = get_object_or_404(Floor, pk=pk)
    fl_form = FloorForm()
    if request.method == "POST":
        name = request.POST.get('fl_name')
        building = request.POST.get('fl_building')
        print(building, 'building name')
        building_obj = Building.objects.get(pk=building)
        user = Floor.objects.filter(id=obj.id).update(name=name, building=building_obj)
        return redirect(reverse_lazy('floor_list')) 
    else:
        fl_form = FloorForm()
        fl_form.fields['name'].initial = obj.name
        fl_form.fields['building'].initial = obj.building
    context = {
        'fl_form':fl_form
    }
    return render(request,'dashboard/master3.html', context)

def floor_delete(request, pk):
    user = get_object_or_404(Floor, pk=pk)
    user.delete()
    return redirect(reverse('floor_list'))

def floor_list(request):
    shelf_queryset = Shelf.objects.all()
    rack_queryset = Rack.objects.all()
    biul_queryset = Building.objects.all()
    floor_queryset = Floor.objects.all()
    room_queryset = Room.objects.all()
    context={
        'shelf_queryset':shelf_queryset,
        'rack_queryset':rack_queryset,
        'room_queryset':room_queryset,
        'floor_queryset':floor_queryset,
        'biul_queryset':biul_queryset,  
    }
    return render(request,'dashboard/master3.html',context)


def room_create(request):
    if request.method == "POST":
        name = request.POST.get('roomname')
        user = Room(name=name)
        user.save()
        return redirect(reverse_lazy('room_list'))
    else:
        context={}
        return render(request,'dashboard/master3.html',context)
def room_edit(request, pk):
    obj = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        name = request.POST.get('roomname')
        user = Room.objects.filter(id=obj.id).update(name=name)
        return redirect(reverse_lazy('room_list')) 
    else:
        form = RoomForm()
        form.fields['name'].initial = obj.name
    return render(request,'dashboard/master3.html')

def room_delete(request, pk):
    user = get_object_or_404(Room, pk=pk)
    user.delete()
    return redirect(reverse('room_list'))

def room_list(request):
    shelf_queryset = Shelf.objects.all()
    rack_queryset = Rack.objects.all()
    biul_queryset = Building.objects.all()
    floor_queryset = Floor.objects.all()
    room_queryset = Room.objects.all()
    context={
        'shelf_queryset':shelf_queryset,
        'rack_queryset':rack_queryset,
        'room_queryset':room_queryset,
        'floor_queryset':floor_queryset,
        'biul_queryset':biul_queryset,  
    }
    return render(request,'dashboard/master3.html',context)

def rack_create(request):
    if request.method == "POST":
        name = request.POST.get('rackname')
        room = request.POST.getlist('rackset')
        room_obj = Room.objects.get(pk__in=room)
        user = Rack(name=name, room=room_obj)
        user.save()
        return redirect(reverse_lazy('rack_list'))
    else:
        context={}
        return render(request,'dashboard/master3.html',context)

def rack_edit(request, pk):
    obj = get_object_or_404(Rack, pk=pk)
    if request.method == "POST":
        rack = request.POST.get('rackname')
        room = request.POST.get('roomname')
        room_obj = Room.objects.get(pk=room)
        user = Rack.objects.filter(id=obj.id).update(name=rack, room=room_obj)
        return redirect(reverse_lazy('rack_list')) 
    else:
        form = RackForm()
        form.fields['name'].initial = obj.name
        form.fields['room'].initial = obj.room
    return render(request,'dashboard/master3.html')

def rack_delete(request, pk):
    user = get_object_or_404(Rack, pk=pk)
    user.delete()
    return redirect(reverse('rack_list'))


def rack_list(request):
    shelf_queryset = Shelf.objects.all()
    rack_queryset = Rack.objects.all()
    biul_queryset = Building.objects.all()
    floor_queryset = Floor.objects.all()
    room_queryset = Room.objects.all()
    context={
        'shelf_queryset':shelf_queryset,
        'rack_queryset':rack_queryset,
        'room_queryset':room_queryset,
        'floor_queryset':floor_queryset,
        'biul_queryset':biul_queryset,  
    }
    return render(request,'dashboard/master3.html',context)

def shelf_create(request):
    if request.method == "POST":
        name = request.POST.get('shelf_name')
        rack = request.POST.getlist('shelfset')
        rack_obj = Rack.objects.get(pk__in=rack)
        user = Shelf(name=name, rack=rack_obj)
        user.save()
        return redirect(reverse_lazy('shelf_list'))
    else:
        context={}
        return render(request,'dashboard/master3.html',context)

def shelf_edit(request, pk):
    obj = get_object_or_404(Shelf, pk=pk)
    if request.method == "POST":
        shelf = request.POST.get('shelfname')
        rack = request.POST.get('rackname')
        rack_obj = Rack.objects.get(pk=rack)
        user = Rack.objects.filter(id=obj.id).update(name=shelf, rack=rack_obj)
        return redirect(reverse_lazy('shelf_list')) 
    else:
        form = ShelfForm()
        form.fields['name'].initial = obj.name
        form.fields['rack'].initial = obj.rack
    return render(request,'dashboard/master3.html')

def shelf_delete(request, pk):
    user = get_object_or_404(Shelf, pk=pk)
    user.delete()
    return redirect(reverse('shelf_list'))

def shelf_list(request):
    shelf_queryset = Shelf.objects.all()
    rack_queryset = Rack.objects.all()
    biul_queryset = Building.objects.all()
    floor_queryset = Floor.objects.all()
    room_queryset = Room.objects.all()
    context={
        'shelf_queryset':shelf_queryset,
        'rack_queryset':rack_queryset,
        'room_queryset':room_queryset,
        'floor_queryset':floor_queryset,
        'biul_queryset':biul_queryset,  
    }
    return render(request,'dashboard/master3.html',context)

def vendor_create(request):
    form = VendorForm()
    if request.method == 'POST':
        name_r = request.POST.get('VendorName')
        address_r = request.POST.get('Vendoraddress')
        contact_r = request.POST.get('VendorContact')
        email_r = request.POST.get('VendorEmail')
        gst_r = request.POST.get('VendorGst')
        pan_r = request.POST.get('VendorPan')
        tan_r = request.POST.get('VendorTan')
        cin_r = request.POST.get('VendorCin')
        image_r = request.POST.get('VendorImage')
        user = Vendor(name=name_r,address=address_r,contact=contact_r,
                        email=email_r,gst=gst_r,pan=pan_r,tan=tan_r,
                        cin=cin_r,image=image_r)
        user.save()
        # form = VendorForm(request.POST or None, request.FILES or None)
        # if form.is_valid():
        #     form.save()
        return redirect('vendor_list')
    else:        
        return render(request, 'dashboard/mastersetup1.html')

def vendor_delete(request, pk):
    user = get_object_or_404(Vendor, pk=pk)
    user.delete()
    return redirect(reverse('vendor_list'))

def vendor_update(request, pk):
    obj = get_object_or_404(Vendor, pk=pk)    
    if request.method == "POST":
        name_r = request.POST.get('VendorName')
        address_r = request.POST.get('Vendoraddress')
        contact_r = request.POST.get('VendorContact')
        email_r = request.POST.get('VendorEmail')
        gst_r = request.POST.get('VendorGst')
        pan_r = request.POST.get('VendorPan')
        tan_r = request.POST.get('VendorTan')
        cin_r = request.POST.get('VendorCin')
        image_r = request.POST.get('VendorImage')        
        user = Vendor.objects.filter(pk=obj.id).update(name=name_r,address=address_r,contact=contact_r,
                        email=email_r,gst=gst_r,pan=pan_r,tan=tan_r,
                        cin=cin_r,image=image_r)        
        
        return redirect('vendor_list')        
    else:
        form = VendorForm()
        form.fields['name'].initial = obj.name
        form.fields['address'].initial = obj.address
        form.fields['contact'].initial = obj.contact
        form.fields['email'].initial = obj.email
        form.fields['gst'].initial = obj.gst
        form.fields['pan'].initial = obj.pan
        form.fields['tan'].initial = obj.tan
        form.fields['cin'].initial = obj.cin
        form.fields['image'].initial = obj.image
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)

def vendor_list(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/mastersetup1.html', context)



def category_create(request):
    if request.method == "POST":
        name = request.POST.get('categoryname')
        user = Category(name=name)
        user.save()
        return redirect(reverse_lazy('category_list'))
    else:
        return render(request,'dashboard/mastersetup1.html')

def category_list(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/mastersetup1.html', context)

def category_update(request, pk):
    obj = get_object_or_404(Vendor, pk=pk)    
    if request.method == "POST":
        name_r = request.POST.get('categoryname')             
        user = Category.objects.filter(pk=obj.id).update(name=name_r)
        user.save()        
        return redirect('category_list')        
    else:
        form = CategoryForm()
        form.fields['name'].initial = obj.name
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)

def category_delete(request,pk):
    user = get_object_or_404(Category, pk=pk)
    user.delete()
    return redirect(reverse('category_list'))

def subcategory_create(request):
    if request.method == 'POST':
        name_r = request.POST.get('categoryname')
        main_category = request.POST.getlist('main_category_name')
        main_category_obj = Category.objects.get(pk__in=main_category)
        user = SubCategory(name=name_r,main_category=main_category_obj)
        user.save()
        # form = VendorForm(request.POST or None, request.FILES or None)
        # if form.is_valid():
        #     form.save()
        return redirect('subcategory_list')
    else:        
        return render(request, 'dashboard/mastersetup1.html')

def subcategory_list(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/mastersetup1.html', context)

def subcategory_update(request, pk):
    obj = get_object_or_404(SubCategory, pk=pk)
    if request.method == "POST":
        name_r = request.POST.get('subcategoryname')
        main_category = request.POST.getlist('maincategoryname')
        main_category_obj = Category.objects.get(pk__in=main_category)
        user = SubCategory.objects.filter(pk=obj.id).update(name=name_r, main_category=main_category_obj)
        return redirect(reverse_lazy('subcategory_list'))
    else:
        dept_queryset = Department.objects.all()
        pub_queryset = Publisher.objects.all()
        au_queryset = Author.objects.all()
        subjqueryset = Subject.objects.all()
        tqueryset = Title.objects.all()
        section_queryset = Section.objects.all()
        store_queryset = Store.objects.all()
        cqueryset = Category.objects.all()
        subqueryset = SubCategory.objects.all()
        bookqueryset = BookCategory.objects.all()
        iss_queryset = IssueType.objects.all()
        vqueryset = Vendor.objects.all()
        context = {
            'dept_queryset':dept_queryset,
            'pub_queryset':pub_queryset,
            'subjqueryset':subjqueryset,
            'tqueryset':tqueryset,
            'section_queryset':section_queryset,
            'store_queryset':store_queryset,
            'iss_queryset':iss_queryset,
            'bookqueryset':bookqueryset,
            'cqueryset':cqueryset,
            'subqueryset':subqueryset,
            'vqueryset':vqueryset,
            'au_queryset':au_queryset,
        }
        return render(request, 'dashboard/mastersetup1.html', context)

def subcategory_delete(request,pk):
    obj = get_object_or_404(SubCategory, pk=pk)
    obj.delete()
    return redirect(reverse_lazy('subcategory_list'))

def bookcategory_create(request):
    if request.method == 'POST':
        name_r = request.POST.get('bookcategory_name')
        main_category = request.POST.getlist('categoryset')
        category = request.POST.getlist('maincategoryset')
        main_category_obj = SubCategory.objects.get(pk__in=main_category)
        category_obj = Category.objects.get(pk__in=main_category)
        user = BookCategory(name=name_r,sub_category=main_category_obj, category=category_obj)
        user.save()
        # form = VendorForm(request.POST or None, request.FILES or None)
        # if form.is_valid():
        #     form.save()
        return redirect('bookcategory_list')
    else:
        dept_queryset = Department.objects.all()
        pub_queryset = Publisher.objects.all()
        au_queryset = Author.objects.all()
        subjqueryset = Subject.objects.all()
        tqueryset = Title.objects.all()
        section_queryset = Section.objects.all()
        store_queryset = Store.objects.all()
        cqueryset = Category.objects.all()
        subqueryset = SubCategory.objects.all()
        bookqueryset = BookCategory.objects.all()
        iss_queryset = IssueType.objects.all()
        vqueryset = Vendor.objects.all()
        context = {
            'dept_queryset':dept_queryset,
            'pub_queryset':pub_queryset,
            'subjqueryset':subjqueryset,
            'tqueryset':tqueryset,
            'section_queryset':section_queryset,
            'store_queryset':store_queryset,
            'iss_queryset':iss_queryset,
            'bookqueryset':bookqueryset,
            'cqueryset':cqueryset,
            'subqueryset':subqueryset,
            'vqueryset':vqueryset,
            'au_queryset':au_queryset,
        }     
        return render(request, 'dashboard/mastersetup1.html', context)

def bookcategory_list(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/mastersetup1.html', context)

def bookcategory_edit(request, pk):
    obj = get_object_or_404(BookCategory, pk=pk)
    if request.method == "POST":
        name_r = request.POST.get('bookcategoryname')
        sub_category = request.POST.getlist('categoryset')
        category = request.POST.getlist('maincategoryset')
        main_category_obj = SubCategory.objects.get(pk__in=sub_category)
        category_obj = Category.objects.get(pk__in=category)
        user = BookCategory.objects.filter(pk=obj.id).update(name=name_r, sub_category=main_category_obj, category=category_obj)
        return redirect(reverse_lazy('bookcategory_list'))
    else:
        dept_queryset = Department.objects.all()
        pub_queryset = Publisher.objects.all()
        au_queryset = Author.objects.all()
        subjqueryset = Subject.objects.all()
        tqueryset = Title.objects.all()
        section_queryset = Section.objects.all()
        store_queryset = Store.objects.all()
        cqueryset = Category.objects.all()
        subqueryset = SubCategory.objects.all()
        bookqueryset = BookCategory.objects.all()
        iss_queryset = IssueType.objects.all()
        vqueryset = Vendor.objects.all()
        context = {
            'dept_queryset':dept_queryset,
            'pub_queryset':pub_queryset,
            'subjqueryset':subjqueryset,
            'tqueryset':tqueryset,
            'section_queryset':section_queryset,
            'store_queryset':store_queryset,
            'iss_queryset':iss_queryset,
            'bookqueryset':bookqueryset,
            'cqueryset':cqueryset,
            'subqueryset':subqueryset,
            'vqueryset':vqueryset,
            'au_queryset':au_queryset,
        }
        return render(request, 'dashboard/mastersetup1.html', context)

def bookcategory_delete(request,pk):
    obj = get_object_or_404(BookCategory, pk=pk)
    obj.delete()
    return redirect(reverse_lazy('subcategory_list'))

def issuetype_create(request):
    if request.method == "POST":
        name = request.POST.get('issuetypename')
        user = IssueType(name=name)
        user.save()
        return redirect('issuetype_list')
    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)
    return render(request, 'dashboard/mastersetup1.html', context)

def issuetype_list(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/master1.html', context)

def issuetype_edit(request, pk):
    obj = get_object_or_404(IssueType, pk)
    if request.method == "POST":
        name = request.POST.get('issuetypename')
        user = IssueType.objects.filter(pk=obj.id).update(name=name)
        return redirect('issuetype_list')
    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)
    return render(request, 'dashboard/mastersetup1.html', context)

def issuetype_delete(request, pk):
    user = get_object_or_404(IssueType, pk=pk)
    user.delete()
    return redirect(reverse('issuetype_list'))

def store_create(request):
    if request.method == "POST":
        name = request.POST.get('storename')
        user = Store(name=name)
        user.save()
        return redirect('store_list')

    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)

def store_list(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/mastersetup1.html', context)

def store_edit(request, pk):
    if request.method == "POST":
        name = request.POST.get('storename')
        user = Store.objects.filter(pk=obj.id).update(name=name)
        return redirect('store_list')
    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)

def store_delete(request, pk):
    user = get_object_or_404(Store, pk=pk)
    user.delete()
    return redirect(reverse('store_list'))

def section_create(request):
    if request.method == "POST":
        name = request.POST.get('sectionname')
        user = Section(name=name)
        user.save()
        return redirect('section_list')
    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)

def section_list(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/mastersetup1.html', context)

def section_edit(request, pk):
    if request.method == "POST":
        name = request.POST.get('sectionname')
        user = Section.objects.filter(pk=obj.id).update(name=name)
        return redirect('section_list')
    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)

def section_delete(request, pk):
    user = get_object_or_404(Section, pk=pk)
    user.delete()
    return redirect(reverse('section_list'))

# def bookcategory_create(request):
#     if request.method == "POST":
#         name = request.POST.get('bookcategoryname')
#         user = BookCategory(name=name)
#         user.save()
#         return redirect('bookcategory_list')
#     else:
#         context = {}
#         return render(request, 'dashboard/master1.html', context)

# def bookcategory_list(request):
#     book_queryset = BookCategory.objects.all()
#     context = {
#         'book_queryset':book_queryset
#     }
#     return render(request, 'dashboard/mastersetup1.html', context)

# def bookcategory_edit(request, pk):
#     obj = get_object_or_404(BookCategory, pk=pk)
#     if request.method == "POST":
#         pass

# def bookcategory_delete(request, pk):
#     user = get_object_or_404(BookCategory, pk=pk)
#     user.delete()
#     return redirect(reverse('bookcategory_list'))

def title_create(request):
    if request.method == "POST":
        name = request.POST.get('titlename')
        user = Title(name=name)
        user.save()
        return redirect('title_list')
    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)
    return render(request, 'dashboard/mastersetup1.html', context)

def title_list(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/mastersetup1.html', context)

def title_edit(request, pk):
    obj = get_object_or_404(Title, pk=pk)
    if request.method == "POST":
        name = request.POST.get('titlename')
        user = Title.objects.filter(pk=obj.id).update(name=name)
        return redirect(reverse_lazy('title_list'))
    else:
        return render(request, 'dashboard/mastersetup1.html')

def title_delete(request, pk):
    user = get_object_or_404(Title, pk=pk)
    user.delete()
    return redirect(reverse('title_list'))


def subject_create(request):
    if request.method == "POST":
        name = request.POST.get('subjectname')
        user = Subject(name=name)
        user.save()
        return redirect('subject_list')
    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)

def subject_list(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/mastersetup1.html', context)

def subject_edit(request, pk):
    obj = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        name = request.POST.get('subjectname')
        user = Subject.objects.filter(pk=obj.id).update(name=name)
        user.save()
        return redirect('subject_list')
    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)

def subject_delete(request, pk):
    user = get_object_or_404(Subject, pk=pk)
    user.delete()
    return redirect(reverse('subject_list'))

def author_create(request):
    if request.method == "POST":
        name = request.POST.get('authorname')
        user = Author(name=name)
        user.save()
        return redirect('author_list')

    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)
    return render(request, 'dashboard/mastersetup1.html', context)

def author_list(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/mastersetup1.html', context)

def author_edit(request, pk):
    obj = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        name = request.POST.get('authorname')
        user = Author.objects.filter(pk=obj.id).update(name=name)
        return redirect(reverse_lazy('author_list'))
    else:
        return render(request, 'dashboard/mastersetup1.html')

def author_delete(request, pk):
    user = get_object_or_404(Author, pk=pk)
    user.delete()
    return redirect(reverse('author_list'))

def publisher_create(request):
    if request.method == "POST":
        name = request.POST.get('publishername')
        address = request.POST.get('publisheraddress')
        gst = request.POST.get('publishergst')
        user = Publisher(name=name, address=address, gst=gst)
        user.save()
        return redirect('publisher_list')
    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)
    return render(request, 'dashboard/mastersetup1.html', context)

def publisher_list(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/mastersetup1.html', context)

def publisher_edit(request,pk):
    obj = get_object_or_404(Publisher, pk=pk)
    if request.method == "POST":
        name = request.POST.get('publishername')
        address = request.POST.get('publisheraddress')
        gst = request.POST.get('publishergst')
        user = Publisher.objects.filter(pk=obj.id).update(name=name, address=address, gst=gst)
        user.save()
        return redirect('publisher_list')
    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)
    return render(request, 'dashboard/mastersetup1.html', context)

def publisher_delete(request, pk):
    user = get_object_or_404(Publisher, pk=pk)
    user.delete()
    return redirect(reverse('publisher_list'))

def department_create(request):
    if request.method == "POST":
        name = request.POST.get('deptname')
        user = Department(name=name)
        user.save()
        return redirect('department_list')
    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)

def department_list(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/mastersetup1.html', context)

def department_edit(request, pk):
    obj = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        name = request.POST.get('deptname')
        user = Department.objects.filter(pk=obj.id)(name=name)
        user.save()
        return redirect('department_list')
    else:
        context = {}
        return render(request, 'dashboard/mastersetup1.html', context)

def department_delete(request, pk):
    user = get_object_or_404(Department, pk=pk)
    user.delete()
    return redirect(reverse('department_list'))


def bindingtype_create(request):
    if request.method == "POST":
        name = request.POST.get('bindingtype')
        user = BindingType(name=name)
        user.save()
        return redirect(reverse_lazy('bindingtype_list'))
    else:
        context = {}
        return render(request, 'dashboard/mastersetup2.html', context)

def bindingtype_list(request):
    binding_queryset = BindingType.objects.all()
    ed_queryset = Edition.objects.all()
    curr_queryset = Currency.objects.all()    
    lang_queryset = Language.objects.all()
    context = {
        'binding_queryset':binding_queryset,
        'lang_queryset':lang_queryset,
        'ed_queryset':ed_queryset,
        'curr_queryset':curr_queryset,
    }
    return render(request, 'dashboard/mastersetup2.html', context)

def bindingtype_edit(request, pk):
    obj = get_object_or_404(BindingType, pk=pk)
    if request.method == "POST":
        name = request.POST.get('bindingtype')
        user = BindingType.objects.filter(id=obj.id).update(name=name)
        return redirect(reverse_lazy('bindingtype_list'))
    else:
        return render(request,'dashboard/mastersetup2.html')

def bindingtype_delete(request, pk):
    user = get_object_or_404(BindingType, pk=pk)
    user.delete()
    return redirect(reverse('bindingtype_list'))

def language_create(request):
    if request.method == "POST":
        name = request.POST.get('languagename')
        code = request.POST.get('languagecode')
        sequence = request.POST.get('languagesequence')
        user = Language(name=name, code=code, sequence=sequence)
        user.save()
        return redirect(reverse_lazy('language_list'))
    else:
        context = {}
        return render(request, 'dashboard/mastersetup2.html', context)

def language_list(request):
    ed_queryset = Edition.objects.all()
    curr_queryset = Currency.objects.all()    
    lang_queryset = Language.objects.all()
    context = {
        'lang_queryset':lang_queryset,
        'ed_queryset':ed_queryset,
        'curr_queryset':curr_queryset,
    }
    return render(request, 'dashboard/mastersetup2.html', context)

def language_edit(request, pk):
    obj = get_object_or_404(Language, pk=pk)
    if request.method == "POST":
        name = request.POST.get('languagename')
        code = request.POST.get('languagecode')
        sequence = request.POST.get('languagesequence')
        user = Language.objects.filter(pk=obj.pk).update(name=name, code=code, sequence=sequence)
        return redirect(reverse_lazy('language_list'))
    else:
        return render(request, 'dashboard/mastersetup2.html')

def language_delete(request, pk):
    user = get_object_or_404(Language, pk=pk)
    user.delete()
    return redirect(reverse('language_list'))

def edition_create(request):
    if request.method == "POST":
        name = request.POST.get('edition')
        user = Edition(name=name)
        user.save()
        return redirect(reverse_lazy('edition_list'))
    else:
        context = {}
        return render(request, 'dashboard/mastersetup2.html', context)

def edition_list(request):
    ed_queryset = Edition.objects.all()
    curr_queryset = Currency.objects.all()
    context = {
        'ed_queryset':ed_queryset,
        'curr_queryset':curr_queryset,
    }
    return render(request, 'dashboard/mastersetup2.html', context)

def edition_edit(request, pk):
    obj = get_object_or_404(Edition, pk=pk)
    if request.method == "POST":
        name = request.POST.get('edition')
        user = Edition.objects.filter(pk=obj.id).update(name=name)
        return redirect(reverse_lazy('edition_list'))
    else:
        return render(request, 'dashboard/mastersetup2.html')

def edition_delete(request, pk):
    user = get_object_or_404(Edition, pk=pk)
    user.delete()
    return redirect(reverse('edition_list'))

def currency_create(request):
    if request.method == "POST":
        name = request.POST.get('currencyname')
        code = request.POST.get('currencycode')
        sequence = request.POST.get('currencysequence')
        user = Currency(name=name, code=code, sequence=sequence)
        user.save()
        return redirect(reverse_lazy('currency_list'))
    else:
        context = {}
        return render(request, 'dashboard/mastersetup2.html', context)

def currency_list(request):
    curr_queryset = Currency.objects.all()
    context = {
        'curr_queryset':curr_queryset
    }
    return render(request, 'dashboard/mastersetup2.html', context)

def currency_edit(request, pk):
    obj = get_object_or_404(Currency, pk=pk)
    if request.method == "POST":
        name = request.POST.get('currencyname')
        code = request.POST.get('currencycode')
        sequence = request.POST.get('currencysequence')
        user = Currency.objects.filter(pk=obj.id).update(name=name, code=code, sequence=sequence)
        return redirect(reverse_lazy('currency_list'))
    else:
        context = {}
        return render(request, 'dashboard/mastersetup2.html', context)

def currency_delete(request, pk):
    user = get_object_or_404(Currency, pk=pk)
    user.delete()
    return redirect(reverse('currency_list'))

def mastersetup1(request):
    dept_queryset = Department.objects.all()
    pub_queryset = Publisher.objects.all()
    au_queryset = Author.objects.all()
    subjqueryset = Subject.objects.all()
    tqueryset = Title.objects.all()
    section_queryset = Section.objects.all()
    store_queryset = Store.objects.all()
    cqueryset = Category.objects.all()
    subqueryset = SubCategory.objects.all()
    bookqueryset = BookCategory.objects.all()
    iss_queryset = IssueType.objects.all()
    vqueryset = Vendor.objects.all()
    context = {
        'dept_queryset':dept_queryset,
        'pub_queryset':pub_queryset,
        'subjqueryset':subjqueryset,
        'tqueryset':tqueryset,
        'section_queryset':section_queryset,
        'store_queryset':store_queryset,
        'iss_queryset':iss_queryset,
        'bookqueryset':bookqueryset,
        'cqueryset':cqueryset,
        'subqueryset':subqueryset,
        'vqueryset':vqueryset,
        'au_queryset':au_queryset,
    }
    return render(request, 'dashboard/mastersetup1.html', context)

def mastersetup2(request):
    binding_queryset = BindingType.objects.all()
    ed_queryset = Edition.objects.all()
    curr_queryset = Currency.objects.all()    
    lang_queryset = Language.objects.all()
    context = {
        'binding_queryset':binding_queryset,
        'lang_queryset':lang_queryset,
        'ed_queryset':ed_queryset,
        'curr_queryset':curr_queryset,
    }
    return render(request, 'dashboard/mastersetup2.html', context)

def mastersetup3(request):
    shelf_queryset = Shelf.objects.all()
    rack_queryset = Rack.objects.all()
    biul_queryset = Building.objects.all()
    floor_queryset = Floor.objects.all()
    room_queryset = Room.objects.all()
    context={
        'shelf_queryset':shelf_queryset,
        'rack_queryset':rack_queryset,
        'room_queryset':room_queryset,
        'floor_queryset':floor_queryset,
        'biul_queryset':biul_queryset,  
    }
    return render(request, 'dashboard/master3.html', context)



def entity_type_create(request):
    if request.method == "POST":
        name = request.POST.get('entname')
        user = Entity(name=name)
        user.save()
        return redirect(reverse_lazy('entity_type_list'))
    else:
        en_queryset = Entity.objects.all()
        context = {
            'en_queryset':en_queryset
        }
        return render(request, 'dashboard/entity_type.html')

def entity_type_list(request):
    en_queryset = Entity.objects.all()
    context = {
        'en_queryset':en_queryset
    }
    return render(request, 'dashboard/entity_type.html', context)

def entity_type_edit(request, pk):
    obj = get_object_or_404(Entity, pk=pk)
    if request.method == "POST":
        name = request.POST.get('entname')
        user = Entity.objects.filter(pk=obj.id).update(name=name)
        return redirect(reverse_lazy('entity_type_list'))
    return render(request, 'dashboard/entity_type.html')

def entity_type_delete(request, pk):
    obj = get_object_or_404(Entity, pk=pk)
    obj.delete()
    return redirect(reverse_lazy('entity_type_list'))

def library_mapping_create(request):
    if request.method == "POST":
        store = request.POST.getlist('storename_1')
        store_obj = Store.objects.get(pk__in=store)
        section = request.POST.getlist('section_1')
        section_obj = Section.objects.get(pk__in=section)
        book_category = request.POST.getlist('book_category')
        book_category_obj = BookCategory.objects.get(pk__in=book_category)
        abbr = request.POST.get('abbr123')
        sequence = request.POST.get('sequence1234')
        user = LibraryMapping(store=store_obj, section=section_obj, book_category=book_category_obj, abbr=abbr, sequence=sequence)
        user.save()    
        return redirect(reverse_lazy('library_mapping_list'))
    else:
        sto_queryset = Store.objects.all()
        sec_queryset = Section.objects.all()
        book_cat_queryset = BookCategory.objects.all()
        map_queryset = LibraryMapping.objects.all()
        context = {
            'sto_queryset':sto_queryset,
            'sec_queryset':sec_queryset,
            'book_cat_queryset':book_cat_queryset,
            'map_queryset':map_queryset,
        }
        return render(request, 'dashboard/library_assign.html',context)

def library_mapping_list(request):
    map_queryset = LibraryMapping.objects.all()
    issue_type_book = IssueType.objects.all()
    sto_queryset = Store.objects.all()
    sec_queryset = Section.objects.all()
    book_cat_queryset = BookCategory.objects.all()
    entity_type = Entity.objects.all()
    context = {
        'map_queryset':map_queryset,
        'sto_queryset':sto_queryset,
        'sec_queryset':sec_queryset,
        'book_cat_queryset':book_cat_queryset,
        'entity_type':entity_type,
        'issue_type_book':issue_type_book,
        'book_cat_queryset':book_cat_queryset,
    }
    return render(request, 'dashboard/library_assign.html', context)

def library_mapping_edit(request, pk):
    obj = get_object_or_404(LibraryMapping, pk=pk)
    if request.method == "POST":
        store = request.POST.getlist('storetype')
        store_obj = Store.objects.get(pk__in=store)
        section = request.POST.getlist('sectiontype')
        section_obj = Section.objects.get(pk__in=section)
        book_category = request.POST.getlist('bookcategorytype')
        book_category_obj = BookCategory.objects.get(pk__in=book_category)
        abbr = request.POST.get('abbras')
        sequence = request.POST.get('sequenceins')
        user = LibraryMapping.objects.filter(id=obj.id).update(store=store_obj,section=section_obj,
                    book_category=book_category_obj,abbr=abbr,sequence=sequence)
        return redirect(reverse_lazy('library_mapping_list'))
    else:
        map_queryset = LibraryMapping.objects.all()
        sto_queryset = Store.objects.all()
        sec_queryset = Section.objects.all()
        book_cat_queryset = BookCategory.objects.all()
        context = {
        'map_queryset':map_queryset,
        'sto_queryset':sto_queryset,
        'sec_queryset':sec_queryset,
        'book_cat_queryset':book_cat_queryset
        }
        return render(request, 'dashboard/library_assign.html', context)

def library_mapping_delete(request, pk):
    obj = get_object_or_404(LibraryMapping, pk)
    obj.delete()
    return redirect(reverse_lazy('library_mapping_list'))

def library_entity_mapping_create(request):
    if request.method == "POST":
        entity = request.POST.getlist('entity_name')
        entity_obj = Entity.objects.get(pk__in=entity)
        issue_type = request.POST.getlist('issuetype_book')
        issue_type_obj = IssueType.objects.get(pk__in=issue_type)
        num_of_books = request.POST.get('numberofbooks')
        max_days = request.POST.get('numberofdays')
        user = LibraryEntityMapping(entity=entity_obj,issue_type=issue_type_obj,num_of_books=num_of_books,max_days=max_days)
        user.save()
        return redirect(reverse_lazy('library_entity_mapping_list'))
    else:
        lemap_queryset = LibraryEntityMapping.objects.all()
        entity_type = Entity.objects.all()
        issue_type_book = IssueType.objects.all()
        sto_queryset = Store.objects.all()
        sec_queryset = Section.objects.all()
        book_cat_queryset = BookCategory.objects.all()
        context = {
            'lemap_queryset':lemap_queryset,
            'entity_type':entity_type,
            'sto_queryset':sto_queryset,
            'sec_queryset':sec_queryset,
            'book_cat_queryset':book_cat_queryset,
            'issue_type_book':issue_type_book
        }
        return render(request, 'dashboard/library_assign.html', context)

def library_entity_mapping_list(request):
    lemap_queryset = LibraryEntityMapping.objects.all()
    lamap_queryset = LibraryMapping.objects.all()
    entity_type = Entity.objects.all()
    issue_type_book = IssueType.objects.all()
    sto_queryset = Store.objects.all()
    sec_queryset = Section.objects.all()
    book_cat_queryset = BookCategory.objects.all()
    context = {
        'lemap_queryset':lemap_queryset,
        'lamap_queryset':lamap_queryset,
        'entity_type':entity_type,
        'sto_queryset':sto_queryset,
        'sec_queryset':sec_queryset,
        'book_cat_queryset':book_cat_queryset,
        'issue_type_book':issue_type_book
    }
    return render(request, 'dashboard/library_assign.html', context)

def library_entity_mapping_edit(request, pk):
    obj = get_object_or_404(LibraryEntityMapping, pk=pk)
    if request.method == "POST":
        mapping = request.POST.getlist('ssientity')
        mapping_obj = LibraryMapping.objects.get(pk__in=mapping)
        entity = request.POST.getlist('entity_name')
        entity_obj = Entity.objects.get(pk__in=entity)
        issue_type = request.POST.getlist('issuetype_book')
        issue_type_obj = IssueType.objects.get(pk__in=issue_type)
        num_of_books = request.POST.get('numberofbooks')
        max_days = request.POST.get('numberofdays')
        user = LibraryEntityMapping.objects.filter(id=obj.id).update(mapping=mapping_obj,entity=entity_obj,issue_type=issue_type_obj,num_of_books=num_of_books,max_days=max_days)
    else:
        lemap_queryset = LibraryEntityMapping.objects.all()
        lamap_queryset = LibraryMapping.objects.all()
        entity_type = Entity.objects.all()
        issue_type_book = IssueType.objects.all()
        sto_queryset = Store.objects.all()
        sec_queryset = Section.objects.all()
        book_cat_queryset = BookCategory.objects.all()
        context = {
            'lemap_queryset':lemap_queryset,
            'lamap_queryset':lamap_queryset,
            'entity_type':entity_type,
            'issue_type_book':issue_type_book,
            'sto_queryset':sto_queryset,
            'sec_queryset':sec_queryset,
            'book_cat_queryset':book_cat_queryset,            
        }
        return render(request, 'dashboard/library_assign.html', context)

def library_entity_mapping_delete(request, pk):
    obj = get_object_or_404(LibraryEntityMapping, pk=pk)
    obj.delete()
    return redirect(reverse_lazy('library_entity_mapping_list'))

def requisiton_create(request):
    if request.method == "POST":
        vendor = request.POST.getlist('vendernm')
        vendor_obj = Vendor.objects.get(pk__in=vendor)
        reqno = request.POST.get('reqno')
        reqdate = request.POST.get('reqdate')
        user = Requisition_Number(vendor=vendor_obj, requisition_num=reqno, date=reqdate)
        user.save()
        return redirect(reverse_lazy('requisiton_list'))
    else:
        v_queryset = Vendor.objects.all()
        re_queryset = Requisition_Number.objects.all()
        t_queryset = Title.objects.all()
        pub_queryset = Publisher.objects.all()
        au1_queryset = Author.objects.all()
        au2_queryset = Author.objects.all()
        au3_queryset = Author.objects.all()
        au4_queryset = Author.objects.all()
        au5_queryset = Author.objects.all()
        ed_queryset = Edition.objects.all()
        bin_queryset = BindingType.objects.all()
        la_queryset = Language.objects.all()
        context = {
            'v_queryset':v_queryset,
            're_queryset':re_queryset,
            't_queryset':t_queryset,
            'pub_queryset':pub_queryset,
            'au1_queryset':au1_queryset,
            "au2_queryset" :au2_queryset,
            'au3_queryset':au3_queryset,
            'au4_queryset':au4_queryset,
            'au5_queryset':au5_queryset,
            'bin_queryset':bin_queryset,
            'ed_queryset':ed_queryset,
            'la_queryset':la_queryset,
        }
        return render(request, 'dashboard/requisition.html', context)


def requisiton_list(request):
    v_queryset = Vendor.objects.all()
    re_queryset = Requisition_Number.objects.all()
    t_queryset = Title.objects.all()
    pub_queryset = Publisher.objects.all()
    au1_queryset = Author.objects.all()
    au2_queryset = Author.objects.all()
    au3_queryset = Author.objects.all()
    au4_queryset = Author.objects.all()
    au5_queryset = Author.objects.all()
    ed_queryset = Edition.objects.all()
    bin_queryset = BindingType.objects.all()
    la_queryset = Language.objects.all()
    context = {
        'v_queryset':v_queryset,
        're_queryset':re_queryset,
        't_queryset':t_queryset,
        'pub_queryset':pub_queryset,
        'au1_queryset':au1_queryset,
        "au2_queryset" :au2_queryset,
        'au3_queryset':au3_queryset,
        'au4_queryset':au4_queryset,
        'au5_queryset':au5_queryset,
        'bin_queryset':bin_queryset,
        'ed_queryset':ed_queryset,
        'la_queryset':la_queryset,
    }
    return render(request, 'dashboard/requisition.html', context)

class RequisitionCreateView(View):
    def get(self, request, pk, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass

def items_add_requisition(request, pk):
    obj = get_object_or_404(Requisition_Number, pk=pk)
    print(obj)
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        title = request.POST.get('title')
        title_obj = Title.objects.get(pk=title)
        publisher = request.POST.get('publisher')
        publisher_obj = Publisher.objects.get(pk=publisher)
        author1 = request.POST.get('author_1')
        author1_obj = Author.objects.get(pk=author1)
        author2 = request.POST.get('author_2')
        author2_obj = Author.objects.get(pk=author2)
        author3 = request.POST.get('author_3')
        author3_obj = Author.objects.get(pk=author3)
        edition = request.POST.get('edition')
        edition_obj = Edition.objects.get(pk=edition)
        bindingtype = request.POST.get('bindingtype')
        bindingtype_obj = BindingType.objects.get(pk=bindingtype)
        language = request.POST.get('language')
        language_obj = Language.objects.get(pk=language)
        pubyear = request.POST.get('pubyear')
        copies = request.POST.get('copies')
        author6 = request.POST.get('author6')
        author7 = request.POST.get('author7')
        author8 = request.POST.get('author8')
        publisher1 = request.POST.get('publisher1')
        user = Requisition(requisition=obj,book_name=book_name,title=title_obj,publisher=publisher_obj,no_of_copies=copies,
                            author1=author1_obj,author2=author2_obj,author3=author3_obj,edition=edition_obj,
                            binding_type=bindingtype_obj,language=language_obj, publication_year=pubyear,author6=author6,author7=author7,author8=author8,publisher1=publisher1 )
        user.save()
        return redirect(reverse_lazy('items_add_requisition_list'))
    else:
        t_queryset = Title.objects.all()
        pub_queryset = Publisher.objects.all()
        au1_queryset = Author.objects.all()
        au2_queryset = Author.objects.all()
        au3_queryset = Author.objects.all()
        au4_queryset = Author.objects.all()
        au5_queryset = Author.objects.all()
        ed_queryset = Edition.objects.all()
        bin_queryset = BindingType.objects.all()
        v_queryset = Vendor.objects.all()
        re_queryset = Requisition.objects.all()
        la_queryset = Language.objects.all()
        id_of_object = obj
        context = {
            'id_of_object':id_of_object,
            'v_queryset':v_queryset,
            're_queryset':re_queryset,
            't_queryset':t_queryset,
            'pub_queryset':pub_queryset,
            'au1_queryset':au1_queryset,
            "au2_queryset" :au2_queryset,
            'au3_queryset':au3_queryset,
            'au4_queryset':au4_queryset,
            'au5_queryset':au5_queryset,
            'bin_queryset':bin_queryset,
            'ed_queryset':ed_queryset,
            'la_queryset':la_queryset,
        }
        return render(request, 'dashboard/requisition.html', context)

def items_add_requisition_list(request):
    t_queryset = Title.objects.all()
    pub_queryset = Publisher.objects.all()
    au1_queryset = Author.objects.all()
    au2_queryset = Author.objects.all()
    au3_queryset = Author.objects.all()
    au4_queryset = Author.objects.all()
    au5_queryset = Author.objects.all()
    ed_queryset = Edition.objects.all()
    bin_queryset = BindingType.objects.all()
    v_queryset = Vendor.objects.all()
    re_queryset = Requisition.objects.all()
    la_queryset = Language.objects.all()
    context = {
        'v_queryset':v_queryset,
        're_queryset':re_queryset,
        't_queryset':t_queryset,
        'pub_queryset':pub_queryset,
        'au1_queryset':au1_queryset,
        "au2_queryset" :au2_queryset,
        'au3_queryset':au3_queryset,
        'au4_queryset':au4_queryset,
        'au5_queryset':au5_queryset,
        'bin_queryset':bin_queryset,
        'ed_queryset':ed_queryset,
        'la_queryset':la_queryset,
    }
    return render(request, 'dashboard/requisition_list.html', context)

def items_add_to_stock(request):
    return render(request, 'dashboard/add_item_to_stock.html')

def manual_stock_entry_create(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        title = request.POST.get('title')
        title_obj = Title.objects.get(pk=title)
        publisher = request.POST.get('publisher')
        publisher_obj = Publisher.objects.get(pk=publisher)
        author1 = request.POST.get('author_1')
        author1_obj = Author.objects.get(pk=author1)
        author2 = request.POST.get('author_2')
        author2_obj = Author.objects.get(pk=author2)
        author3 = request.POST.get('author_3')
        author3_obj = Author.objects.get(pk=author3)
        edition = request.POST.get('edition')
        edition_obj = Edition.objects.get(pk=edition)
        bindingtype = request.POST.get('bindingtype')
        bindingtype_obj = BindingType.objects.get(pk=bindingtype)
        language = request.POST.get('language')
        language_obj = Language.objects.get(pk=language)
        subject = request.POST.get('subject')
        subject_obj = Subject.objects.get(pk=subject)
        copies = request.POST.get('copies')
        book_category = request.POST.get('book_cat')
        book_category_obj = BookCategory.objects.get(pk=book_category)
        isbn = request.POST.get('isbn')
        barcode = request.POST.get('barcode')
        accn = request.POST.get('accn')
        book_num = request.POST.get('book_num')
        issuetype = request.POST.get('issuetype')
        issuetype_obj = IssueType.objects.get(pk=issuetype)
        store = request.POST.get('store')
        store_obj = Store.objects.get(pk=store)
        requisition = request.POST.get('requisition')
        requisition_obj = Requisition_Number.objects.get(pk=requisition)
        user = Stock(name=book_name,
                    title=title_obj,
                    publisher=publisher_obj,
                    author1=author1_obj,
                    author2=author2_obj,
                    author3=author3_obj,
                    edition=edition_obj,
                    binding_type=bindingtype_obj,
                    language=language_obj,
                    availablity=1,
                    ISBN=isbn,
                    subject=subject_obj,
                    store=store_obj,
                    issue_type=issuetype_obj,
                    book_category=book_category_obj,
                    requisition=requisition_obj,
                    barcode=barcode,
                    book_no=book_num,
                    acc_no=accn,
                    )
        user.save()
        return redirect(reverse_lazy('manual_stock_entry_list'))
    else:
        t_queryset = Title.objects.all()
        pub_queryset = Publisher.objects.all()
        au1_queryset = Author.objects.all()
        au2_queryset = Author.objects.all()
        au3_queryset = Author.objects.all()
        au4_queryset = Author.objects.all()
        au5_queryset = Author.objects.all()
        ed_queryset = Edition.objects.all()
        bin_queryset = BindingType.objects.all()
        v_queryset = Vendor.objects.all()
        re_queryset = Requisition.objects.all()
        la_queryset = Language.objects.all()
        issue_queryset = IssueType.objects.all()
        book_queryset = BookCategory.objects.all()
        sto_queryset = Store.objects.all()
        sub_queryset = Subject.objects.all()
        req_queryset = Requisition_Number.objects.all()
        context = {
            'v_queryset':v_queryset,
            're_queryset':re_queryset,
            't_queryset':t_queryset,
            'pub_queryset':pub_queryset,
            'au1_queryset':au1_queryset,
            "au2_queryset" :au2_queryset,
            'au3_queryset':au3_queryset,
            'au4_queryset':au4_queryset,
            'au5_queryset':au5_queryset,
            'bin_queryset':bin_queryset,
            'ed_queryset':ed_queryset,
            'la_queryset':la_queryset,
            'issue_queryset':issue_queryset,
            'book_queryset':book_queryset,
            'sto_queryset':sto_queryset,
            'sub_queryset':sub_queryset,
            'req_queryset':req_queryset,
        }
        return render(request, 'dashboard/manual_entry_stock.html', context)

def manual_stock_entry_list(request):
    t_queryset = Title.objects.all()
    pub_queryset = Publisher.objects.all()
    au1_queryset = Author.objects.all()
    au2_queryset = Author.objects.all()
    au3_queryset = Author.objects.all()
    au4_queryset = Author.objects.all()
    au5_queryset = Author.objects.all()
    ed_queryset = Edition.objects.all()
    bin_queryset = BindingType.objects.all()
    v_queryset = Vendor.objects.all()
    re_queryset = Requisition.objects.all()
    la_queryset = Language.objects.all()
    issue_queryset = IssueType.objects.all()
    book_queryset = BookCategory.objects.all()
    sto_queryset = Store.objects.all()
    stock_queryset = Stock.objects.all()
    req_queryset = Requisition_Number.objects.all()
    context = {
        'v_queryset':v_queryset,
        're_queryset':re_queryset,
        't_queryset':t_queryset,
        'pub_queryset':pub_queryset,
        'au1_queryset':au1_queryset,
        "au2_queryset" :au2_queryset,
        'au3_queryset':au3_queryset,
        'au4_queryset':au4_queryset,
        'au5_queryset':au5_queryset,
        'bin_queryset':bin_queryset,
        'ed_queryset':ed_queryset,
        'la_queryset':la_queryset,
        'issue_queryset':issue_queryset,
        'book_queryset':book_queryset,
        'sto_queryset':sto_queryset,
        'stock_queryset':stock_queryset,
        'req_queryset':req_queryset,
    }
    return render(request, 'dashboard/manual_stock_list.html', context)

def manual_stock_entry_edit(request, pk):
    obj = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        title = request.POST.get('title')
        title_obj = Title.objects.get(pk=title)
        publisher = request.POST.get('publisher')
        publisher_obj = Publisher.objects.get(pk=publisher)
        author1 = request.POST.get('author_1')
        author1_obj = Author.objects.get(pk=author1)
        author2 = request.POST.get('author_2')
        author2_obj = Author.objects.get(pk=author2)
        author3 = request.POST.get('author_3')
        author3_obj = Author.objects.get(pk=author3)
        edition = request.POST.get('edition')
        edition_obj = Edition.objects.get(pk=edition)
        bindingtype = request.POST.get('bindingtype')
        bindingtype_obj = BindingType.objects.get(pk=bindingtype)
        language = request.POST.get('language')
        language_obj = Language.objects.get(pk=language)
        copies = request.POST.get('copies')
        subject = request.POST.get('subject')
        subject_obj = Subject.objects.get(pk=subject)
        copies = request.POST.get('copies')
        book_category = request.POST.get('book_cat')
        book_category_obj = BookCategory.objects.get(pk=book_category)
        isbn = request.POST.get('isbn')
        issuetype = request.POST.get('issuetype')
        issuetype_obj = IssueType.objects.get(pk=issuetype)
        store = request.POST.get('store')
        store_obj = Store.objects.get(pk=store)
        user = Stock.objects.filter(id=obj.id).update(
                            name=book_name,
                            title=title_obj,
                            publisher=publisher_obj,
                            no_of_copies=copies,
                            author1=author1_obj,
                            author2=author2_obj,
                            author3=author3_obj,
                            edition=edition_obj,
                            binding_type=bindingtype_obj,
                            language=language_obj,
                            availablity=1,
                            ISBN=isbn,
                            subject=subject_obj,
                            store=store_obj,
                            issue_type=issuetype_obj,
                            book_category=book_category_obj,
                            )
        return redirect(reverse_lazy('manual_stock_entry_list'))
    else:
        t_queryset = Title.objects.all()
        pub_queryset = Publisher.objects.all()
        au1_queryset = Author.objects.all()
        au2_queryset = Author.objects.all()
        au3_queryset = Author.objects.all()
        au4_queryset = Author.objects.all()
        au5_queryset = Author.objects.all()
        ed_queryset = Edition.objects.all()
        bin_queryset = BindingType.objects.all()
        v_queryset = Vendor.objects.all()
        re_queryset = Requisition.objects.all()
        la_queryset = Language.objects.all()
        issue_queryset = IssueType.objects.all()
        book_queryset = BookCategory.objects.all()
        sto_queryset = Store.objects.all()
        sub_queryset = Subject.objects.all()
        context = {
            'v_queryset':v_queryset,
            're_queryset':re_queryset,
            't_queryset':t_queryset,
            'pub_queryset':pub_queryset,
            'au1_queryset':au1_queryset,
            "au2_queryset" :au2_queryset,
            'au3_queryset':au3_queryset,
            'au4_queryset':au4_queryset,
            'au5_queryset':au5_queryset,
            'bin_queryset':bin_queryset,
            'ed_queryset':ed_queryset,
            'la_queryset':la_queryset,
            'issue_queryset':issue_queryset,
            'book_queryset':book_queryset,
            'sto_queryset':sto_queryset,
            'sub_queryset':sub_queryset,
        }
        return render(request, 'dashboard/manual_stock_entry_edit.html', context)

def manual_stock_entry_delete(request, pk):
    obj = get_object_or_404(Stock, pk=pk)
    obj.delete()
    return redirect(reverse_lazy('manual_stock_entry_list'))

def acquisition(request):
    return render(request, 'dashboard/acquisition.html')

def load_books(request):
    req_num = request.GET.get('req_number')
    req_obj = Requisition_Number.objects.get(requisition_num=req_num)
    main_obj = Requisition.objects.filter(requisition=req_obj.id)
    main_obj_count = main_obj.count()
    main_obj_list = []
    for obj in main_obj:
        main_obj_dict = {}
        main_obj_dict['req_id'] = obj.id
        main_obj_dict['book_name'] = obj.book_name
        main_obj_dict['no_of_copies'] = int(obj.no_of_copies)
        main_obj_dict['publisher'] = obj.publisher.name
        main_obj_dict['title'] = obj.title.name
        main_obj_dict['author1'] = obj.author1.name
        main_obj_dict['author2'] = obj.author2.name
        main_obj_dict['author3'] = obj.author3.name
        main_obj_dict['count_of_objects'] = main_obj_count
        main_obj_dict['req_num'] = req_num        
        main_obj_list.append(main_obj_dict)
    requisition_json = json.dumps({'main_obj_list': main_obj_list})
    return HttpResponse(requisition_json, 'application/json')

def acquisition_form(request, num):
    req_number = request.GET.get('req_number')
    req_obj = Requisition_Number.objects.get(requisition_num=req_number)
    main_obj = Requisition.objects.filter(requisition=req_obj.id)
    num_loop = int(num)
    print(num_loop)
    print(req_number)
    context = {
        'num_loop':range(num_loop),
        'main_obj':main_obj,
    }
    return render(request, 'dashboard/acquisition_form.html', context)


def create_books(request):
    total = request.GET.get('total')
    num_loop = request.GET.get('no_of_times')

    context = {
        'num_loop':num_loop,
    }
    return HttpResponse('Suxxessfull')

def get_books_name(request):
    total = request.POST.get('no_of_time')
    req_number = request.POST.get('req_number')
    req_obj = Requisition_Number.objects.get(requisition_num=req_num)
    main_obj = Requisition.objects.filter(requisition=req_obj.id)
    print("main objects is:",main_obj)
    main_obj_count = main_obj.count()
    main_obj_list = []
    for obj in main_obj:
        main_obj_dict = {}
        main_obj_dict['req_id'] = obj.id
        main_obj_dict['book_name'] = obj.book_name
        main_obj_dict['count_of_objects'] = main_obj_count
        main_obj_dict['req_num'] = req_number
        main_obj_list.append(main_obj_dict)
    requisition_json = json.dumps({'main_obj_list': main_obj_list})
    return HttpResponse(requisition_json, 'application/json')

def library_book_issue(request):
    return render(request, 'dashboard/book_issue_return.html')

def autocompletesearchbooksbyaccn(request):
    data = request.POST.get('term')
    books = Stock.objects.filter(Q(acc_no__icontains=data))
    results = []
    for i in books:
        book_json = {}
        book_json['id'] = i.id
        book_json['availablity'] = i.availablity
        book_json['barcode'] = i.barcode
        book_json['title'] = i.title.name
        book_json['acc_no'] = i.acc_no
        book_json['name'] = i.name
        results.append(book_json)
    else:
        book_json = {}
        book_json['id'] = i.id
        book_json['availablity'] = i.availablity
        book_json['barcode'] = i.barcode
        book_json['title'] = i.title.name
        book_json['acc_no'] = i.acc_no
        book_json['name'] = i.name
        results.append(book_json)
    data = json.dumps(results)
    mimetype = 'application/json'    
    return HttpResponse(data, mimetype)

def getBookByAccn(request):
    accn_no = request.GET.get('accn_no')
    accn_no_obj = Stock.objects.get(pk=accn_no)
    print(accn_no_obj)
    data = json.dumps(accn_no_obj)
    mimetype = 'application/json'    
    return HttpResponse(data, mimetype)

def student_autocomplete(request):
    data = request.POST.get('stud_term')
    students = Student.objects.filter(Q(id__icontains=data))
    results = []
    for i in students:
        stu_json = {}
        stu_json['id'] = i.id
        stu_json['full_name'] = i.full_name
        results.append(stu_json)
    else:
        stu_json = {}
        stu_json['id'] = i.id
        stu_json['full_name'] = i.full_name
        results.append(stu_json)
    data = json.dumps(results)
    mimetype = 'application/json'    
    return HttpResponse(data, mimetype)   

def get_student_book_list(request):
    student_id = request.GET.get('student_id')
    stud_obj = Student.objects.get(enr_id=student_id)
    print(stud_obj)
    student_name = stud_obj.full_name
    print(student_name)
    books_issued = BookIssueReturnStudent.objects.filter(student=stud_obj.id)
    print(books_issued)
    # book_id = books_issued.id
    # book_name = books_issued.book_accn_no.name
    # book_accn = books_issued.book_accn_no.acc_no
    # book_issue_date = books_issued.issue_date
    # book_return_date = books_issued.return_date
    # book_expected_return_date = books_issued.expected_return_date
    # book_fine_collected_date = books_issued.fine_collected_date
    # book_fine_amount = books_issued.fine_amount
    # book_status = books_issued.status
    results = []
    for i in books_issued:
        books_json = {}
        books_json['book_id'] = i.id
        books_json['student_id'] = i.student.enr_id
        books_json['book_accn_no'] = i.book_accn_no.acc_no
        books_json['book_name_id'] = i.book_accn_no.id
        books_json['book_issue_date'] = str(i.issue_date)
        books_json['book_return_date'] = str(i.return_date)
        books_json['book_expected_return_date'] = str(i.expected_return_date)
        books_json['book_name'] = str(i.book_accn_no.title.name)
        books_json['book_fine_collected_date'] = str(i.fine_collected_date)
        books_json['book_fine_amount'] = int(i.fine_amount)
        books_json['book_status'] = i.status
        results.append(books_json)    
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def return_this_book(request):
    accn_no = request.GET.get('book_accn')
    accn_no_obj = Stock.objects.get(acc_no=accn_no)
    student_id = request.GET.get('student_id')
    stud_obj = Student.objects.get(enr_id=student_id)
    book_id = request.GET.get('book_id')
    book_obj = Stock.objects.get(pk=book_id)
    print('book id is:',book_obj)
    user_obj = BookIssueReturnStudent.objects.filter(student=stud_obj.id, book_accn_no=book_obj).update(student=None,book_accn_no=None, status='available')
    us = int(user_obj)
    print('user_obj',user_obj)
    context = {}
    next_user_obj = 0
    if(us == 1):
        next_user_obj = Stock.objects.filter(id=book_obj.id).update(status='available')
        print('next_user_obj',next_user_obj)
        context = {
            'next_user_obj':next_user_obj,
        }
    else:
        print('next_user_obj',next_user_obj)
        context = {
            'next_user_obj':next_user_obj,
        }
    data = json.dumps(context)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def find_the_book(request):
    item_accn = request.GET.get('item_accn')
    student_id = request.GET.get('student_id')
    item_barcode = request.GET.get('item_barcode')
    stud_obj = Student.objects.get(enr_id=student_id)
    if item_accn !="":
        item_accn_obj = Stock.objects.get(acc_no=item_accn)
        context = {
            'item_accn':item_accn_obj.acc_no,
            'book_id':item_accn_obj.id,
            'book_name':item_accn_obj.name,
            'book_title':item_accn_obj.title.name,
            'book_author1':item_accn_obj.author1.name,
            'book_author2':item_accn_obj.author2.name,
            'book_barcode':item_accn_obj.barcode,
        }
    if item_barcode != "":
        item_barcode_obj = Stock.objects.get(barcode=item_barcode)
        context = {
            'item_barcode':item_accn_obj.barcode,
            'book_id':item_accn_obj.id,
            'book_name':item_accn_obj.name,
            'book_title':item_accn_obj.title.name,
            'book_author1':item_accn_obj.author1.name,
            'book_author2':item_accn_obj.author2.name,
            'item_accn':item_accn_obj.acc_no,
        }
    data = json.dumps(context)
    return HttpResponse(data, 'application/json')
        

def issue_this_book(request):
    book_id = request.GET.get('book_id')
    book_accn = request.GET.get('book_accn')
    student_id = request.GET.get('student_id')    
    data_length = request.GET.get('data_length')
    issue_date = request.GET.get('issue_date')
    expected_return_date = request.GET.get('expected_return_date')
    book_obj = Stock.objects.get(pk=book_id)
    stud_obj = Student.objects.get(enr_id=student_id)
    print('book Obj:', book_obj.id)
    print('student Obj:', stud_obj.id)
    user = BookIssueReturnStudent()
    user.status = 'not available'
    user.issue_date = issue_date
    user.expected_return_date = expected_return_date
    user.student = stud_obj
    user.book_accn_no = book_obj
    user.save()
    message = "Successfully Issued"
    context = {}
    if(user == 1):
        context = {
            'message':message
        }
    else:
        context = {
            'message':'Unsuccessfull attempt'
        }
    data = json.dumps(context)
    return HttpResponse(data, 'application/json')





# obj.refresh_from_db()
# use this somewhere in issue and return