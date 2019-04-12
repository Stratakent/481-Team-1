import subprocess
import random
import randint
from _random

# test edit
def main():
#this will be the AI trained to receive and destroy the image via photoshop
    class AI_creator:
        #get the photo from a selected library
        pic=open(##path to file##)
        #open it in photoshop or paint; your call
        paint=r'#path to file'
        subprocess.Popen("%s %s"%(paint,pic))
        #get photoshop or paint to add in a smudge onto the photo... randomly, flip a coin or something i dunno.
        coinflip=(randint(0,1))
        #figure out how to do that
        if coinflip==1:
            #defile image
            #state=1(true)
        else:
            #nothing

        #save the changes into a new library.
        pic.close()

#this will be the AI that will be trained to recognize an image is photoshopped or not.
    class AI_recognizer:
        #open the new photo in the new library
        #attempt to compare the new photo with the original and determine if its real or fake.
        #If it's real or fake, announce so.
        if state==1:
            print("Image is a poorly made fake!")
        else:
            print("Image is a genuine copy!")
        #do something, like mentally slap the user or something...
