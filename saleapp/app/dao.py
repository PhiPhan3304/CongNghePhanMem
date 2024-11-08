from app.models import Category, Products


def load_categories():
    return Category.query.order_by('id').all()


def load_products(cate_id=None, kw=None):
    query = Products.query
    if kw:
        query = query.filter(Products.name.contains(kw))
    if cate_id:
        query = query.filter(Products.category_id == cate_id)
    return query.all()
