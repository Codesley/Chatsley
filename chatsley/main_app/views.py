from django.contrib.auth import login 
from django.shortcuts import render,redirect
from .forms import SignUp

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid(): #is_valid makes sure that the passwords are matching and username doesn't exist 
            user = form.save() 
            login(request,user)
            return redirect('homepage') 
    else: 
        form = SignUp()  

    return render(request, 'signup.html', {'form':form})