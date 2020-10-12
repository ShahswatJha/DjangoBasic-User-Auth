from django.shortcuts import render
from accounts.models import Account

# Create your views here.

def home_view(request):
    context = {}
    account = Account.objects.all()
    context["account"] = account
    return render(request,'main/home.html',context)
