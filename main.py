from flask import Flask
from flask_restful import Api

from JSON import Languages, Files

app = Flask(__name__)
api = Api(app)

api.add_resource(Languages, '/json-languages')
api.add_resource(Files, '/json-files')

if __name__ == '__main__':
    app.run()  # run our Flask app
