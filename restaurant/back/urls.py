from django.urls import path
from . import views

app_name = 'back'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.mazir, name='menu'), 
    path('reviews/', views.reviews_page, name='reviews'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('tables/', views.tables_view, name='tables'),
    path('booking/<int:table_number>/<str:time>/', views.booking, name='booking'),
    path('confirm_delete_booking/<int:booking_id>/', views.confirm_delete_booking, name='confirm_delete_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('booking_success/<int:table_number>/<str:time>/<str:phone>/', views.booking_success, name='booking_success'),
    path('table/<int:table_number>/<str:time>/', views.table_details, name='table_details'),
    path('book_table/', views.book_table, name='book_table'),
    path('save_phone_number/', views.save_phone_number, name='save_phone_number'),
    path('success_deleted/<int:table_number>/<str:time>/', views.success_deleted, name='success_deleted'),
]
