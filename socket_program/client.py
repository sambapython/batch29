import socket
#host="www.google.com"
host="tcloudost-VirtualBox"
port= 8889 #443 #80
try:
	s=socket.socket()
	s.connect((host,port))
	ack=s.recv(1024)
	print "ack from service:",ack
	s.send("12")
	res = s.recv(1024)
	print "result : ",res
except Exception as err:
	print err
finally:
	s.close()
