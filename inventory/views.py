from django.shortcuts import render
from .models import inventory, supplier

# Create your views here.
def index(request):
    queryset = inventory.objects.all()
    context = {
        'inventory': queryset,
    }
    return render(request, "inventory/index.html", context)

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