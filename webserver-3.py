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


