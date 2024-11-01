# first we will start build the main class in models .
# class name extends from (models.model) >> class maen(models.model):
# then add attribute for each class like : name , db , dt . . ... .
#class name(models.model):
#    fName = models.charfields(max_length=20 verbose_name اسم بديل="first name")
# ordering ترتيب >> class Meta: /n >> ordering = ['db']
# then wwe print the __ str __ >> def __str__(self): return self.fname+ self.lname (FOR A STRING)
# always the __STR__ RETURN A STRING
# for a number return f"{self.date}"
# to show it in admin panel we go to admin.py >> add to from .model name of class (from .models import Users (,car))
# then we regester it .
 
# we used foreign key to links 2 things like book and author (models.foreignkey(author),on_delete=models.cascade ( delete all the book to this author when delete the author))
# we used many to many fields to link 1 to many like book and gener (models.manytomanyfields(gener,related_name='book'))
# we used (models.textfields) to big sentences 
# primary key used for special char like>> ID
# we used (on_delete=models.SET_NULL) to delete the instance just.
# we used (on_delete = models.CASCADE ) to delete every thins link with author
  