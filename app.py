from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello world</h1>"

@app.route('/hello')
def Hello():
    return "<h2>Hello World</h2>"

@app.route('/student')
def Hello1():
    return "Hello Student"

@app.route('/faculty')
def Hello2():
    return "Hello Faculty"

@app.route('/user/<type>')
def user(type):
    if type == 'student':
        return redirect(url_for('Hello1'))
    if type == 'faculty':
        return redirect(url_for('Hello2'))

USERNAME = 'admin'
PASSWORD = '123'

@app.route('/login2', methods=['POST', 'GET'])  # Form handling in Flask
def formLogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            return f"Welcome {username}"
        else:
            return "Try Again, Error"
    
    return render_template('login.html')  # Render the login form for GET requests


@app.route('/<uname>')
def helloName(uname):
    return render_template('msg.html' , name = uname)

@app.route('/htmltemplate1')    #html templates for flask  and should always in template folder
def htmlTemplate():
    return render_template('index.html')

@app.route('/page')
def page():
    return render_template('page.html')

@app.route('/fetching')
def registration():
    return render_template('formFetch.html')

@app.route('/login5' , methods = ['GET' , 'POST'])
def registration2():
    if request.method == 'POST':
        # Handling POST request - data comes from form body
        result = request.form
    elif request.method == 'GET':
        # Handling GET request - data comes from URL parameters
        result = request.args

    return render_template('result.html', result=result)






if __name__ == '__main__':
    app.run(debug=True)



















# from flask import Flask, redirect, url_for, render_template ,request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "<h1> Hello world  </h1>"

# @app.route('/hello')
# def Hello():
#     return "<h2> Hello World </h2>"


# @app.route('/student')
# def Hello1():
#     return "Hello Student"

# @app.route('/faculty')
# def Hello2():
#     return "Hello Faculty"

# # @app.route('/<name>/')
# # def helloName(name):
# #     return "Hello" + name 

# @app.route('/user/<type>')
# def user(type):
#     if type == 'student':
#         return redirect(url_for('Hello1'))
#     if type == 'faculty':
#         return redirect(url_for('Hello2'))
    

# @app.route('/htmltemplate1')    #html templates for flask  and should always in template folder
# def htmlTemplate():
#     return render_template('index.html')

# USERNAME = 'admin'
# PASSWORD = '123'


# @app.route('/login' ,methods =['POST', 'GET'])   #form handling in flask
# def formLogin():
#     if request.method == 'POST' :

#       username = request.form['username']
#       password = request.form['password']

#       if username == USERNAME and password == PASSWORD:
#         return f"Welcome {username}"
#       else :
#         return "Try Again , Error"
      
#     return render_template('login.html')
      






    

# if __name__ == '__main__':  #ensuring app will run only when executed from here and not imported from somewhere
#     app.run(debug=True)




