import email
from io import StringIO
import socket
import ssl

class Repeater:

    def __init__(self):
        self.ENDL = '@@ANGIE_ENDLN'
        pass

    def set_endl(self,s):
        self.ENDL = s

    def read_from_file(self,path):
 
        f= open(path,"r")
        st = f.read()
        st = st.rstrip()
        st = st.replace('\n','')
        st = st.replace('\r','')
        st = st.replace(self.ENDL,'\r\n')
        return st

    def send_http(self,http_str,url,p=80):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        addr = (url, p)
        s.connect(addr)
        #ss.send('GET / HTTP/1.0\r\n\r\n'.encode())
        s.send(http_str.encode())
        resp = s.recv(10000)
        #print(resp)
        #print(http_str.encode())
        s.close()
        resp = str(resp)
        resp = resp.replace('\\n','\n')
        resp = resp.replace('\\r','\r')

        return resp


    def send_https(self,http_str,url,p=443):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
        addr = ('www.youtube.com', p)
        ss.connect(addr)
        #ss.send('GET / HTTP/1.0\r\n\r\n'.encode())
        ss.send(http_str.encode())
        resp = ss.recv(10000)
        #print(resp)
        ss.close()

        resp = str(resp)
        resp = resp.replace('\\n','\n')
        resp = resp.replace('\\r','\r')
        return resp

