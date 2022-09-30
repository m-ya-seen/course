from operator import contains
from xmlrpc.client import boolean

content=str(input("enter text"))
if ("subscribe"   in content):
    print("spam detected")
else:
    print("no spam detected")    
