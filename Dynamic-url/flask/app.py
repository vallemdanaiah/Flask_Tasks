from flask import Flask 
app = Flask(__name__)

@app.route('/') #this is the default url 
def home():
    return '<h1>welcome to the flask in the eee  datapoint'


@app.route('/dani')
def dani():
    return '<h1>datapoint in the good company</h1>' 

    """above to funcations  are static funcations
    """
    
#this is the dynamaic url

@app.route('/<name>')
def name(name):
    return f"Hello {name}!"

#redirect the funcation first method
from flask import Flask ,redirect, url_for
@app.route('/admin')
def admin():
    return redirect('/')
# #redirect the funcation second method
# @app.route('/ad')
# def ad():
#     return redirect(url_for('dani'))



if __name__ == '__main__':
    app.run(debug=True) #in this debug=True is automatic run the server in development only not in production
    