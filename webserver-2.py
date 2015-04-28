'''

Phase two: Routing + Controllers

On Modern web sites we drop the .html for things, and it is more action based.

In your browser a user would request <your site.com> + 

/ 
/about
/blog
/blog/1

1) Add two new functions index_page and about_page

2) Create a hash called urls that maps between a http request like "/" and call index_page(), 
   "/about" calls about_page()

3) Move your file reading code into both of those functions, so index_page reads index.html and
   returns that data, about_page() the same but for about.html


'''
import socket


HOST, PORT = '', 8888
VIEWS_DIR = "./views"


def read_data(filename):
	print filename, type(filename)
	with open(filename, "r") as f:
		return f.read()

def index_page():
	return read_data("views/index.html")

def about_page():
	return read_data("views/about.html")

urls = {'/':index_page, '/about':about_page}

def run_server():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)

 
    print 'Serving HTTP on port %s ...' % PORT
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(4096)

        if not request:
            continue

        firstline = request.split('\r\n')[0]
        verb = firstline.split(' ')[0]
        f = firstline.split(' ')[1]        

        if f not in urls:
        	print "404"
        else:
        	html = urls[f]()


        http_response = """\
    HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n %s
    """ % html

        client_connection.sendall(http_response)
        client_connection.close()


run_server()
