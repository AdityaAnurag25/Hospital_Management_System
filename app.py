from flask import Flask, render_template
from config import configure_app

app = Flask(__name__)
configure_app(app)
import routes
import models

if __name__ == '__main__':
    app.run(debug=True)
