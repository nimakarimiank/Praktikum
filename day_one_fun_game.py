from microbit import *
import random
import music

# 1. Start the game with a 3-2-1 countdown
for i in range(3, 0, -1):
    display.show(str(i))
    sleep(500)
display.clear()

# 2. Set up the starting variables
score = 0
time_limit = 2000  # Players start with 2000 milliseconds (2 seconds) to react

# 3. The Main Game Loop
while True:
    sleep(500)
    display.scroll("LOS GEHTS", delay=20)
    
    # Pick a random action (0 to 3)
    # 0 = Button A, 1 = Button B, 2 = Logo, 3 = Clap (Loud Noise)
    action = random.randint(0, 3)
    
    # Clear out any old button presses or noises before the round starts
    button_a.was_pressed()
    button_b.was_pressed()
    microphone.was_event(SoundEvent.LOUD)
    
    # Show the symbol for the chosen action
    if action == 0:
        display.show(Image.ARROW_W) # Arrow pointing left to Button A
    elif action == 1:
        display.show(Image.ARROW_E) # Arrow pointing right to Button B
    elif action == 2:
        display.show(Image.TARGET)  # A target to represent the touch logo
    elif action == 3:
        display.show(Image.SQUARE)  # A box to represent making noise
        
    # Record the time the round started
    start_time = running_time()
    success = False
    
    # Keep checking for input as long as the time limit hasn't run out
    while running_time() - start_time < time_limit:
        
        # Check if they did the RIGHT action
        if action == 0 and button_a.was_pressed():
            success = True
            break
        elif action == 1 and button_b.was_pressed():
            success = True
            break
        elif action == 2 and pin_logo.is_touched():
            success = True
            break
        elif action == 3 and microphone.was_event(SoundEvent.LOUD):
            success = True
            break
            
        sleep(10) # A tiny pause keeps the micro:bit running smoothly
        
    # 4. Check the result of the round
    if success:
        # They got it right!
        display.show(Image.YES)
        music.play(["C5:1"]) # Play a short, happy beep
        score += 1
        sleep(400)
        
        # Make the game harder: Every 5 points, subtract 250ms from the time limit
        # (But don't let it drop below 500ms, or it becomes impossible!)
        if score % 5 == 0 and time_limit > 500:
            time_limit -= 250
            
    else:
        # They ran out of time (or did the wrong thing)
        display.show(Image.NO)
        music.play(music.WAWAWAWAA) # Play a sad sound
        sleep(1000)
        
        # Game over - scroll the final score forever
        display.scroll("Score: " + str(score), delay=20)
        