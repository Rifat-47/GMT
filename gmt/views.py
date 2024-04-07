# gmt/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .utils import get_timezone_info

def gmt_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        result = get_timezone_info(phone_number)
        context = {'result': result, 'name': name}
        return render(request, 'gmt/form.html', context)
    else:
        return render(request, 'gmt/form.html')
