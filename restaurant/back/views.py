from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *    
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

menu = [
    {'title': 'aid', 'url': 'back:home'}
]

from django.shortcuts import render

def home(request):
    menu = MenuItem.objects.all()
    categories = Category.objects.all()
    categorized_menu = {category.name: [] for category in categories}

    for item in menu:
        categorized_menu[item.category.name].append(item)

    menu_chunks = {}
    total_items = 0

    for category_name, items in categorized_menu.items():
        if total_items >= 4:
            break
        num_to_add = min(1, len(items))
        menu_chunks[category_name] = items[:num_to_add]
        total_items += num_to_add

    reviews = Review.objects.all()[:4]

    data = {
        'menu_chunks': menu_chunks,
        'title': 'Главная страница',
        'reviews': reviews,
    }
    return render(request, 'back/home.html', context=data)

def mazir(request):
    menu_items = MenuItem.objects.all()
    categories = Category.objects.all()
    categorized_menu = {category: [item for item in menu_items if item.category == category] for category in categories}
    data = {
        'categorized_menu': categorized_menu,
        'categories': categories,
        'title': 'Главная страница'
    }
    
    return render(request, 'back/menu.html', context=data)

def reviews_page(request):
    reviews = Review.objects.all()
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user 
            review.save()
            messages.success(request, 'Отзыв успешно добавлен!')
            return redirect('back:reviews')  

    return render(request, 'back/reviews.html', {'reviews': reviews, 'form': form})

def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        review.delete()
    return redirect('back:reviews') 

def tables_view(request):
    site_settings_list = SiteSettings.objects.all()
    tables = Table.objects.all()

    times_lists = [site_settings.times.split(',') for site_settings in site_settings_list]
    time = times_lists[0][0] if times_lists and times_lists[0] else '00:00'

    context = {
        'tables': tables,
        'times_lists': times_lists,
        'time': time,
    }

    return render(request, 'back/tables.html', context)


@login_required
def booking(request, table_number, time):
    table_number = int(table_number)
    tables = Table.objects.all()
    is_booked_tables = [booking.table_number for booking in Booking.objects.filter(time=time)]
    
    is_booked = False
    is_booked_by_other = False
    user_booking = None
    user_booked_tables = []

    if request.user.is_authenticated:
        user_booking = Booking.objects.filter(user=request.user, table_number=table_number, time=time).first()
        is_booked = user_booking is not None
        user_booked_tables = [booking.table_number for booking in Booking.objects.filter(user=request.user, time=time)]
        is_booked_by_other = table_number in is_booked_tables and not is_booked
    
    has_booked = request.session.get('has_booked', False)
    if has_booked and is_booked:
        messages.error(request, 'Вы уже забронировали столик на данное время.')
        request.session['has_booked'] = False  
        return redirect('back:booking', table_number=table_number, time=time)

    booking = Booking.objects.filter(table_number=table_number, time=time).first()

    context = {
        'tables': tables,
        'table_number': table_number,
        'time': time,
        'is_booked': is_booked,
        'is_booked_by_other': is_booked_by_other,
        'is_booked_tables': is_booked_tables,
        'user_booking': user_booking,
        'user_booked_tables': user_booked_tables,
        'booking': booking,  
    }

    if request.user.is_authenticated:
        return render(request, 'back/booking.html', context)
    else:
        messages.error(request, 'Чтобы забронировать столик, пожалуйста, войдите в систему.')
        return redirect('authe:signup')

@login_required
def confirm_delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    context = {'booking': booking}
    return render(request, 'back/confirm_delete_booking.html', context)

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    table_number = booking.table_number
    time = booking.time
    booking.delete()
    messages.success(request, 'Бронь успешно удалена.')
    return redirect('back:success_deleted', table_number=table_number, time=time)

def success_deleted(request, table_number, time):
    return render(request, 'back/success_deleted.html', {'table_number': table_number, 'time': time})


def booking_success(request, table_number, time, phone):
    table_number = int(table_number)

    try:
        table = Table.objects.get(number=table_number)
    except Table.DoesNotExist:
        messages.error(request, 'Столик не найден')
        return redirect('back:tables')

    table.is_reserved = True
    table.save()

    return render(request, 'back/booking_success.html', {'table_number': table_number, 'time': time, 'phone': phone})


def table_details(request, table_number, time=None):
    try:
        table = Table.objects.get(number=table_number)
    except Table.DoesNotExist:
        messages.error(request, 'Столик не найден')
        return redirect('back:tables')

    is_booked = False
    is_booked_by_other = False

    if request.user.is_authenticated:
        is_booked = Booking.objects.filter(user=request.user, table_number=table_number, time=time).exists()
        if not is_booked:
            is_booked_by_other = Booking.objects.filter(table_number=table_number, time=time).exists()

    context = {
        'table_number': table.number,
        'time': time,
        'is_booked': is_booked,
        'is_booked_by_other': is_booked_by_other,
    }
    return render(request, 'back/table_details.html', context)


def book_table(request):
    if request.method == 'POST':
        table_number = request.POST.get('table_number')
        time = request.POST.get('time')
        phone = request.POST.get('phone')

        if Booking.objects.filter(user=request.user, table_number=table_number, time=time).exists():
            messages.error(request, 'Вы уже забронировали этот столик на данное время.')
            return redirect('back:table_details', table_number=table_number, time=time)

        existing_booking = Booking.objects.filter(table_number=table_number, time=time).exists()
        if existing_booking:
            messages.error(request, 'Столик уже забронирован другим пользователем.')
            return redirect('back:table_details', table_number=table_number, time=time)

        booking = Booking.objects.create(
            user=request.user,
            table_number=table_number,
            time=time,
            phone=phone
        )

        request.session['has_booked'] = True

        messages.success(request, 'Столик успешно забронирован.')
        return redirect('back:booking_success', table_number=table_number, time=time, phone=phone)
    else:
        return redirect('back:tables')

def save_phone_number(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        PhoneNumber.objects.create(phone_number=phone_number)
        return HttpResponse('Номер успешно отправлен в админ панель.')
    return HttpResponse('Метод не поддерживается.')