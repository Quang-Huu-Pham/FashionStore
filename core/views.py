from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import ProfileUser
from .forms import RegistrationForm, UserProfileForm

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

    page = request.GET.get('page', '')

    if page:
        products = Product.objects.all()[0:8+int(page)]

    context = {
        'products': products,
        'categories': categories,
        'classifies': classifies,
        'active_category': active_category,
        'profile': profile,
    }

    return render(request, 'core/home.html', context)


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
