# first go to setting.py > templates > write templates in dirs['']

# go to the apps (car,library...)>> make folder and name is templates >> inside folder make html file

# Call the ready code (html5) in html 5 , then give title name(home) , then add (h1'welcome to the home page')

# go the view.py > edit the function by delete httpsResponse >> add render(request,'name for file.html') after return

# (which python3 >> echo $VIRTUAL_ENV )use for know what the rnviroment you use

# then open the terminal in vscode then activate the virtual environment by (source ../enviro/bin/activate) (../ mean back )

# python3 manage.py runserver >> http://127.0.0.1:8000/car/home/

# http://127.0.0.1:8000/admin >> give me error 

# python3 manage.py migration >> make to me db that have Apply all migrations: admin, auth, contenttypes, sessions

# http://127.0.0.1:8000/admin >> give me error fixed and open admin banal

# then write python3 manage.py createsuperuser for user who enter to the admin banal

# enter to user : 
# a. active : this user can open you website 
# b. staff user : this for give the user admin in your website (admin control what you can see)
# superuser status: this for give the user admin in your website(you can control in any thing in the website)

# we usr print under def home(request) in view.py >> to debugging

# if i need to show variable in page >> contaxt={'name':name} in view.py>> then add to the render(request,'name for file.html',contaxt=contaxt)

# then go to html page >> {% use this for logic like if statment %}{% else %} {% end logic %} // {{for variable}}