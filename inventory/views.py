from django.shortcuts import render
from .models import inventory, supplier
import requests
from django.db.models import Q

# Create your views here.
def index(request):

    response = requests.get('http://127.0.0.1:8000/api/inventory')
    inv_data = response.json()

    # Get all suppliers
    # supplier_name = supplier.objects.all().values('id','name')

    for inv in inv_data["data"]:
        inv["supplier"] = supplier.objects.filter(id=inv["supplier"]).values_list('name').first()[0]

    context = {
        'inv_list': inv_data['data'],
    }
    return render(request, "inventory/index.html", context)

def search(request):
    if request.method=='GET':
        
        # Set default search value
        name = request.GET.get('name', default="")

        # Filter the model
        queryset = inventory.objects.filter(
            Q(name__icontains=name)
        )
        context = {
            'inv_list': queryset,
        }
        return render(request, 'inventory/index.html', context)

def search_by_id(request, id="undefined"):
    queryset = inventory.objects.filter(id=id).values().first()

    # Set supplier_id to name
    supplier_name = supplier.objects.filter(id=queryset["supplier_id"]).values_list('name').first()
    queryset["supplier_id"]=supplier_name[0]

    # Change "supplier_id" to just "supplier"
    queryset["supplier"] = queryset["supplier_id"]
    del queryset["supplier_id"]

    context = {
        'inventory': queryset,
    }
    return render(request, "inventory/details.html", context)