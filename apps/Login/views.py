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
        request.session['user_id'] = user.id
        request.session['first_name'] = request.POST['first_name']
        errors["success"] = "Successfully registered (or logged in)!"
        return redirect('/dashboard')

def process_login(request):
    errors = User.objects.login_validator(request.POST)
    email = User.objects.filter(email=request.POST['email']).all()
    HashPass = request.POST['password']
    for item in email:
        print HashPass
        if bcrypt.hashpw(HashPass.encode(), item.password.encode()):
            request.session.modified = True
            request.session['email'] = item.email
            request.session['user_id'] = item.id
            request.session['first_name'] = User.objects.get(email=request.session['email']).first_name
            print "Password Match"
            print request.session['email']
            return redirect('/dashboard')
        else: 
            print "Passwords do not match"
            messages.add_message(request, messages.INFO, 'Your password is incorrect')
            return redirect('/')

def dashboard(request):
    me = User.objects.get(id=request.session['user_id'])
    context = {
	'item_query': Item.objects.all(),
    'my_list': Item.objects.filter(wished_by=me),
    'not_my_list': Item.objects.exclude(wished_by=me)
    }
    return render (request, 'Login/dashboard.html', context)

def wish_list(request, item_id):
    wish = Item.objects.get(id=item_id).wished_by.all()
    context = {
    'item_query': Item.objects.filter(id=item_id),
    'item': Item.objects.get(id=item_id),
    'wish': wish
    }
    return render (request, 'Login/wish_list.html', context)

def create(request):
    print "test here1"
    return render (request, 'Login/create.html')

def createItem(request):
    print "test here"
    product = request.POST['item']
    user = User.objects.get(id=request.session['user_id'])
    items = Item.objects.create(
        item = product,
        added_by = user,
    ) 
    items.wished_by.add(user)
    print "and here"
    return redirect('/dashboard')

def addItem(request, item_id):
    Item.objects.addItem(item_id, request.session['user_id'])
    return redirect('/dashboard')

def removeItem(request, item_id):
    Item.objects.removeItem(item_id, request.session['user_id'])
    return redirect('/dashboard')

def deleteItem(request, item_id):
    b = Item.objects.get(id=item_id)
    b.delete()
    return redirect('/dashboard')