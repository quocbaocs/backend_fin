from django.shortcuts import render

# Create your views here.
# ---------------------
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, 'http://localhost:3000/components')


def viewProduct(request):
    count = 0
    if request.method == 'GET':
        product_list = Yield_curve.objects.all()
        products = []
        for prod in product_list:
            count= count+1
            products.append(
                {'number1': float(prod.number1), 'number2':float(prod.number2)})
    return JsonResponse(products, safe=False)

# def index(request):
#     book_list = Book.objects.order_by('-pub_date')[:10]
#     return render(request, 'qlbook/index.html', {'book_t': book_list})