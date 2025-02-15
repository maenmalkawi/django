# we have do when we add author add all information in django and go to models and
# run it in  cutomer page
# first add new python page (forms.py) >> from django import forms >> from .models import *
# then create a new class >> 
# class carForms(forms.modelForm):
#    class Meta:
#        model = Car
#        fields = ['CarModel','dateOfIndustry','Engine','gearBox','Wheel']
#        widgets = {
#            'dateOfIndustry':forms.DateInput(attrs={'type':'date'}),
#        } 

# then go to views.py  >> add (from .forms import *)
# then in views.py search for POST add under it form = carForms(request.POST) 
# and in your html page add in forms(<form (method="POST")>)like this >> under it add {% csrf_token %}
# in input sentence add name="CarModel" for all fields  
#under  form = carForms(request.POST) >> print(form) >>   print(form)
                                                        # if form.is_valid():
                                                        #   form.save()
                                                        # in import sentence in the first of page behind request add ,redirect
                                                        #    redirect(to='home')