'''

Phase three: Templating

Templating allows a program to replace data dynamically in an html file. 

Ex: A blog page, we wouldn't write a whole new html file for every blog page. We want to write
the html part, and styling just once, then just inject the different blog data into that page. 


1) Add the following line to index.html in the body

<h2>###Title###</h2>

2) When a request come in for index (/)
   
   - read the file data for index.html 

   - change the ###Title### string to the string "This is templating"
  
   - return the changed html 

3) Write a function render_template to take an html template, and a hash context

   Ex: render_template("<html>...",{"Title":"This is templating"})

   - Render will the try to replace all the fields in that hash

   Ex: context = {"Title":"This is the title","BlogText":"this is blog data"}

   In the html template replace ###Title### and ###BlogText### with corresponding key values.

   - Test by using this context {"Title":"This is the title","BlogText":"this is blog data"}

4) Add render_template to index_page with the sample context above

'''

import socket
import re

HOST, PORT = '', 8888
VIEWS_DIR = "./views"

context = {"Title":"This is the title","BlogText":"this is blog data"}

urls = {'/':index_page, '/about':about_page}
regex = r'###(\w)###'

def read_data(filename):
	with open(filename, "r") as f:
		return f.read()

def index_page():
	return render_template(read_data("views/index.html"))

def about_page():
	return read_data("views/about.html")

def render_template(template, hash):
	for x in re.findall(regex, template):
		html = template.replace('###'+x+'###',hash[x])
	return html

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

        elif f == '/favicon.ico':
            continue

        firstline = request.split('\r\n')[0]
        f = firstline.split(' ')[1]        

        if f not in urls:
        	print "404 - resource not found!"
        else:
        	html = urls[f]()


        http_response = """\
    HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n %s
    """ % html

        client_connection.sendall(http_response)
        client_connection.close()


run_server()
