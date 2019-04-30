import subprocess
from random import randint
import image
import webbrowser
from PIL import Image, ImageDraw

def main():
    img1 = Image.open("testimage.jpg")
    AI_creator(img1)
    img2 = Image.open("testcopy.jpg")
    img2.show()


def AI_creator(img):
    # might require the PILLOW extension for image drawing.
    # get the photo from a selected library
    # open via PILLOW module
    # get photoshop or paint to add in a smudge onto the photo... randomly, flip a coin or something i dunno.
    i = 0
    while i < 3:
        # img.size as referenced multiple times in the code below gets the image sizes of the x and y coordinates.
        R=randint(0,255)
        G=randint(0,255)
        B=randint(0,255)
        diceroll = (randint(1,20))  # Might want to introduce more randomness so that the AI does more interesting things
        print(diceroll, "\n")
        draw = ImageDraw.Draw(img)
        if diceroll == 1:
            # Horizontal Line Top
            draw.line((0, 0, img.size[0], 0), fill=(R,G,B),width=20)
        if diceroll == 3:
            # Horizontal LIne Bottom
            draw.line((0, img.size[1], img.size[0], img.size[1]), fill=(R,G,B),width=20)
        if diceroll == 5:
            # Vertical Line LEFT
            draw.line((0, 0, 0, img.size[1]), fill=(R,G,B),width=20)
        if diceroll == 7:
            # Vertical LIne RIGHT
            draw.line((img.size[0], 0, img.size[0], img.size[1]), fill=(R,G,B),width=20)
        if diceroll == 9:
            # Diagnol Bottom Left to Top Right
            draw.line((0, img.size[1], img.size[0], 0), fill=(R,G,B),width=20)
        if diceroll == 11:
            # Diagnol Bottom Right to Top Left
            draw.line((0, 0, img.size[0], img.size[1]), fill=(R,G,B),width=20)
        if diceroll == 13:
            # Cross over image
            draw.line((0, img.size[1] / 2, img.size[0], img.size[1] / 2), fill=(R,G,B),width=20)
            draw.line((img.size[0] / 2, 0, img.size[0] / 2, img.size[1]), fill=(R,G,B),width=20)
        if diceroll == 15:
            # Rotate image
            img = img.rotate(90)
        if diceroll == 17:
            # Cross over image
            draw.line((0, img.size[1] / 2, img.size[0], img.size[1] / 2), fill=(R, G, B), width=5000)
            draw.line((img.size[0] / 2, 0, img.size[0] / 2, img.size[1]), fill=(R, G, B), width=5000)
        if diceroll == 19:
            # Replace with another picture
            img = Image.open("testimage2.jpeg")
            img = img.convert('RGB')
            img.save("testcopy.jpg")
            return
        # if diceroll==20:
        # This one is for fun... just don't click the link.
        # webbroswer.open_new_tab('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        del draw
        i = i + 1
        # save the changes into a new library.
    img.save("testcopy.jpg")
    print("Using Creator...\n")
    return img


# this will be the AI that will be trained to recognize an image is photoshopped or not.
def AI_recognizer(image1, image2):
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
    # Iterate though every pixel
    # If not equal images do not match
    # Else they are equal

def result(state):
    if state == 1:
        print("Image is a poorly made fake!")

    else:
        print("Image is a genuine copy!")

main()

    

