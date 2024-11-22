from flask import render_template, request,redirect
import dao
from __init__ import app,login
from flask_login import login_user, logout_user


@app.route("/")
def index():
    cates = dao.load_categories()

    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')

    prodts = dao.load_products(cate_id=cate_id, kw=kw)
    return render_template('index.html', categories=cates, products=prodts)


@app.route('/logout')
def logout_process():
    logout_user()
    return redirect('/login')


@app.route("/login", methods=['get', 'post'])
def login_process():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password= request.form.get('password')

        u = dao.auth_user(username=username, password=password)
        if u:
            login_user(u)
            return redirect('/')

    return render_template('login.html')


@login.user_loader
def get_user_by_id(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)
