from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def success():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<username>')
def username(username):
    return 'Hi ' + username

@app.route('/repeat/<int:num>/<word>')
def repeater(num, word):
    return num * word

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module 
    app.run(debug=True)    # Run the app in debug mode.
