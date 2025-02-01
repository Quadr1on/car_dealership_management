###########################################################################
# Creating the password:
# In this file you would be able to create the password required for the 
# Admin panel just run the code and enter a password which you want

# In Case you forget the password:
# Just delete the "password.dat" file in the file directory and rerun the
# code and enter a password which you like!!
##########################################################################
import pickle

f = open("password.dat","wb")
e = input("enter password: ")
l=[]
l.append(e)
pickle.dump(l,f)
