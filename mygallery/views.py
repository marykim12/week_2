from django.shortcuts import render,redirect,get_object_or_404
from .models import Photo
from .forms import LoginForm
from .forms import AddPhotoForm
#from .forms import userregistrationform
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
@login_required(login_url='login_user')
def index(request):
    photos = Photo.objects.all()
    ctx = {'photos': photos}
    return render(request, 'index.html', ctx)


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password')
    context = {'loginform':form}
    
    return render(request, 'login_user.html', context=context )

def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                 form.save()
                 return redirect('login_user')
        else:
             form = UserCreationForm()
    
        return render(request,'signup.html', {'form':form})

@login_required(login_url='login_user')
def add_photo(request):
     #print("View function accessed")
     if request.method == 'POST':
          form = AddPhotoForm(request.POST, request.FILES)
          if form.is_valid():
               print("form is valid")
               photo = form.save()
               return redirect('photo_details',photo_id = photo.id)
          else:
               print("form not valid")
               print(form.errors)
     else:
          print("get method detected")
          form = AddPhotoForm()
     print("form created")
     return render(request ,'add_photo.html', {'form':form})


@login_required(login_url='login_user')
def photo_details(request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        print(photo.image.url)
        return render(request, 'photo_details.html', {'photo': photo})

@login_required(login_url='login_user')    
def logout_user(request):
    logout(request)
    messages.success(request, ('You are now logged out..'))
    return redirect(request, '')








