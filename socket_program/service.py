import socket
host = "tcloudost-VirtualBox"
port = 8889
try:
    s=socket.socket()
    s.bind((host,port))
    s.listen(6)
    print "waiting for the client request"
    #print s.accept()
    cob,ci=s.accept()
    cob.send("connected successfully.")
    data = cob.recv(1024)
    data=int(data)
    resp = "EVEN" if data%2==0 else "ODD"
    cob.send(resp)
except Exception as err:
    print err
finally:
    s.close()