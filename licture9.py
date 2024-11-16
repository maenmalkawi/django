# session : ( is a way to store and manage data across multiple 
# requests made by the same user during their interaction with a web application. 
# It allows the server to recognize and remember user information, like login status, preferences, and other temporary data.)

# first go to views.py >> in def(home) make a session that show the user how many he view the home page.

# then create a variable that store number of views >> (number_of_views = request.session.get('number_of_views' = (if u found number take this) ,0 = (if u dont found make the value 0)))

# then increment number of views  >>  (   request.session['number_of_views']=number_of_views +1)

# then in context add >> "number_of_views": number_of_views,

# then in home.html we can add any thing in context like(<h1> welcome to the home page you visit the page {{number_of_views}} time </h1>)

# if we have a button we make this step to work the session >>    change_logo= request.session.get('change_logo',0)
# then>> if request.method =='POST':
#           print('post request')
#           request.session['change_logo'] = change_logo +1
      
#            pass 

# then add it in context 

# then in home.html in context add  <form method="post">
#                                     {% csrf_token %}
#                                     <button type="submit"> change logo </button>
#                                   </form>    
#                                   <h2> you change the logo {{ change_logo }} time </h2>

# CSRF token is a security measure used in web applications to prevent unauthorized actions by verifying that requests are intentionally made by authenticated users, 

# go to console then (>>) application then cookies


 