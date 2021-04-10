#!/bin/python3

import getpass
import telnetlib

#OSPF
def eigrp(HOST,user,password,ensec):
	nw = input("In which network do you want to run EIGRP? >> ")
	wildmask = input("Enter Wildcard mask: >> ")
	asn = input("ASN? >> ")
	tn = telnetlib.Telnet(HOST)

	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\n")
	if password:
	    tn.read_until(b"Password: ")
	    tn.write(password.encode('ascii') + b"\n")

	tn.write(b"en\n")
	tn.write(ensec.encode('ascii') + b"\n")
	tn.write(b"conf t\n")
	tn.write(b"router eigrp " + asn.encode('ascii') + b"\n")
	tn.write(b"network " + nw.encode('ascii') + b" " + wildmask.encode('ascii') + b"\n")
	tn.write(b"end\n")
	tn.write(b"exit\n")

	print(tn.read_all().decode('ascii'))
	
	
#START
print("what do you want to Configure?")
list1 = ["OSPF","Vlan","Trunk","STP","EIGRP"]
list2 = []
n = 1
for i in list1 :
	list2.append(n)
	print(n,":",i)
	n = n + 1

while True:
	select = int(input("choose a number: "))
	if select in list2:
		HOST = input("Enter your Device IP Addrees >> ")
		user = input("Enter your remote account: >> ")
		password = getpass.getpass()
		ensec = input("Enter your password/secret: (leave empty if not defined) >> ")
		print("OK, Lets Configure...")

		if select == 1:
			eigrp(HOST,user,password,ensec)
		elif select == 2:
			Vlan()
		elif select == 3:
			Trunk()
		elif select == 4:
			STP()
		exit(0)
	else:
		print("Please Enter the Operation Number of the list")
		

