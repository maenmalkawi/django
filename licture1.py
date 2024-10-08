# view >>>> module >>>> template >> urls



# ls>> list use fto show what the file and folder in project

# mkdir >> create folder 

# cd >> use for move betweeen folder by in the folder by write (cd name for mkdir) ئ

# venv work inviroment(بيئه العمل)


#we start every project from here 

# # (python3 -m venv namefor the enviroment ) use for use for create the vitual enviroment

# source envir(name for the enviroment)/bin/activate  active the file we are work in

# pip install django  for download django framework

# django-admin startproject name of project(without space) for start django project

# python3 manage.py runserver  use for run server and show the django project in google from ise the url that give you

#python3 manage.py -h (use to show that commands we need in project)

# code . >> use for open django in vscode

# python3 manage.py startapp library open folder thats name is library in vscode(use to create app lie : car , library .....)

# we go to make connection between app and django project by :
# 1. go the django project and open setting.py >> go to instaled apps and add theic name(like : car , library...)
# 2. go to django project and oper urls.py >> search for the import sentence and add include for (from django.urls import path,(include))

# then go to the path in setting.py >> urls patterns >> add new path >> path('name like car ,library ...',include(car,library ...))

# the go to the projectname(like : library or car...) the go the >> view.py>> add (from django.http import HttpResponse) under import django.short  
# then >> make fuction (def name (request): /n HttpResponse('welcome to the (car,library.. )apps))

# then create file in (car or library ..)thats name is (urls.py) and type in file
# A.from .view import * // from django.urls import path the go to the urls in django project>> urls.py>> copy all patterns >> paste in the file
# >> clear all of the in pattern = {path('home/',home,name='home' )}

##../enviro/bin/activate (dot dot mean back) 

#summary: venv> activate > isntall django > startproject > code . > startapp > setting.py-(app) > urls (1.proj , 2. include(car.lib..))
# > view(function,https) > create urls.py > path home > run server
  