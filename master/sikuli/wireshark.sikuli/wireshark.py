if exists("Win.png"):
	click("Win.png")
	type("cmd")
	type(Key.ENTER)
	sleep (2)
	type("cd c:\\remote")
	type(Key.ENTER)
	type("plink.exe -ssh -pw "+'""'+" root@10.102.81.77"+' "/usr/sbin/tcpdump -s 0 -U -n -w - -i eth0 not port 22 "'+ " | " +'"C:\Program Files\Wireshark\Wireshark.exe"'+" -k -i  -")
	type(Key.ENTER)
else:    
    raise AssertionError,"Cann't capture packet from femtocell"


type("capture_filter.png", "s1ap")
click("Apply.png")
if exists("packet.png",300):
    click("Stop_capture.png")
else:
    raise AssertionError, "Cann't stop capture packet"
    # print "Cann't stop capture packet"

click("File.png")
click("Save.png")
sleep (3)
type("result")
sleep (1)
type("s",KEY_ALT)

if exists("Save_as.png"):
    click("Yes.png")
else:    
    raise "Cann't save capture packet"

click("File.png")
click("export_text.png")
click("As_plain_text.png")
type("result.txt")
type("s",KEY_ALT)
if exists("Save_as.png"):
    type("y",KEY_ALT)
else:    
    raise AssertionError, "Cann't saveexport capture packet"
    # print "Cann't saveexport capture packet"
type("q",KEY_CTRL)

            
