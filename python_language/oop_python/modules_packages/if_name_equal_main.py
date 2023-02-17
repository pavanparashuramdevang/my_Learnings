'''
you have seen a statement like 

if __name__ == "__main__":
    do something


you may ask why they are written and what is the use case,is it necessary or we can ignore it

it is necessary and good practice in python programming

consider a file which is made specifically to import as module by other python programs

db.py

class Database:
    pass
    

#it does initialize the database there only 
database=Database()

we don't want that so we write a specific funcion to initialize that for us

def init_database():
    global database
    database=Database()
    print("database initialized")

it works only when the function is explicitly called by user


consider when you want to run this db.py file on its own it initalizes the db
'''


class Database:
    print("this is database ")
    print("init from Database")

#database=Database() #if name== main is commented this initializes the database

def init_db():
    print(f"first module name is {__name__}")#python sets the name variable to __main__
    global db 
    #db=Database()
    print("db init from init_db")



if __name__=="__main__":
    print("this is run in main")

else:
    print("this is run when imported ")
