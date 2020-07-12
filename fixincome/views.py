from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Treasury_Yield
from .serializers import TreasuryYieldSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

import scipy.optimize as optimize
from fixincome.BootstrapYieldCurve import BootstrapYieldCurve

class TreasuryYieldViewSet(viewsets.ModelViewSet):
    queryset = Treasury_Yield.objects.all()
    serializer_class = TreasuryYieldSerializer
    authentication_classes =(TokenAuthentication,)
    permission_classed = (IsAuthenticated,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes =(TokenAuthentication,)


def index(request):
    return render(request, 'http://localhost:3000/components')


def viewProduct(request):
    count = 0
    if request.method == 'GET':
        product_list = Treasury_Yield.objects.all()
        products = []
        yield_curve = BootstrapYieldCurve()
        for prod in product_list:
            # yield_curve.add_instrument(prod.maturity, prod.yeild, 0., 97.5)
            count= count+1
            products.append(
                {'number1': prod.maturity, 'number2': prod.yeild})
    return JsonResponse(products, safe=False)

def fixincome(request):
  return HttpResponse("Hello, world. You're at the polls index.")


