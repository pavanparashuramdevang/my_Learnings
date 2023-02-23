'''
what is polymorphism 

its simply differnt behaviours happen depending on subclass 

python doesn't really support polymorphism,we call polymorphism in python as duck typing

what is duck typing

python allows us to use any object that provides the required behaviour without forcing it to be subclass

in polymorphism, it need to be a subclass to work,but in duck typing if it has enough similer arguments
and its called upon any class it works you may think it's good but in actuality it's really not that good

one use of duck typing is you don't really need inheritance as duck typing solves inheriting from public
interface so you just need duck typing
'''

class audio_file():
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            print("invalid file extension")
        else:
            self.filename=filename


class mp3_file(audio_file):
    ext='mp3'
    def play(self):
        print(f"playing {self.filename}")


#duck typing

class flacfile():
    def __init__(self,filename):
        if not filename.endswith(".flac"):
            print("invalide format")

        else:
            self.filename=filename

    def play(self):
        print(f"playing {self.filename}")


mp3file=mp3_file("abc.mp3")
mp3file.play()

flacaudio=flacfile("abc.flac")
flacaudio.play()


"""
there is another important concept to regulate the duck typing by a class
its called Abstract Base Class i.e ABC which tells that a class must implement these set of properties
and methods to be considered as a duck typable  class

which is hard and require knowledge of decorators and design pattern so I will explain about this in that
place

"""