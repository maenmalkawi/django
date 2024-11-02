# now we will add a search fields in django by using list_filter
# we go to admin.py >> in class i need to put search in under list_display (list_display = ('book',))
# or we use a a search_fields = ['book']
# for Split screen into two parts we used the fieldsets =  fieldsets = (
#                                                                    (None,
#                                                                        {'fields' : ('Id','book')}),
#                                                                        (availabilty,
#                                                                   {'fields':('status',)}),
#                                                                    )
#
# we can put any class in other class in django banal like we pyt book instance in book by using INLINES
# FIRST WE MADE class bookInstanceInlines(admin.TabularInline) :
#   model = bookInstance
# then in class book >> inlines = [bookInstanceInlines]
#
#
#
#
#
#
#
#