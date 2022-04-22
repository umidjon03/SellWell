from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import AddProdForm
from .models import Product, Category

# Create your views here.


@login_required(login_url='login')
def add(request):
    form = AddProdForm()
    categories = Category.objects.all()
    if request.method == 'POST':
        category_name = request.POST.get('category')
        category = Category.objects.get(category=category_name)
        Product.objects.create(
            seller = request.user,
            title = request.POST.get('title'),
            type_prod = request.POST.get('itemName') ,
            decsription = request.POST.get('description'),
            category = category,
            price = request.POST.get('price'),
            negotiable = True if request.POST.get('negotiable')=='on' else False,
            contact_name = request.POST.get('c_name'),
            contact_number = request.POST.get('c_number'),
            email = request.POST.get('c_email'),
            address = request.POST.get('address'),
            image = request.FILES['file'],
        )
        return redirect('home')
        
    context = {'form': form, 'categories': categories}
    return render(request, 'products/add.html', context)
