import os 

ip = input("[$] Please Enter your IP Address : ")
process = os.popen("node detect-tor.js %s " % ip)
kos = process.read()
print (kos)
if "false" in kos:
    print ("The IP is not using tor proxy !")
elif "true" in kos:
    print ("The IP is using tor proxy !")
else:
    print ("Wrong Maybe !")
    