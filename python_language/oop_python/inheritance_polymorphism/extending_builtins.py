'''
there are built in classes like lists and dictionaries etc
are also we can extend like providing additional functionality to that list

'''

class contactlist(list): #before we used to have used list but now we use this class which we created
    #to satisfy our needs like searching name instedad of object
    def search(self,name):
        #[1,2,3] consider this as the contact list
        matching_contacts=[]

        for contact in self:#this traverses self means all contacts [1,2,3]
            if name in contact.name:
                matching_contacts.append(contact)
            
        return matching_contacts
    

    #now this is extended and return matching contact name when searched


class contact():
    all_contacts=contactlist()#you need to call this on class as it is considered as class variable

    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.all_contacts.append(self)
        


a=contact('pavan','pavan@gmail.com')
b=contact('abc','abc@gmail.com')
c=contact('va','va@gmail.com')



#like this you can also extend dictionaries or any other class to your needs



'''
another important concept is overriding super
in the extending builtins we added new behaviour to our class  that means we completly change or rewritten
the behaviour

there may question what about changing behaviour 

adding behaviour means, in our contact class we have values like name and email, what about adding 
phone numbers to only we required like friends and family

'''

# class friend(contact):
#     def __init__(self,name,email,phone):
#         self.name=name
#         self.email=email
#         self.phone=phone

'''
the above code works but it becomes messy while maintaining code 

super() allows us to call parent method directly

'''

class friend(contact):
    
    def __init__(self,name,email,phone):
        super().__init__(name,email)#there is no self part because super method handles all
        self.phone=phone

    
friend1=friend('pav','ghi@gmail.com','1333')

match_list=contact.all_contacts.search('pa')

for obj in match_list:
    print(obj.name)
    print(obj.email)

