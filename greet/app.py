import flask as fl

app = fl.Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/home')
def welcomeHome():
    return 'welcome home'

@app.route('/welcome/back')
def welcomeBack():
    return 'welcome back'