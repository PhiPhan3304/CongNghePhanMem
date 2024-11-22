from models import Category, Products, User
import hashlib


def load_categories():
    return Category.query.order_by('id').all()


def load_products(cate_id=None, kw=None):
    query = Products.query
    if kw:
        query = query.filter(Products.name.contains(kw))
    if cate_id:
        query = query.filter(Products.category_id == cate_id)

    page_size = 8
    # start = (page -1) * page_size
    # query = query.slice(start )

    return query.all()


def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username), User.password.__eq__(password)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)
