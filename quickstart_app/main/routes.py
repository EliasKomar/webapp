from flask_login import current_user, login_required
from flask import render_template, redirect, url_for, request, Blueprint, abort
from quickstart_app.models import User, Task, Subject
from quickstart_app import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/config', methods=['GET', 'POST'])
@login_required
def config():
    user = User.query.get_or_404(current_user.id)
    if user.status == 'user':
        abort(403)

    editors = User.query.filter_by(status='editor').all()
    god_mode = User.query.filter_by(status='god_mode').all()
    return render_template('config.html', title='Config', editors=editors+god_mode)

@main.route('/subject', methods=['GET', 'POST'])
@login_required
def add_subject():
    subjects = Subject.query.all()
    if request.method == 'POST':
        db.session.add(Subject(name=request.form['name']))
        db.session.commit()
        return redirect(url_for('main.add_subject'))
    return render_template('add_subject.html', title='Subject', subjects=subjects)

@main.route('/makeditor/<string:username>')
@login_required
def make_editor(username):
    if current_user.status != 'god_mode':
        abort(403)
    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404)
    user.status = 'editor'
    db.session.commit()
    return redirect(url_for('users.profile', username=user.username))
