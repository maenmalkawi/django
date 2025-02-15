# first we dived a page for two user : 1.manegar 2. client
# create manegar.html >> 
# open views.html >> add from .models import Users , Car >> add to under def(home) :Cars = Car.objects.all() 
# then go to context add cars >> then go to home.html after clear all info in context add
# {% for i in Cars %} >> <h2> {{i.title}} </h2> >> <p> {{i.description}} </p> {% endfor %}
# for  # Check if the logged-in user is in the 'manager' group
#   is_manager = request.user.groups.filter(name='manager').exists()
#    print(f"Is manager: {is_manager}")
# then go to manager.html add {{user.username}} {{user.groups.all.0}} 
# for build manegar.html take cards from bbotstrab and grid it then to add something
# # new html page like addbook.html then add this {%extends "base.html"%} 
# {% block title%}
# <title> ADD CARS </title>
# {%endblock%} 

# {% block contant %}
# <form>
#     <div class="form-group">
#       <label for="exampleInputEmail1">Email address</label>
#       <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
#       <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
#     </div>
#     <div class="form-group">
#       <label for="exampleInputPassword1">Password</label>
#       <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
#     </div>
#     <div class="form-check">
#       <input type="checkbox" class="form-check-input" id="exampleCheck1">
#       <label class="form-check-label" for="exampleCheck1">Check me out</label>
#     </div>
#     <button type="submit" class="btn btn-primary">Submit</button>
#   </form>
# {%endblock%} 


# then go to views.html add new login reqired (@login_required(login_url='login'
# def addcars(request) :
#     user = request.user
#     if user.groups.filter(name='manager').exists():
#         pass
#     else:
#         return HttpResponse("YOU DONT HAVE PERMISSION TO ADD CAR"))

   
# then go to urls.py add new path (path('addcars/',addcars,name='addcars'),)
 