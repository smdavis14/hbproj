from django.shortcuts import render

# Create your views here.
def shopping_cart(request):
    print(request.POST)
    return render(request, 'hb/shopping_cart.html')