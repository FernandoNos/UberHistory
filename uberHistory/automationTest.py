from uiautomator import device as d
print 'OI'
print d.info
d.screen.on()
print "click on uber"
d(text="Uber").click()