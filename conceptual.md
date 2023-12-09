### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
there are many syntax differenced between python and javascript. Python is a versatile language with a focus on readability, often used in data science, AI, and server-side applications. JavaScript is the primary language for web development, enabling interactive and dynamic content in web browsers. While Python is known for its simplicity and wide range of applications, JavaScript is essential for creating engaging web experiences.



- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
you can use a GET method or 'try except blocl

get method allows you to acces key values but if the key is not found it returns none

try-except block while accessing the key normally if an Keyerror is raised the excerpt will prevent the program from crashing
- What is a unit test?
a unit test is a method of testing python code if your code base is a washing machine this would be like testin gif the basket was spinning properly. this is testing a specific part of your code individually
- What is an integration test?
testing multiple concepts and seeing if they work together

- What is the role of web application framework, like Flask?
simplifies web development by providing tools and frameworks to build and deploy web applications efficiently. testing web routes and requests, handling data exchange between client and server

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  the initial entry would be if the parameter is only talking about pretzels. if the type=pretzel it means that someone dynamically entered in pretzels into the searchfield 

- How do you collect data from a URL placeholder parameter using Flask?
 to get the query parameters in the URL in Flask, use request. args. In order to access and control the query parameters, we can use methods like get
- How do you collect data from the query string using Flask?
request.args.get('file-name')

- How do you collect data from the body of the request using Flask?
form_data = request.form['key]


- What is a cookie and what kinds of things are they commonly used for?
 a small piece of data sent from a website and stored on the user's computer by the user's web browser while the user is browsing. 

 Websites use cookies to personalize user experience by remembering preferences, settings, and login information. 

Cookies can help in ensuring the security of online transactions and in preventing fraud.

- What is the session object in Flask?
a way to store information specific to a user from one request to the next. It is similar to cookies, except that session data is stored on the server. Here are key aspects of the session object in Flask:

- What does Flask's `jsonify()` do?
Flask's jsonify() function converts Python data structures into JSON format and wraps the resulting JSON in a Response