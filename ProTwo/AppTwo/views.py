from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    # return HttpResponse("<em>My Second App</em>")
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'AppTwo/index.html',context=user_dict)


def help(request):
    my_dict = {'insert_me': "Hellloooo,practice help"}
    return render(request, 'AppTwo/help.html', context=my_dict)