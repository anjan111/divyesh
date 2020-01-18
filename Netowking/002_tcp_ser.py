# tcp server
import socket as sock
print "creating TCP server "
tcp_ser = sock.socket(sock.AF_INET,sock.SOCK_STREAM)
ip = sock.gethostname()
port =5000
print "fixing the IP : Port to server :",ip,": ",port
tcp_ser.bind((ip,port))
print "fixing the no of connection "
tcp_ser.listen(1)
print " waiting for connection"
conn , addr_c = tcp_ser.accept()
print "i got connection from : ",addr_c

data = input("enter some data for sending : ")
conn.send(data)
print "waiting for data : ",
data= conn.recv(1024)
print data," received from ",addr_c
print "closing the server"
tcp_ser.close()

