from flask import Blueprint ,render_template,flash,request #blueprint separates and can have multiple files
from flask_login import login_required,current_user
from .models import Note
from . import db

views = Blueprint('views',__name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if not note or len(note.strip()) < 1:
            flash('Note is too short!', category='error')
        else:
            try:
                new_note = Note(data=note, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note Added!', category='success')
            except Exception as e:
                db.session.rollback()
                flash(f"An error occurred while adding the note: {str(e)}", category='error')
    return render_template("home.html", user=current_user)
