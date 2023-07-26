from flask import Flask
from database import db
from users import users_bp


app = Flask(__name__)
app.register_blueprint(users_bp)

@app.route('/', methods=['GET'])
def hello():
    return 'Initial page'

# Run the Flask application
if __name__ == '__main__':
    with db:
        app.run()


