import os
import ConfigParser
 
config = ConfigParser.SafeConfigParser()
config.read('..\ini\power.conf')
max_power = config.get('TX_Max_Power','Max_Power')
femto_ip = config.get('TX_Max_Power','femto_ip')

if exists(Pattern("Start.png").similar(0.90)):
	doubleClick(Pattern("Start.png").similar(0.90))
	click("ePerView.png")
	sleep(7)  
    
if exists(Pattern("Stop.png").similar(0.90),10):
	click(Pattern("Stop.png").similar(0.90))
#	click(Pattern("Stop.png").similar(0.90))    
	click(Pattern("clear_field.png").targetOffset(0,-10),5)
	type("a",KEY_CTRL) 
	type(Key.DELETE)
	type(femto_ip)
	type(Key.TAB)
	type("a",KEY_CTRL) 
	type(Key.DELETE)
	type("7777")
	click(Pattern("CancelOKAuto.png").targetOffset(-20,0))#OK
	sleep(5)
	click("Clear.png")
	sleep(1)	
	click("command_field.png")


#    for i in range(0,40):
#        max_power = int(max_power) + int(i)
#        type("shell('set_tx_max_power "+ str(max_power)+"')")
#        type(Key.ENTER)
#        sleep(15)
	
#	type("shell('set_tx_max_power "+ max_power+"')")
#	type(Key.ENTER)

   
else:
    raise AssertionError,"switch android FtpClient app error"     






# Pattern("CancelOKAuto.png").targetOffset(-90,0)#Cancel
# Pattern("CancelOKAuto.png").targetOffset(80,0)#auto reconnect
