import subprocess
import random
import image
import webbrowser
from PIL import Image, ImageDraw, ImageColor

def main():
    # this will be the AI trained to receive and destroy the image via photoshop
    
    AI_creator()
    AI_recognizer()

def AI_creator():
    # might require the PILLOW extension for image drawing.
     # get the photo from a selected library
        # open via PILLOW module
        # get photoshop or paint to add in a smudge onto the photo... randomly, flip a coin or something i dunno.
    img = Image.open("testimage.jpg")
    pix = img.load()
    i = 0
    while i < 3:
        # img.size as referenced multiple times in the code below gets the image sizes of the x and y coordinates.
        diceroll = (random.randint(1, 20))  # Might want to introduce more randomness so that the AI does more interesting things
        color = PIL.ImageColor.getrgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if diceroll == 1:
            # Horizontal Line Top
            pix = ImageDraw.Draw(img)
            pix.line((0, 0, img.size[0], 0), color, 2)
        if diceroll == 3:
            # Horizontal LIne Bottom
            pix = ImageDraw.Draw(img)
            pix.line((0, img.size[1], img.size[0], img.size[1]), color, 2)
        if diceroll == 5:
            # Vertical Line LEFT
            pix = ImageDraw.Draw(img)
            pix.line((0, 0, 0, img.size[1]), color, 2)
        if diceroll == 7:
            # Vertical LIne RIGHT
            pix = ImageDraw.Draw(img)
            pix.line((img.size[0], 0, img.size[0], img.size[1]), color, 2)
        if diceroll == 9:
            # Diagnol Bottom Left to Top Right
            pix = ImageDraw.Draw(img)
            pix.line((0, img.size[1], img.size[0], 0), color, 2)
        if diceroll == 11:
            # Diagnol Bottom Right to Top Left
            pix = ImageDraw.Draw(img)
            pix.line((0, 0, img.size[0], img.size[1]), color, 2)
        if diceroll == 13:
            # Cross over image
            pix = ImageDraw.Draw(img)
            pix.line((0, img.size[1] / 2, img.size[0], img.size[1] / 2), color, 2)
            pix.line((img.size[0] / 2, 0, img.size[0] / 2, img.size[1]), color, 2)
        if diceroll == 15:
            # Rotate image
            pix.rotate(90)
        if diceroll == 17:
            # Turn everything one color
            pix.paste(color, 0, 0, image.size[0], image.size[1])
        if diceroll == 19:
            # Replace with another picture
            pix.close()
            im2 = image.open("testimag2.jpg")
            pix = im2.load()
        # if diceroll==20:
        # This one is for fun... just don't click the link.
        # webbroswer.open_new_tab('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        i = i+1
        # save the changes into a new library.
    pix.save("testcopy.jpg")
    print("Using Creator...\n")

# this will be the AI that will be trained to recognize an image is photoshopped or not.
def AI_recognizer(image1,image2):
    state = 0
    # open the new photo in the new library
    # attempt to compare the new photo with the original and determine if its real or fake.
    # If it's real or fake, announce so.
    # might need state space to look like we did more than we did.
    # Might want to change it so it guesses the edits
    # To do this we shoudl see see which pixels are likely to change between two pictures
    # and Create an alogrithm where it decides which of the pixels to go to based on what difference
    # are found?
    
    # Checks for rotation
    if image1.size[0] != image2.size[0]:
        result(state)
    if image1.size[1] != image2.size[1]:
        result(state)
    x=0
    y=0
    
    # Iterate though every pixel
    # If not equal images do not match
    # Else they are equal

def result(state):
    if state == 1:
        print("Image is a poorly made fake!")
        
    else:
        print("Image is a genuine copy!")

    

