# first to use html in django go to template then new folder.html
# write html5 then delete a <title>>> write this  for write a title you used {% block title%}name of title {%endblock%}
# then make div in body and giv it id for style  <div id="">      </div>
# for add bootsrap you should write in terminal pip install bootstrap-5 then go to setting.py >> installed app >> add >> 'bootstrap5',
# then add this under title >> {% load bootstrap5 %} >> {% bootstrap_css %} >> {% bootstrap_javascript %}
# under end div write {% block contant%}{% endblock %}
# to do connection between al lot of html page you should used {%extends "base.html"%} (the page you do it main)
# then write {% block title%}<title> home </title> {%endblock%} to give you the title on that base.html have oit 
# for create new page go to view.py >> def name(request): 
#                                           return render(request,'name.html')
# then go to urls.py >> urlpatterns >> path('news',news,name='news')
# then new html file name.html
# if you have a url href  in django the best way in href= add "{%url 'name'%}"
# to add image in django >> static file >> new folder(images) >> put the img inside it 
# under extends put {% load static %} >> in contant >> <img src= " {% static 'images/name pic'  %} "  /> 
# for active js in django make file in static name.js >> in contant add <script src="{% static 'js/name.js'  %}"></script>
# for add slider in django >> slider.html >> then git all inf in base.html >> then views.py >> like create new page in line (8,9,10,11)  
# for fet your project in gitHup from terminal  1.git add .  >> 2.git commit -m "..."   >> 3.git push -u origin main  