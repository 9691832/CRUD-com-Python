from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    all_cars = Carros.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        data['search_query'] = search_query
        data['db'] = Carros.objects.filter(modelo__icontains=search_query)
    else:
        paginator = Paginator(all_cars, 2)
        page_number = request.GET.get('page')
        data['db'] = paginator.get_page(page_number)

    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('HomePage')

def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('HomePage')
    
def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('HomePage') 