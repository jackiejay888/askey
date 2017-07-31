if exists("Congratulati.png"):
    click("Congratulati.png")
    pass
if exists("SorryACSinit.png"):
    raise AssertionError, "The ACS initiate connection failed."
else:
    print 'pass'
    pass
