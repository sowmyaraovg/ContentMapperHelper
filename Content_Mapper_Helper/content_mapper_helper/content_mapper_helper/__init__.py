from flask import Flask

from .models import db
from .views import Contentmapperhelper

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

app.register_blueprint(Contentmapperhelper)
