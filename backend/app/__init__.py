from flask import Flask
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
"""
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
CORS(app, resources={r'/*': {'origins': '*'}})
"""
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db_metadata = db.metadata
login_manager = LoginManager()
login_manager.init_app(app)



from app.models import *
"""
#db.create_all() #раз у нас есть алембик, то зачем эта штука... Она к тому же мешает, если вы создаете новую таблицу :)

"""
from app.upload import *
from app.generatePerson import generatePersons
upload_vys()
upload_groups()
upload_warcomm()
upload_roles()
# upload_admin()
upload_studying_statuses()
upload_priority_rights()
upload_event_statuses()
"""

