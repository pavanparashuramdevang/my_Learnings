'''
python doesn't enforce any law on what is private public or protected like othe object oriented programming
languages, instead it provides some guidelines and best pracices for what to do with variable


every_variable name is public by default

you can specify _ underscore at the bigining of the variable name 
that suggest that this is not supposed to be called directly, it can't denay you from accessing it

__ double underscore at the begining of variable name, storngly suggest that you are not supposed to 
call that variable directly,it makes some "name mangling" means changes name to (_classname+variablename)

'''


class secrate_string():

    def __init__(self,plain_text,password):
        self._private="this is private string"
        self.__plain_text=plain_text
        self.__password=password

    
    def decrypt(self,password):
        if password==self.__password:
            print(f"your secrate text is : {self.__plain_text}")
        else:
            print("wrong password")

secrate=secrate_string("this is secrate string","1234")

secrate.decrypt("1234")
#it prints the secrate string but direct access is not allowed like

#print(secrate.__plain_text)  #it provides a attribute error because the name is changed to something else

print(secrate._secrate_string__plain_text)  #it doesn't provide error its _classname+varname

print(secrate._private)


#there is another concept which is third party libraries

"""
you need to have pip installed on your device to install third party libraries 

you can makesure pip installed or not by command

>>> python -m ensurepip

run it as module

you can intstall from pip using 

>>> pip install lib_name

you need to search the internet to find the required name 

>>> pip list

it is used to check the installed libraries

virtual environments are very essential concepts of python

I mostly use virtualenv but venv comes preinstalled on python 

>>>python -m venv environ_name
>>> source environ_name/bin/activate   #for linux and macos

>>> env/bin/activate.bat  #you can run that bat file on windows

"""