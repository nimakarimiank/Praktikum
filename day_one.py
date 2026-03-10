from microbit import *
image_number = 0

image_list = [Image.HEART, Image.HAPPY, Image.SMILE, Image.SAD,
              Image.CONFUSED, Image.ANGRY, Image.ASLEEP, Image.SURPRISED,
              Image.FABULOUS, Image.SILLY, Image.YES, Image.NO, Image.MEH,
             Image.DUCK, Image.GIRAFFE, Image.SKULL, Image.GHOST, Image.PACMAN]
while True:
    if button_a.was_pressed():
        if image_number + 1 == len(image_list):
            image_number = 0
        else:
            image_number = image_number +1 
        # take a light measurement and store it
        #reading = display.read_light_level()
        display.show(image_list[image_number])
        #display.show(Image.DIAMOND_SMALL)
        sleep(400)

        #display.show(Image.DIAMOND)
        #sleep(400+500)
        #display.show('M')
        

    elif button_b.was_pressed():
        if image_number == 0:
            image_number = len(image_list) - 1
        else: 
            image_number = image_number -1
        # display the stored light measurement
        display.clear()
        display.show(image_list[image_number])
        sleep(500)
        #display.show('M')

        

