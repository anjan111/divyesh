# udp client
import socket as sock
print "creating UDP Client "
udp_cli = sock.socket(sock.AF_INET,sock.SOCK_DGRAM)
ip = sock.gethostname()
port =5005
print "fixing the IP : Port to client :",ip,": ",port
udp_cli.bind((ip,port))
print "waiting for data : ",
data, addr = udp_cli.recvfrom(1024)
print data," received from ",addr

data = input("enter some data for sending : ")
udp_cli.sendto(data,(ip,5000))
print "closing the client"
udp_cli.close()
