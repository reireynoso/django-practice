from django.shortcuts import render
# from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm
# Create your views here.

def index(request):
    # return HttpResponse("<em>My Second App</em>")
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'AppTwo/index.html',context=user_dict)


def help(request):
    my_dict = {'insert_me': "Hellloooo,practice help"}
    return render(request, 'AppTwo/help.html', context=my_dict)

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True) # saves to the db
            return index(request) # redirect to index page
            # print("first:" + form.cleaned_data['first_name'])
            # print("Last:" + form.cleaned_data['last_name'])
            # print("email:" + form.cleaned_data['email'])
        else:
            print("ERROR FORM INVALID")

    return render(request, 'AppTwo/model_form.html', {'form': form})