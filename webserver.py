Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import socket
>>> 
>>> HOST, PORT ='', 8888
>>> 
>>> listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
>>> listen_socket.bind((HOST, PORT))
>>> listen_socket.listen(1)
>>> print('Serving HTTP on port %s ...' % PORT)
Serving HTTP on port 8888 ...
>>> while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.rec(1024)
	print(request.decode('utf-8'))

	
http_response = """\
HTTP/1.1 200 OK

Diana Sedlak says "Hello, World!"
"""
client_connection.sendall(bytes(http_response, 'utf-8'))
client_connection.close()
