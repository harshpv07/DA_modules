import os

#for ML related projects
#folder_name -> name of the folder to be saved
#venv -> do you need a venv or not
#name ->name of the main python file
#path ->path of the folder of the project 
def ML(fold_name,venv,name,path):
    if(venv == 1):
        os.system("pip install virtualenv")
        os.system("cd " + path + "&& mkdir " + fold_name + "&& cd " + fold_name + "&& touch " + name)
        venv_name = input("Enter the name of the venv: ")
        if(os.name != "nt"): #for ubuntu
            os.system("cd " + path + "&& cd " + fold_name + "&& virtualenv " + venv_name + "&& . " + venv_name+"/bin/activate " + "&& pip install -r /home/harsh/Documents/DA_modules/requirements/ml.txt")
            print("VENV Sucessfully created and activated")
    else:
        print("Not created")

def Django(fold_name,venv,name,path):
    if(venv == 1):
        os.system("pip install virtualenv")
        os.system("cd " + path + "&& mkdir " + fold_name + "&& cd " + fold_name)
        venv_name = input("Enter the name of the venv: ")
        if(os.name != "nt"): #for ubuntu
            os.system("cd " + path + "&& cd " + fold_name + "&& virtualenv " + venv_name + "&& . " + venv_name+"/bin/activate " + "&& pip install -r /home/harsh/Documents/DA_modules/requirements/django.txt " + "&& django-admin startproject " + fold_name)
            print("VENV Sucessfully created and activated")
    else:
        print("Not created")

def react(fold_name,venv,name,path):
    if(venv == 1):
        os.system("sudo apt-get install curl && curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash - && sudo apt-get install nodejs")
        os.system("cd " + path + "&& mkdir " + fold_name + "&& cd " + fold_name)
        # venv_name = input("Enter the name of the venv: ")
        if(os.name != "nt"): #for ubuntu
            os.system("cd " + path + " && cd " + fold_name + " && npx create-react-app " + name )
            print("VENV Sucessfully created and activated")
    else:
        print("Not created")



if __name__ == "__main__":
    #ML(input(),1,"main.py",input()) 
    #Django("new_django_project",1,"hello","/home/harsh/Desktop")
    react("new_react_project",1,"react_app","/home/harsh/Desktop")
