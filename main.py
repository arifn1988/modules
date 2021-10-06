import this
import time
import math
import datetime
import sys
import greet

# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

def wait(seconds):
	time.sleep(seconds)

def my_sin(radian):
	return math.sin(radian)

def iso_now():
	return datetime.datetime.now().replace(microsecond=0).isoformat()

def platform():
	return sys.platform

def supergreeting_wrapper(name):
	return greet.supergreeting(name)

#wait(5)
#print(iso_now())
#print(my_sin(1.57))
#print(platform())
print(supergreeting_wrapper('Arif'))