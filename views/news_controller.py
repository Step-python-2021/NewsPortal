from flask import render_template, session
from config import app


class NewsController(object):

    @staticmethod
    @app.route('/news/create')
    def create():
        if 'user' in session and session['user'] == 'test3':
            return render_template('news/create.html')
        else:
            return render_template('access/page403.html')

    @staticmethod
    @app.route('/news/delete')
    def delete():
        return render_template('news/delete.html')

    @staticmethod
    @app.route('/news/details')
    def details():
        return render_template('news/details.html')

    @staticmethod
    @app.route('/news/list')
    def list():
        return render_template('news/list.html')

    @staticmethod
    @app.route('/news/update')
    def update():
        return render_template('news/update.html')
