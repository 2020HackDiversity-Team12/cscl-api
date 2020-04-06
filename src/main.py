import database
from flask import Flask

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'localhost',
    'port': 27017
}


database.init(app)

# ROUTES
@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000", debug=True)
