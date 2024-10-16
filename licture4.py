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
