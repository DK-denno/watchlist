from . import forms
from flask import Blueprint
auth = Blueprint('auth', __name__)
from . import views
from .. import db
from flask import render_template, redirect, url_for
from ..models import User
from .forms import RegistrationForm


@auth.route('/register', methods=(['GET', 'POST']))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data
                    )
        db.session.add(user)
        db.session.commit()
        return redirect( url_for('auth.login'))
        
    return render_template('auth/register.html',reg_form=form)

