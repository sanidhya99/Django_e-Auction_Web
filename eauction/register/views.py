from django.shortcuts import render
def homePage(request):
    
    return render(request,"index.html", {'navbar':'Home'})
def aboutUs(request):
     return render(request,"aboutus.html", {'navbar':'About Us'})
def login(request):
    return render(request,"registration/login.html", {'navbar':'Login'})
def signup(request):
   form=SignupForm()
   return render(request,"registration/signup.html",{"form":form}, {'navbar':'SignUp'})
# Create your views here.
