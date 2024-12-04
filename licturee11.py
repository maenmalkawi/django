# in this licture we made a login for user in html page
#  first go to urls.py in newdjango(name file is new django) and add to path this : (path('accounts/', include('django.contrib.auth.urls')),)
# in templates make folder name regestriation and in this file make file html login.html
# then put any form login like this <form method="POST" action="{% url 'login' %}">
#           
#             {% if form.errors %}
#           <p style="color:red"> your password  or username didn't match. please try again</p>
#        {% endif %}  (this for if password or any thing does not exists )
# 
#           {% csrf_token %}
#            <table>
#                <tr> 
#                    <td>{{form.username.label_tag}} </td>    
#                    <td>{{form.username}} </td>    
#                </tr>
#                <tr> 
#                    <td>{{form.password.label_tag}} </td>    
#                    <td>{{form.password}} </td>        
#                </tr>
#                <tr> 
#                    <td><input type="submit" value="login"></td>    
#                </tr>
#            </table>
#        </form>
#  
# then go to setting.py  under default_auto_field add this
# LOGIN_REDIRECT_URL = 'name for html u need when customer click submit in login we moved in ' 
# >> and add LOGIN_URL="login" thats do where u need the customer go after press a login button 

# we need logout buuton go to base.html page that have a navbar add button after 
# add logout button go to setting.py add (LOGOUT_REDIRECT_URL = "login")
# if we had to but login nessecary go to view.py before  def(home) :
# add login required to this view (@login_required(login_url='login'))
# and import it from django (from django.contrib.auth.decorators import login_required))  
# in bootstrab if we get a form we have do some edit : 
# 1. user name edit the input type to text and add name="username"
# 2. password edit the input type to password and add name="password"
# 3. submit button edit type to submit

# if we had to show the user name in nave bar just add {{user.username}} in any fields 