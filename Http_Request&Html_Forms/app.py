from flask import Flask,redirect,url_for,render_template ,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        use = request.form['usr_name']
        
        return redirect(url_for('user',usr=use))
    return render_template('login.html')
@app.route('/<usr>')
def user(usr):
    return f'hello {usr}!'

if __name__ == '__main__':
    app.run(debug=True)