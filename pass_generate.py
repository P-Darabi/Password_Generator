from termcolor import cprint
import random
import string
import os

settings={
    "Upper": "True",
    "Lower": "True",
    "Number" : "True",
    "Symbol" : "True",
    "Space" : "False",
    "Lenght": "8"
}

PASSWORD_MIN_LENGHT=5
PASSWORD_MAX_LENGHT=30


def get_lenght_of_password(option, default, min_len_of_pass=PASSWORD_MIN_LENGHT, max_len_of_pass=PASSWORD_MAX_LENGHT):
    while True:
        user_choice=input(f'What {option} do you want?! (You should enter a number between {min_len_of_pass} and {max_len_of_pass}, default is {default} ) (enter: default): ')
        if user_choice.isdigit()== True:
            if (min_len_of_pass <= int(user_choice) <= max_len_of_pass):
               return int(user_choice)
        if user_choice=='':
            return default
        print (" The number that you entered is incorrect please try again!")

def getting_yes_or_no_from_user(option, default):
    while True:
        user_input=input(f'include  {option}? (Default is {default}) (y: yes , n: no, enter : default):   ')
        if user_input in ["y","n"]:
            return user_input== "y"  # user_input== "y" --->  true  /////  user_input== "n" ---> false
        if user_input=='':
            return default
        print ("The word that you entered is incorrect please try again! ")



def asking_for_changing_settings(settings):
    while True:
        answer_user= input(" Do you want to change password settings: (yes: y, no: n, enter: yes) : ")
        if answer_user in ["y", "n",""]:
            if answer_user in ["y",""]:
                cprint("               ------------ changing settings -----------", "red")
                get_setting_from_user(settings)
            break
        print(" The word that you entered was incorrect! please try again!")

    
def get_setting_from_user(settings):

    for option, default in settings.items():
        if option != "Lenght":
            user_choice=getting_yes_or_no_from_user(option, default)
            settings[option]= user_choice
        else:
            user_choice= get_lenght_of_password(option, default)
            settings[option]= user_choice

def make_random_char(final_settings):
        choice=random.choice(final_settings)

        if choice == "Upper":
            return random.choice(string.ascii_uppercase)
        if choice == "Lower":
            return random.choice(string.ascii_lowercase)
        if choice == "Number":
            return random.choice(string.digits) 
        if choice == "Symbol":
            return random.choice(string.punctuation)                     
        if choice == "Space":
            return ' '
            
def password_generate(settings):
    password_lenght= settings["Lenght"]
    final_settings=[]
    final_settings= list(filter(lambda x: settings[x]== "True", ["Upper", "Lower", "Number" ,"Symbol" ,"Space"]))
    # for key, value in settings.items(): 
    #if value == "True":   
    #final_settings.append(key)
    list_of_pass=''
    for i in range(int(password_lenght)):
            list_of_pass+=make_random_char(final_settings)
    return list_of_pass

def password_generator_loop(settings):
   while True:
       cprint("----------------------", "blue")
       print(f'YOUR PASSWORD IS :  {password_generate(settings)}')
    
       while True:
           user_input= input("Do you want another password?  (yes: y, no: n , enter: yes):  ")
           if user_input in ["y", "n", ""]:
               if user_input=="n":
                   return
               break
           print ("The Word that you entered is incorrect please try again!")  
        
def Run():
    os.system("cls")
    cprint("--------------------- Welcome To Password Generator App --------------------------", color= "red")
    asking_for_changing_settings(settings)
    password_generator_loop(settings)
    cprint(text= "         -------------- Thank you for choosing us ----------------" , color="red")
    

Run()