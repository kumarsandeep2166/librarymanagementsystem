from django import forms
from .models import (Building, Floor, Room, Rack, Shelf,
                    IssueType, Stock, Store, Section, Subject, BookCategory, Title,
                    Author, Publisher, Department, BindingType, Language, Edition, Currency,
                    Vendor, PurchaseOrder, Entity, CategoryMapping, EntityMapping,
                    Category, SubCategory
                    )

class BuildingForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Building(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class FloorForm(forms.Form):
    name = forms.CharField(max_length=100)
    building = forms.ChoiceField(choices=[(o.id, str(o.name)) for o in Building.objects.all()])

    def save(self):
        data = self.cleaned_data
        building_obj = Building.objects.get(pk=data['building'])
        user = Floor(name=data['name'], building=building_obj)
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        building_obj = Building.objects.get(pk=data['building'])
        obj.building = building_obj
        obj.save()
        return obj

class RoomForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Room(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class RackForm(forms.Form):
    name = forms.CharField(max_length=100)
    room = forms.ChoiceField(choices=[(o.id, str(o.name)) for o in Room.objects.all()])

    def save(self):
        data = self.cleaned_data
        room_obj = Room.objects.get(pk=data['room'])
        user = Rack(name=data['name'], room=room_obj)
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        room_obj = Room.objects.get(pk=data['room'])
        obj.room = room_obj
        obj.save()
        return obj

class ShelfForm(forms.Form):
    name = forms.CharField(max_length=100)
    rack = forms.ChoiceField(choices=[(o.id, str(o.name)) for o in Rack.objects.all()])

    def save(self):
        data = self.cleaned_data
        rack_obj = Rack.objects.get(pk=data['rack'])
        user = Rack(name=data['name'], rack=rack_obj)
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        rack_obj = Rack.objects.get(pk=data['rack'])
        obj.rack = rack_obj
        obj.save()
        return obj

class IssueTypeForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = IssueType(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class StoreForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Store(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class SectionForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Section(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class BookCategoryForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    sub_category = forms.ChoiceField(choices=[(o.id, str(o.name)) for o in SubCategory.objects.all()])

    def save(self):
        data = self.cleaned_data
        sub_category_obj = SubCategory.objects.get(pk=data['sub_category'])
        user = BookCategory(name=data['name'], sub_category=sub_category_obj)
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        bookcategory_obj = SubCategory.objects.get(pk=data['sub_category'])
        obj.sub_category = bookcategory_obj
        obj.save()
        return obj

class SubCategoryForm(forms.Form):
    name = forms.CharField(max_length=100)
    main_category = forms.ChoiceField(choices=[(o.id, str(o.name)) for o in Category.objects.all()])

    def save(self):
        data = self.cleaned_data
        sub_category_obj = Category.objects.get(pk=data['main_category'])
        user = SubCategory(name=data['name'], sub_category=sub_category_obj)
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        bookcategory_obj = Category.objects.get(pk=data['main_category'])
        obj.main_category = bookcategory_obj
        obj.save()
        return obj

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Category(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj


class TitleForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Title(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Author(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class PublisherForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Publisher(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class SubjectForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Subject(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class DepartmentForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Department(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class BindingTypeForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = BindingType(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class LanguageForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Language(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class EditionForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Edition(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class CurrencyForm(forms.Form):
    name = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = Currency(name=data['name'])
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.save()
        return obj

class VendorForm(forms.Form):
    name = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.Textarea,required=False)
    contact = forms.CharField(max_length=25, required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    gst = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    pan = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    tan = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    cin = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    image = forms.ImageField(required=False)

    def save(self):
        data = self.cleaned_data
        user = Vendor(
            name = data['name'],
            address = data['address'],
            contact = data['contact'],
            email = data['email'],
            gst = data['gst'],
            pan = data['pan'],
            tan = data['tan'],
            cin = data['cin'],
            image = data['image'],
        )
        user.save()
    
    def update(self, obj):
        data = self.cleaned_data
        obj.name = data['name']
        obj.address = data['address']
        obj.contact = data['contact']
        obj.email = data['email']
        obj.gst = data['gst']
        obj.pan = data['pan']
        obj.tan = data['tan']
        obj.cin = data['cin']
        obj.image = data['image']
        obj.save()
        return obj

