from django.shortcuts import render, redirect 
from django.contrib import messages
import bcrypt
from models import *

def index(request):
    
    return render(request, 'Login/index.html')

def process_register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        HashPass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=HashPass
        )
        errors["success"] = "Successfully registered (or logged in)!"
        return redirect('/quotes')

def process_login(request):
    errors = User.objects.login_validator(request.POST)
    email = User.objects.filter(email=request.POST['email']).all()
    HashPass = request.POST['password']
    for item in email:
        print HashPass
        if bcrpyt.hashpw(HashPass.encode(), item.password.encode()bcrypt.gensalt())):
            print "Password Match"
            request.session['name'] = item.name
            request.session['user_id'] = item.id 
            print request.session['name']
            return redirect('/quotes')
        else: 
            print "Passwords do not match"
            messages.add_message(request, messages.INFO, 'Your password is incorrect')
            return redirect('/')

def quotes(request):

        return render (request, 'Login/quotes.html')
