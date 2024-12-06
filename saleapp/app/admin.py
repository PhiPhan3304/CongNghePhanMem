from models import  Category,Products,User
from __init__ import  app,db
from flask_admin import Admin
from flask_admin.contrib.sqla import  ModelView


admin= Admin(app, name='eCommerce Admin', template_mode='bootstrap4')
admin.add_view(ModelView(Category,db.session))
admin.add_view(ModelView(Products,db.session))
admin.add_view(ModelView(User,db.session))

