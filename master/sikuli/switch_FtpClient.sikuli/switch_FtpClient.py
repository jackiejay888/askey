if exists(Pattern("Stop.png").similar(0.90)):
    click("Stop.png")

if exists("Start.png"):
 #   click("Start.png")
    if exists("Setting.png"):
        click("Setting.png")    
        if exists("Choose.png"):
            click("Choose.png")
            sleep(1)    
            type("Z:\\automation\\apk\\FtpClient.apk")
            type("o",KEY_ALT)          
            click("Start.png")
            sleep(2)     

else:
    raise AssertionError,"switch android FtpClient app error" 