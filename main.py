from flask import Flask
from flask_restful import Api

from JSON import Languages

app = Flask(__name__)
api = Api(app)

api.add_resource(Languages, '/json-languages')

if __name__ == '__main__':
    app.run()  # run our Flask app
