from serial_communication import Arduino

bot=Arduino()

def navigate(x,width=640):
    center=width//2

    if x<center-50:
        bot.left()
        print("Moving Left")

    elif x>center+50:
        bot.right()
        print("Moving Right")

    else:
        bot.forward()
        print("Moving Forward")

def stop():
    bot.stop()

def pollinate():
    bot.stop()
    bot.pollinate()
    print("Pollinating")
