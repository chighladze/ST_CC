from django.shortcuts import render
from home.models import StMonthlyStatistic
from django.http import HttpResponse
# Create your views here.


def monthlystatistic(request):
    item = StMonthlyStatistic.objects.filter()
    context = {
        'item': item,
    }
    return render(request, 'home/index.html', context=context)
