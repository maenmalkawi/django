# user authentication and permission : Distribution of roles and powers within the website
# CRUD : C >> CREATE (POST) , R >> READ (GET) , U >> UPDATE (PUT) , D >> DELETE
# GO TO MODELS.PY and take the models and start divide to this three part
#  IN DJANGO THE authentication and permission Divided in 3 part : 
#    
#   1. ADMIN : crud            2. CLIENT : R , p >> in instance        3. MANEGAR >> crud 

# django build automatically all this in django banel   thats name is (GROUP)
# FIRST start create group like client and manegar and start give him the permission
# then create a user and give him staff status (active) and choose what type for this user ( manger or client) 