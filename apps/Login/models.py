from __future__ import unicode_literals
import re
import bcrypt
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if (len(postData['first_name']) < 1) or (len(postData['last_name'])
                < 1) or (len(postData['email']) < 1):
            errors["blank"] = "All fields are required and must not be blank!"
        if not (postData['first_name'].isalpha() and postData['last_name'].isalpha()):
            errors["alpha"] = "First and Last Name cannot contain any numbers!"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid Email Address!"
        if len(postData['password']) < 8:
           errors['password_length'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirmPW']:
           errors['confirmPW'] = "Passwords do not match"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        email = postData['email']
        password = postData['password']
        if User.objects.filter(email=email).count() == 0:
            errors['email'] = "email {} not in database".format(email)
        print errors
        if User.objects.filter(email=email).count() == 1:
            current_user = User.objects.get(email=email)
            checkedPW = bcrypt.checkpw(password.encode(), (current_user.password).encode())
            if checkedPW == False:
                errors['password'] = "wrong password."
        return errors
        

class User(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=35)
    hired = models.DateField(auto_now = False, auto_now_add= False, default='2000-01-01')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

    def __unicode__(self):
        return "id: " + str(self.id) + ", first_name: " + self.first_name + \
        ", last_name: " + self.last_name + ", email: " + self.email + \
        ", password: " + self.password

class ItemManager(models.Manager):
    def addItem(self, item_id, user_id):
        me = User.objects.get(id=user_id)
        item = Item.objects.get(id=item_id)
        item.wished_by.add(me)
    
    def removeItem(self, item_id, user_id):
        me = User.objects.get(id=user_id)
        item = Item.objects.get(id=item_id)
        item.wished_by.remove(me)

class Item(models.Model):
    item = models.CharField(max_length=50)
    added_by = models.ForeignKey(User, related_name="Item")
    wished_by = models.ManyToManyField(User, related_name='wished_by')
    date_added = models.DateField(auto_now_add=True)
    objects = ItemManager()
