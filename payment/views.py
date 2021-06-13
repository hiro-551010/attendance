from django.shortcuts import render
from accounts.models import User, Profile



def pay(request):
    payment = request.user.hourly_wage
    context = {
        'payment': payment
    }
    return render(request, 'payment/pay.html', context)