from django.http import HttpResponse
from django.template import loader
from .models import Products


def products(request):
    myproducts = Products.objects.all().values()
    template = loader.get_template("all_products.html")
    context = {
        myproducts: myproducts,
    }
    return HttpResponse(template.render(context, request))


