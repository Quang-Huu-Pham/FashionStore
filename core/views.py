from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render, redirect
import datetime
from .models import ProfileUser
from .forms import RegistrationForm, UserProfileForm
from order.models import OrderItem

from product.models import Product, Category, Classify
# Create your views here.


def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile = ProfileUser(user_id=user.id)
            profile.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {'form': form})


def index(request):
    products = Product.objects.all()[0:8]
    categories = Category.objects.all()
    classifies = Classify.objects.all()

    if request.user.id:
        profile = ProfileUser.objects.get(user=request.user.id)
    else:
        profile = None

    active_category = request.GET.get('category', '')

    if active_category:
        products = Product.objects.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query))

    type = request.GET.get('type', '')

    if type:
        products = Product.objects.filter(classify=type)
        return render(request, 'product/product_list.html', {'products': products})

    page = request.GET.get('page', '')

    if page:
        products = Product.objects.all()[0:8+int(page)]
        return render(request, 'product/product_list.html', {'products': products})

    context = {
        'products': products,
        'categories': categories,
        'classifies': classifies,
        'active_category': active_category,
        'profile': profile,
    }

    return render(request, 'core/home.html', context)


def filter_price(request, action):
    if action == 'short':
        products = Product.objects.order_by('-price')
    elif action == 'tall':
        products = Product.objects.order_by('price')

    return render(request, 'product/product_list.html', {'products': products})


@login_required
def myprofile(request):
    profile = ProfileUser.objects.get(user=request.user.id)
    return render(request, 'core/myprofile.html', {'profile': profile})


@login_required
def edit_myprofile(request):
    profile = ProfileUser.objects.get(user=request.user.id)

    if request.method == 'POST' and request.FILES['avatar']:
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        profile.avatar = request.FILES.get('avatar')
        profile.phone = request.POST.get('phone')
        user.save()
        profile.save()

        return redirect('myprofile')

    return render(request, 'core/edit_myprofile.html', {'profile': profile})


def analytics(request):
    order = OrderItem.objects.all()

    statistical = 0

    for item in order:
        dateOrder = item.order.created_at
        if (str(dateOrder)[:10] == str(datetime.date(2023, 1, 11))):
            statistical += item.quantity

    return render(request, 'core/analytics.html', {'statistical': statistical})
