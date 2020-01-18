# tcp client
import socket as sock
print "creating TCP Client "
tcp_cli = sock.socket(sock.AF_INET,sock.SOCK_STREAM)
ip = sock.gethostname()
port =5005
print "fixing the IP : Port to client :",ip,": ",port
tcp_cli.bind((ip,port))
print "sending the request from client to server"
tcp_cli.connect((ip,5000))
print "waiting for data : ",
data=tcp_cli.recv(1024)
print data," received from ",(ip,5000)

data = input("enter some data for sending : ")
tcp_cli.send(data)
print "closing the client"
tcp_cli.close()
