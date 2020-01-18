# udp server
import socket as sock
print "creating UDP server "
udp_ser = sock.socket(sock.AF_INET,sock.SOCK_DGRAM)
ip = sock.gethostname()
port =5000
print "fixing the IP : Port to server :",ip,": ",port
udp_ser.bind((ip,port))
data = input("enter some data for sending : ")
udp_ser.sendto(data,(ip,5005))
print "waiting for data : ",
data, addr = udp_ser.recvfrom(1024)
print data," received from ",addr
print "closing the server"
udp_ser.close()

