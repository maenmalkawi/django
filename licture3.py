# we need to build models

# first we write in models.py>> class -name for class-(models.model) ((these calls inheritance))

# then we take variable for the class like (name,phone,email,age .....)(then we select the type for each one)

# name = models.charFields(maxlength=15)(phone = models.decimalFields(max_digits=20 , decimal_places=2(كم فاصله عشريه بتحتاج)))

# if we have any change for models we use (python3 manage.py makemigrations(we sued for build django banal), python3 manage.py migrate)

# then we run server

# then we have to show models in main adminbanal for do this we can do some codes :

# go to admin.py >> from .models import (name of class) 

# then we have to register class by : @admin.register(name of class) /n // class(name for class admin(admin.ModelAdmin):)

# then list_display = we write the variable ('name','phone','email'...)

# we can hide any variable in main banal users by delete in in the list_display but when you enter in class in banal you can see it.
 
