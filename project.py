import subprocess
import random
import randint
from _random

def main():
#this will be the AI trained to receive and destroy the image via photoshop
    class AI_creator:
        #get the photo from a selected library
        pic=open(##path to file##)
        #open it in photoshop or paint; your call
        paint=r'#path to file'
        subprocess.Popen("%s %s"%(paint,pic))
        #get photoshop or paint to add in a smudge onto the photo... randomly, flip a coin or something i dunno.
        coinflip=(randint(0,1))     #Might want to introduce more randomness so that the AI does more interesting things
        #figure out how to do that
        if coinflip==1:
            #defile image
            #state=1(true)

            #Ideas of edits
            # Horizontal Line Top
            # Horizontal LIne Bottom
            # Vertical Line Top
            # Vertical LIne Bottom
            # Diagnol Top to Bottom
            # Diagnol Bottom to Top
            # Draw a Circle
            # Random Coloring
            # Turn everything one color
            # Replace with anotehr picture
        else:
            #nothing

        #save the changes into a new library.
        pic.close()

#this will be the AI that will be trained to recognize an image is photoshopped or not.
    class AI_recognizer:
        #open the new photo in the new library
        #attempt to compare the new photo with the original and determine if its real or fake.
        #If it's real or fake, announce so.

        # Might want to change it so it guesses the edits
        # To do this we shoudl see see which pixels are likely to change between two pictures
        # and Create an alogrithm where it decides which of the pixels to go to based on what difference
        # are found?
        if state==1:
            print("Image is a poorly made fake!")
        else:
            print("Image is a genuine copy!")
        #do something, like mentally slap the user or something...
