from django.urls import path
from . import views

urlpatterns = [
    path('building_create',views.building_create, name='building_create'),
    path('building_list',views.building_list, name='building_list'),
    path('building_edit/<int:pk>/',views.building_edit, name='building_edit'),
    path('building_delete/<int:pk>/',views.building_delete, name='building_delete'),

    path('floor_create',views.floor_create, name='floor_create'),
    path('floor_list',views.floor_list, name='floor_list'),
    path('floor_edit/<int:pk>/',views.floor_edit, name='floor_edit'),
    path('floor_delete/<int:pk>/',views.floor_delete, name='floor_delete'),

    path('room_create',views.room_create, name='room_create'),
    path('room_list',views.room_list, name='room_list'),
    path('room_edit/<int:pk>/',views.room_edit, name='room_edit'),
    path('room_delete/<int:pk>/',views.room_delete, name='room_delete'),

    path('rack_create',views.rack_create, name='rack_create'),
    path('rack_list',views.rack_list, name='rack_list'),
    path('rack_edit/<int:pk>/',views.rack_edit, name='rack_edit'),
    path('rack_delete/<int:pk>/',views.rack_delete, name='rack_delete'),

    path('shelf_create',views.shelf_create, name='shelf_create'),
    path('shelf_list',views.shelf_list, name='shelf_list'),
    path('shelf_edit/<int:pk>/',views.shelf_edit, name='shelf_edit'),
    path('shelf_delete/<int:pk>/',views.shelf_delete, name='shelf_delete'),

    path('vendor_create',views.vendor_create, name='vendor_create'),
    path('vendor_list',views.vendor_list, name='vendor_list'),
    path('vendor_update/<int:pk>/',views.vendor_update, name='vendor_update'),
    path('vendor_delete/<int:pk>/',views.vendor_delete, name='vendor_delete'),

    path('issuetype_create',views.issuetype_create, name='issuetype_create'),
    path('issuetype_list',views.issuetype_list, name='issuetype_list'),
    path('issuetype_edit/<int:pk>/',views.issuetype_edit, name='issuetype_edit'),
    path('issuetype_delete/<int:pk>/',views.issuetype_delete, name='issuetype_delete'),

    path('store_create',views.store_create, name='store_create'),
    path('store_list',views.store_list, name='store_list'),
    path('store_edit/<int:pk>/',views.store_edit, name='store_edit'),
    path('store_delete/<int:pk>/',views.store_delete, name='store_delete'),

    path('section_create/',views.section_create, name='section_create'),
    path('section_list/',views.section_list, name='section_list'),
    path('section_edit/<int:pk>/',views.section_edit, name='section_edit'),
    path('section_delete/<int:pk>/',views.section_delete, name='section_delete'),

    path('bookcategory_create/',views.bookcategory_create, name='bookcategory_create'),
    path('bookcategory_list/',views.bookcategory_list, name='bookcategory_list'),
    path('bookcategory_edit/<int:pk>/',views.bookcategory_edit, name='bookcategory_edit'),
    path('bookcategory_delete/<int:pk>/',views.bookcategory_delete, name='bookcategory_delete'),

    path('title_create/',views.title_create, name='title_create'),
    path('title_list/',views.title_list, name='title_list'),
    path('title_edit/<int:pk>/',views.title_edit, name='title_edit'),
    path('title_delete/<int:pk>/',views.title_delete, name='title_delete'),

    path('subject_create/',views.subject_create, name='subject_create'),
    path('subject_list/',views.subject_list, name='subject_list'),
    path('subject_edit/<int:pk>/',views.subject_edit, name='subject_edit'),
    path('subject_delete/<int:pk>/',views.subject_delete, name='subject_delete'),

    path('author_create/',views.author_create, name='author_create'),
    path('author_list/',views.author_list, name='author_list'),
    path('author_edit/<int:pk>/',views.author_edit, name='author_edit'),
    path('author_delete/<int:pk>/',views.author_delete, name='author_delete'),

    path('publisher_create/',views.publisher_create, name='publisher_create'),
    path('publisher_list/',views.publisher_list, name='publisher_list'),
    path('publisher_edit/<int:pk>/',views.publisher_edit, name='publisher_edit'),
    path('publisher_delete/<int:pk>/',views.publisher_delete, name='publisher_delete'),

    path('department_create/',views.department_create, name='department_create'),
    path('department_list/',views.department_list, name='department_list'),
    path('department_edit/<int:pk>/',views.department_edit, name='department_edit'),
    path('department_delete/<int:pk>/',views.department_delete, name='department_delete'),

    path('bindingtype_create/',views.bindingtype_create, name='bindingtype_create'),
    path('bindingtype_list/',views.bindingtype_list, name='bindingtype_list'),
    path('bindingtype_edit/<int:pk>/',views.bindingtype_edit, name='bindingtype_edit'),
    path('bindingtype_delete/<int:pk>/',views.bindingtype_delete, name='bindingtype_delete'),

    path('language_create/',views.language_create, name='language_create'),
    path('language_list/',views.language_list, name='language_list'),
    path('language_edit/<int:pk>/',views.language_edit, name='language_edit'),
    path('language_delete/<int:pk>/',views.language_delete, name='language_delete'),

    path('edition_create/',views.edition_create, name='edition_create'),
    path('edition_list/',views.edition_list, name='edition_list'),
    path('edition_edit/<int:pk>/',views.edition_edit, name='edition_edit'),
    path('edition_delete/<int:pk>/',views.edition_delete, name='edition_delete'),

    path('currency_create/',views.currency_create, name='currency_create'),
    path('currency_list/',views.currency_list, name='currency_list'),
    path('currency_edit/<int:pk>/',views.currency_edit, name='currency_edit'),
    path('currency_delete/<int:pk>/',views.currency_delete, name='currency_delete'),

    path('mastersetup1/',views.mastersetup1, name='mastersetup1'),
    path('mastersetup2/',views.mastersetup2, name='mastersetup2'),
    path('mastersetup3/',views.mastersetup3, name='mastersetup3'),

    path('category_create/',views.category_create, name='category_create'),
    path('category_list/',views.category_list, name='category_list'),
    path('category_update/<int:pk>/',views.category_update, name='category_update'),
    path('category_delete/<int:pk>/',views.category_delete, name='category_delete'),

    path('subcategory_create/',views.subcategory_create, name='subcategory_create'),
    path('subcategory_list/',views.subcategory_list, name='subcategory_list'),
    path('subcategory_update/<int:pk>/',views.subcategory_update, name='subcategory_update'),
    path('subcategory_delete/<int:pk>/',views.subcategory_delete, name='subcategory_delete'),

    path('library_mapping_create/', views.library_mapping_create, name="library_mapping_create"),
    path('library_mapping_list/', views.library_mapping_list, name="library_mapping_list"),
    path('library_mapping_edit/<int:pk>/', views.library_mapping_edit, name="library_mapping_edit"),
    path('library_mapping_delete/<int:pk>/', views.library_mapping_delete, name="library_mapping_delete"),
    
    path('entity_type_create/', views.entity_type_create, name="entity_type_create"),
    path('entity_type_list/', views.entity_type_list, name="entity_type_list"),
    path('entity_type_edit/<int:pk>/', views.entity_type_edit, name="entity_type_edit"),
    path('entity_type_delete/<int:pk>/', views.entity_type_delete, name="entity_type_delete"),

    path('library_entity_mapping_create/', views.library_entity_mapping_create, name='library_entity_mapping_create'),
    path('library_entity_mapping_list/', views.library_entity_mapping_list, name='library_entity_mapping_list'),
    path('library_entity_mapping_edit/<int:pk>/', views.library_entity_mapping_edit, name='library_entity_mapping_edit'),
    path('library_entity_mapping_delete/<int:pk>/', views.library_entity_mapping_delete, name='library_entity_mapping_delete'),

    path('requisiton_create/', views.requisiton_create, name='requisiton_create'),
    path('requisiton_list/', views.requisiton_list, name='requisiton_list'),
    path('items_add_requisition/<int:pk>/', views.items_add_requisition, name='items_add_requisition'),
    path('items_add_to_stock/', views.items_add_to_stock, name='items_add_to_stock'),
    path('items_add_requisition_list/', views.items_add_requisition_list, name='items_add_requisition_list'),
    path('manual_stock_entry_create/', views.manual_stock_entry_create, name='manual_stock_entry_create'),
    path('manual_stock_entry_list/', views.manual_stock_entry_list, name='manual_stock_entry_list'),
    path('manual_stock_entry_edit/<int:pk>/', views.manual_stock_entry_edit, name='manual_stock_entry_edit'),
    path('manual_stock_entry_delete/<int:pk>/', views.manual_stock_entry_delete, name='manual_stock_entry_delete'),
    path('acquisition/', views.acquisition, name='acquisition'),
    path('load_books/', views.load_books, name='load_books'),
    path('create_books/', views.create_books, name='create_books'),
    path('acquisition_form/<int:num>/', views.acquisition_form, name='acquisition_form'),
    path('get_books_name/', views.get_books_name, name="get_books_name"),
    path('library_book_issue/', views.library_book_issue, name="library_book_issue"),
    path('student_autocomplete/', views.student_autocomplete, name="student_autocomplete"),
    path('get_student_book_list/', views.get_student_book_list, name="get_student_book_list"),
    path('return_this_book/', views.return_this_book, name="return_this_book"),
    path('find_the_book/', views.find_the_book, name="find_the_book"),
    path('issue_this_book/', views.issue_this_book, name="issue_this_book"),
]