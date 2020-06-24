#sreeram2001
#to find ip address
import socket
hostname = socket.gethostname()
ipadress = socket.gethostbyname(hostname)

#Output side
print("Your System Name is : " + hostname)
print("Your IP Address is :" + ipadress)