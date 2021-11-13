import os
os.system("tput setaf 2")
print("\t\t\tWelcome to My Menu")
os.system("tput setaf 7")
print("\t\t\t------------------"	)
print()
#voice 
os.system("espeak-ng -s 130 -v en-us 'where do you want to run '")
print("where u want to run ur program  (local/remote): " , end='')
myhost = input()
print(myhost)
if myhost == "remote":
	remote_ip = input("Enter ur remote host ip : ")
print()
while True:
	print("""
	Press 1 : to date
	Press 2 : to cal
	Press 3 : to ls
	Press 4 : to mkdir
	Press 5 : to ping
	Press 6 : to exit
	""")
	if myhost == "remote":
		print("enter ur choice : ", end='')
		ch = input()
		print(ch)
		if int(ch) == 1:
			os.system( "ssh {} date".format(remote_ip) )
		elif int(ch) == 2:
			os.system("ssh {} cal".format(remote_ip) )
		elif int(ch) == 3:
			print("ls")
		elif int(ch) == 4:
			print("mkdir")
		elif int(ch) == 5:
			os.system("ping google.com")
		elif int(ch) == 6:
			exit()
		else:
			print("not supported")
	else:
		print("")
	#the voice menu demo below 
	if myhost == "local":
		os.system("espeak-ng -s 130 -v en-us 'Please Enter your choice '")
		print("enter ur choice : ", end='')
		ch = input()
		if int(ch) == 1:
			os.system("espeak-ng -s 130 -v en-us 'Printing date'")
			os.system("date")
		elif int(ch) == 5:
			os.system("espeak-ng -s 130 -v en-us 'Bye'")
	os.system("espeak-ng -s 130 -v en-us 'Press Enter to continue'")
	input("Press enter to cont .....")
	os.system("clear")
