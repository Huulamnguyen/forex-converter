### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

    While JavaScript is a scripting language, Python is an object-oriented programming language—a type of coding language that lets developers build sites and apps with virtual building blocks

    Scripting Languages (like JavaScript) tell websites and web applications to “do something?” You can visualize this as the scripting language handing a script to the computer program it’s attached to, which the program then reads and acts on.

    Object oriented languages (like Python) take a different approach—these languages allow programmers to create virtual objects in their code and give each of these objects unique attributes and abilities. All of the objects a developer creates are then able to interact with each other or perform actions on their own.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  Using get() Method to handle KeyError
    D = {"a": 1, "b": 2}
    D.get("c", 3)
  Using setdefault() Method to handle KeyError
    D.setdefault("c", 3)
    
- What is a unit test?
  Test one “unit” of functionality: Typically, one function or method
  Don’t test integration of components: Don’t test framework itself (eg, Flask)
  Promote modular code: Write code with testing in mind

- What is an integration test?
  Test that components work together
  The kinds of thing to test:
    Does this URL path map to a route function?
    Does this route return the right HTML?
    Does this route return the correct status code?
    After a POST to this route, are we redirected?
    After this route, does the session contain expected info?

- What is the role of web application framework, like Flask?
  A framework (like Flask) is a code library that makes a developer's life easier when building reliable, scalable, and maintainable web applications" by providing reusable code or extensions for common operations.


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  Answer: I might choose query parameter. It feels like more extra info about page. Cause request eventually comes from form where query parameter is often used. 

- How do you collect data from a URL placeholder parameter using Flask?

  from flask import request
  @app.route(...)
  def login():
    username = request.form.get('username')
    password = request.form.get('password')

- How do you collect data from the query string using Flask?

from flask import request
@app.route('/data')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')


- How do you collect data from the body of the request using Flask?
  request.file

- What is a cookie and what kinds of things are they commonly used for?
  Cookies are name/string-value pair stored by the client (browser).
  The server tells client to store these.
  The client sends cookies to the server with each request.

- What is the session object in Flask?
  Session is yet another way to store user-specific data between requests. 
  It works similar to cookies. To use session you must set the secret key first. 
  The session object of the flask package is used to set and get session data. 
  The session object works like a dictionary but it can also keep track modifications.

- What does Flask's `jsonify()` do?
  jsonify is a function in Flask's flask.json module. jsonify serializes data to JavaScript Object Notation (JSON) format, wraps it in a Response object with the application/json mimetype.

  Note that jsonify is sometimes imported directly from the flask module instead of from flask.json. It is the same function that is imported, but there are less characters to type when you leave off the .json part.