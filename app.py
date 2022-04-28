from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'I have made nothing so far D:'

if __name__ == '__main__':
    app.run(debug=True)