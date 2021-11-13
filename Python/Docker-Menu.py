import os
os.system("tput setaf 2")
print("\t\t\Play with Docker")
os.system("tput setaf 7")
print("\t\t\t------------------"	)
print()
while True:
	print("""
	----------------------------------------------
	To Pull the Image             : Press 1
	To List the Images            : Press 2
	To Run the Image              : Press 3
	To List the Docker Process    : Press 4
	To Get the shell of container : Press 5
	To Remove specific container  : Press 6
	To Remove Image               : Press 7
	To Stop the container         : Press 8
	To Restart the container      : Press 9
	To Cleanig container Junk     : Press 10
	
	To Stop the Docker Service    : Press 98
	----------------------------------------------
	To Exit                       : Press 99	
	----------------------------------------------
	""")
	print("Please Enter your choice : ", end='')
	ch = input()
	print(ch)
	if int(ch) == 1:
		#Pull image
        impImage = input("Please Enter the image name", end='')
        os.system("sudo docker pull {}".format(impImage))    
	elif int(ch) == 2:
		#List the image
		os.system("sudo docker images")
	elif int(ch) == 3:
		#Run the image
		chImage = input("Please enter image name", end='')
		chCUSImage = input("Please Custome name to image", end='')
		chYN = input("After stoping the container do you want to remove container Y/N",end='')
		if chYN == y or Y:
			os.system("sudo docker run -it -d --name={} {} ".format(chCUSImage,chImage))
		else:
			os.system("sudo docker run -it -d --rm --name={} {} ".format(chCUSImage,chImage))
	elif int(ch) == 4:
		#List the images
		chYN = input("Do you want to list all? Y/N")
		if chYN == y or Y:
			os.system("sudo docker ps -a")
		else:
			os.system("sudo docker ps -a")	
	elif int(ch) == 5:
		#Getting shell
		chCon = input("Please enter container ID or Image Name", end='')
		os.system("sudo docker exec -it {} /bin/bash".format(chCon))
	elif int(ch) == 6:
		#RemoveContainer
		os.system("sudo docker ps -a")
		chRem = input("Please enter which container want to remove? \n Note: These command not remove the active container \n\n Must Select Container ID",end='')
		os.system("sudo docker rm {}".format(chCon))
	elif int(ch) == 7:
		#Remove Image
		os.system("sudo docker images")
		chImage = ("Please select image name, That image will be remove")
		os.system("sudo docker rmi {} ".format(chImage))
	elif int(ch) == 8:
		#Stoping Container
		chCon = input("Please enter container ID or Image Name", end='')
		os.system("sudo docker stop {} ".format(chCon))
	elif int(ch) == 9:
		#Restart Container
		chCon = input("Please enter container ID or Image Name", end='')
		os.system("sudo docker restart {} ".format(chCon))
	elif int(ch) == 10:
		#Cleaning up
		os.system("sudo docker rm $(docker ps -a -q)")
	elif int(ch) == 98:
		#Stoping Docker
		os.system("sudo systemctl stop docker.service docker.socket ")
	elif int(ch) == 99:
		#Exiting from loop
		exit()
	else:
		print("Oops Something Wrong.!")


