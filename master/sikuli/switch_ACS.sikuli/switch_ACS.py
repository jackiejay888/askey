import os
if exists("Congratulati-2.png"):
    print 'ACS initiate connection Successfully!'
elif exists("SonyACShitia.png"):
    os.system('..\\..\\tools\\WinSCP\winscp.com /command "open scp://root:root@10.1.106.242/" "get /tmp/trace ..\\..\\Result\\femtolog\\" "exit"')
    raise AssertionError, "The ACS initiate connection failed."
else:
    os.system('..\\..\\tools\\WinSCP\winscp.com /command "open scp://root:root@10.1.106.242/" "get /tmp/trace ..\\..\\Result\\femtolog\\" "exit"')
    raise AssertionError, "The ACS initiate connection failed."