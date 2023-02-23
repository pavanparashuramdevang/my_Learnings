"""
as I said earlier, we have seen how to raise exceptions and how to control it
but how can we define our own Exceptions

for that you have to inherit from class called Exception

which is a base which provide all the interface


"""

class ourException(Exception):
    pass


print("before raising exception")
#raise ourException("invalid entry")

"""
what, you may say thats same as raise Exception 
yes thats same as raise Exception but instaed of just pass we can define something 
"""

class Invalid_withdrawel(Exception):
    def __init__(self,balence,ammount):
        super().__init__("you have insufficient balence")
        self.ammount=ammount
        self.balence=balence

    def overage(self):
        return self.balence-self.ammount


print(Invalid_withdrawel(20,10).overage())