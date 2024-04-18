from flask import Flask 
app = Flask(__name__)

@app.route('/') #this is the default url 
def home():
    return '<h1>welcome to the flask in the eee  datapoint'


@app.route('/dani')
def dani():
    return '<h1>datapoint in the good company</h1>'
if __name__ == '__main__':
    app.run(debug=True) #in this debug=True is automatic run the server in development only not in production
    