from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')


# List to store registered users
registered_users = []

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        Password = request.form['Password']
        registered_users.append({"username": username, "email": email, 'Password':Password})
        return redirect(url_for('registered_list'))
    return render_template('register.html')

@app.route('/registered_list')
def registered_list():
    return render_template('registered_users.html', users=registered_users)


    

if __name__ == '__main__':
   app.run(debug=True)