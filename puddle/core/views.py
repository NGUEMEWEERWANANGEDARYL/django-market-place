from django.shortcuts import render
from item.models import category, item

# Create your views here.
def index(request):
    items = item.object.filter(is_sold=False)[0:6]
    categories = category.object.all()

    return render(request, 'core/index.html'{
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

