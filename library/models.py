from django.db import models
from student.models import Student
from employee.models import Employee


ENTITY_TYPE = (
    ('Faculty','Faculty'),
    ('Student','Student'),
)

class Building(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Floor(models.Model):
    name = models.CharField(max_length=100)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Rack(models.Model):
    name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Shelf(models.Model):
    name = models.CharField(max_length=100)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class IssueType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Title(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    gst = models.CharField(max_length=250,null=True, blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BindingType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, null=True, blank=True)
    sequence = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Edition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, null=True, blank=True)
    sequence = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    contact = models.CharField(max_length=25)
    email = models.EmailField(null=True,blank=True)
    gst = models.CharField(max_length=50,null=True, blank=True)
    pan = models.CharField(max_length=50,null=True, blank=True)
    tan = models.CharField(max_length=50,null=True, blank=True)
    cin = models.CharField(max_length=100)
    image = models.ImageField(upload_to='vendors/images/',blank=True, null=True, editable=True)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)
    requisition_no = models.CharField(max_length=250)
    bill_no = models.CharField(max_length=250)
    bill_date = models.DateField(null=True,blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    other_reference = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=10,null=True, blank=True)
    no_of_products_purchased = models.IntegerField(default=0)

    def __str__(self):
        return '{}--{}'.format(self.bill_no,self.bill_date)

class PurchaseOrderDetails(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    particulars = models.CharField(max_length=250,null=True, blank=True)
    hsn = models.CharField(max_length=250,null=True, blank=True)
    amount = models.DecimalField(decimal_places=2,max_digits=10,null=True, blank=True)

ACCESSION_CHOICES = (
    ('Accession', 'Accession'),
    ('Obsolete', 'Obsolete'),
    ('Missing', 'Missing'),
)



BOOLEAN_CHOICE = (
    ('available','available'),
    ('not available','not available'),
)

class Entity(models.Model):
    name = models.CharField(max_length=100, choices=ENTITY_TYPE, default='Student')

    def __str__(self):
        return self.name

class CategoryMapping(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    item_category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    abbr = models.CharField(max_length=100)
    last_sequence_no = models.IntegerField(default=0)

class EntityMapping(models.Model):
    category_mapping = models.ForeignKey(CategoryMapping, on_delete=models.CASCADE)
    entity_type = models.ForeignKey(Entity, on_delete=models.CASCADE)
    issue_type = models.ForeignKey(IssueType, on_delete=models.CASCADE)
    number_of_books = models.IntegerField(default=0)
    number_of_days = models.IntegerField(default=0)

class Requisition_Number(models.Model):
    date = models.DateField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    requisition_num = models.CharField(max_length=250)

    def __str__(self):
        return self.requisition_num

class Requisition(models.Model):
    requisition = models.ForeignKey(Requisition_Number, on_delete=models.CASCADE, null=True, blank=True)
    book_name = models.CharField(max_length=100, null=True, blank=True)
    no_of_copies = models.IntegerField(default=0, null=True, blank=True)
    author1 = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_1', null=True, blank=True)
    author2 = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_2', null=True, blank=True)
    author3 = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_3', null=True, blank=True)
    author4 = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_4', null=True, blank=True)
    author5 = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_5', null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, null=True, blank=True)
    binding_type = models.ForeignKey(BindingType, on_delete=models.CASCADE, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    publication_year = models.DateField(null=True, blank=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE,null=True, blank=True)
    author6 = models.CharField(max_length=250, null=True, blank=True)
    author7 = models.CharField(max_length=250, null=True, blank=True)
    author8 = models.CharField(max_length=250, null=True, blank=True)
    publisher1 = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return self.book_name

class Acquisition(models.Model):
    pass

class Accesion(models.Model):
    name = models.CharField(max_length=100)
    pass

class LibraryMapping(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    book_category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    abbr = models.IntegerField(default=0)
    sequence = models.IntegerField(default=0)

class LibraryEntityMapping(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    issue_type = models.ForeignKey(IssueType, on_delete=models.CASCADE)
    num_of_books = models.IntegerField(default=0)
    max_days = models.IntegerField(default=0)

class Stock(models.Model):
    name = models.CharField(max_length=100)
    acc_no = models.CharField(max_length=100)
    book_no = models.CharField(max_length=100)
    date_of_addition = models.DateField(null=True, blank=True)
    ISBN = models.CharField('ISBN',max_length=250,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    title = models.ForeignKey(Title, on_delete=models.CASCADE, null=True, blank=True)
    author1 = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author1', null=True, blank=True)
    author2 = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author2', null=True, blank=True)
    author3 = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author3', null=True, blank=True)
    author4 = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author4', null=True, blank=True)
    author5 = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author5', null=True, blank=True)
    author6 = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author6', null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, null=True, blank=True)
    issue_type = models.ForeignKey(IssueType, on_delete=models.CASCADE, null=True, blank=True)
    book_category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    binding_type = models.ForeignKey(BindingType, on_delete=models.CASCADE, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=250, choices=BOOLEAN_CHOICE, default='available')
    availablity = models.IntegerField(default=0, null=True, blank=True)
    barcode = models.CharField(max_length=250, null=True, blank=True)
    requisition = models.ForeignKey(Requisition_Number, on_delete=models.CASCADE, null=True, blank=True) 
    
    def __str__(self):
        return self.name



class BookIssueReturnStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    book_accn_no = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, blank=True)
    issue_date = models.DateField(auto_now_add=False, null=True, blank=True)
    return_date = models.DateField(auto_now_add=False, null=True, blank=True)
    expected_return_date = models.DateField(null=True, blank=True)
    fine_collected_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=BOOLEAN_CHOICE, max_length=50, null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    

