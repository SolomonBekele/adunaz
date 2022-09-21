from django.urls import path
from django.shortcuts import render


def demo(request):
    return render(request, 'accounts/index.html', {})


urlpatterns = [
    path('', demo, name="acc-index")
]
