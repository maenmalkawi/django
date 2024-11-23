# in this licture we made a login for user in html page
#  first go to urls.py in newdjango(name file is new django) and add to path this : (path('accounts/', include('django.contrib.auth.urls')),)
# in templates make folder name regestriation and in this file make file html login.html
# then put anu form login like this <form method="POST" action="{% url 'login' %}">
#           
#             {% if form.errors %}
#           <p style="color:red"> your password  or username didn't match. please try again</p>
#        {% endif %} 
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
# 
#
#