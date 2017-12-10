from flask import Flask
from flask_ask import Ask, statement, question, session
from stat_tracker import updateStats

app = Flask(__name__)
ask = Ask(app, "/ham")

app.route('/')
def homepage():
    return 'Hiya'

@ask.launch
def start_skill():
    greeting = 'Ready'
    return question(greeting)

@ask.intent('HamTvOnIntent')
def tvOn_intent():

    # add tv on function here
    return statement('TV initiating')

@ask.intent('HamTvOffIntent')
def tvOff_intent():

    # add tv off function here
    return statement('TV going to standby mode.')

if __name__=='__main__':
    app.run(debug=True)