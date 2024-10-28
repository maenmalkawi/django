# we have to use static data for use css in my project 

# first we go to google search django static file in w3school then go to >> setting.py in file >> then see static url

# then make folder in template thats name is static and inside static make css file

# go to the html file and add before <head> {% load static %} 

# in the link rel="style sheet" href="{% static 'css/home.css'  %}"

# if the program not run take the static file and put in outside template and put in near the manage.py

# if the program still not work go to google and search whiteNoise w3school

# pip install whiteNoise then

# go to setting.py >> in (middleWear) add this package

# then go to setting.py >> search the static_url >> under static_url add (STATIC_ROOT=[BASE_DIR/'static'])

# after it in the terminal write (collect static)

# go to the setting.py make debug=False // allowed_hosts=[]'*'] (We make the debug=true for check the error in our website)

# then check if the file active >> then run server to check

# we make moduls.py >> in this model we put information like (name,phone,....) and this information have a propareties (decimalFields,charFields)

# in moduls we make class name (models.model) : phone = charFields(max_length=10) >> def__str__(self): return self.phone

# then we go to view.py >> from .models import class name >> then go to the function and definiton variable like users= users.object.all()for give me all users

# then save it in context "users":users (context use for give all information to html part)

# then in html file we make for loop {% for user in users %} >> <p> Users: {{user.name}} </p> {% end for %} we used for loop to show the data
