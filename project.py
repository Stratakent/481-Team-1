import subprocess
from random import randint
import image
import webbrowser
from PIL import Image, ImageDraw

#for the purpose of this project, via the Pillow module, 
#we referenced most of our code from this link: https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html

def main():
    img1 = Image.open("testimage.jpg")
    AI_creator(img1)
    RNG = randint(1,5)

    if RNG==1:
        img2 = Image.open("testcopy.jpg")
    if RNG==2:
        img2 = Image.open("testimage2.jpg")
    if RNG==3:
        img2 = Image.open("testimage3.jpg")
    if RNG==4:
        img2 = Image.open("testcopy.jpg")
    if RNG==5:
        img2 = Image.open("testcopy.jpg")

    AI_recognizer(img1, img2)


def AI_creator(img):
    # might require the PILLOW extension for image drawing.
    # get the photo from a selected library
    # open via PILLOW module
    # get photoshop or paint to add in a smudge onto the photo... randomly, flip a coin or something i dunno.
    i = 0
    j = randint(0,5)
    while i < 5:
        # img.size as referenced multiple times in the code below gets the image sizes of the x and y coordinates.
        R=randint(0,255)
        G=randint(0,255)
        B=randint(0,255)
        diceroll = (randint(1,25))  # Might want to introduce more randomness so that the AI does more interesting things
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
        i += 1
        # save the changes into a new library.
    img.save("testcopy.jpg")
    print("Using Creator...\n")
    return img


# this will be the AI that will be trained to recognize an image is photoshopped or not.
def AI_recognizer(image1, image2):
    state = 0
    size = 0
    image1.show()
    image2.show()
    if image1.size[0]!=image2.size[0]:
        state=1
        size=1
    if image1.size[1] != image2.size[1]:
        state=1
        size=1

    i=0
    while i<image1.size[0] and state==0:
       j = 0
       while j<image1.size[1]:
           if image1.getpixel((i,j))!= image2.getpixel((i,j)):
               state = 1
               print("Pixels don't match.")
           j+=1
       i += 1
    result(state,size)
    # Iterate though every pixel
    # If not equal images do not match
    # Else they are equal

def result(state,size):
    RNG=randint(0,9)
    if RNG <7:#it's correct
        if state == 1:
            print("AI: Image is a poorly made fake!")
            if size == 1:
                print("AI: At least get the right size...")
        else:
            print("AI: Image is a genuine copy!")
    elif RNG > 6:#it's wrong
        if state == 1:
            print("AI: Image is a genuine copy!")
        else:
            print("AI: Image is a poorly made fake!")

    if state == 1:
        print("The image is actually a fake.")
    else:
        print("The image is actually the  real deal.")

    if RNG < 7:
        print("It got it right.")
    else:
        print("It got it wrong.")

main()


