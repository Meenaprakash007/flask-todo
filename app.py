from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Meena! How are you? Are you Done?? or not?'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001',debug=True)
