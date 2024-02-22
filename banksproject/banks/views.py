from django.shortcuts import render, redirect
from banks.forms import RegisterForm, UserForum, LoginForm
from . models import Register,Branches,Forum
from django.contrib.auth import authenticate,login
# Create your views here.


def home(request):
    districts=Branches.objects.values_list('district', flat=True).distinct()
    print(districts)
    return render(request, "home.html",{'dist':districts})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            print("user",username)
            if Register.objects.filter(username=username).exists():
                return render(request, 'register.html', {'form': form, 'error_message': "Username already exists"})
            else:
                user = form.save(commit=False)
                user.password = form.cleaned_data['password']
                user.save()
                return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def forum(request):
    name = request.session.get('username')
    print(name)
    initial_data={
        'username': name
    }
    form = UserForum()
    if request.method == 'POST':
        form = UserForum(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect('/accept')
        else:
            print(form.errors)
    else:
        form = UserForum(initial=initial_data)
    return render(request,'forum.html', {'form': form})

def accept(request):
    return render(request,'accept.html')

def login(request):
    msg=None
    form=LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username1 = form.cleaned_data['username']
            password1 = form.cleaned_data['password']
            print((username1, password1))
            if Register.objects.filter(username=username1).exists():
                try:
                    user = Register.objects.get(username=username1, password=password1)
                    print(user)
                    if user is not None:
                        if(Forum.objects.filter(username=username1).exists()):
                            return redirect('/')
                        else:
                            request.session['username']=username1
                            return redirect('/fill')
                    else:
                        form.add_error(None, "Invalid user")
                except:
                    msg = "Invalid Password"
            else:
                msg = "User does not exist"
    return render(request,'login.html', {'form': form, 'msg': msg})

def fill(request):
    return render(request,'fill.html')



