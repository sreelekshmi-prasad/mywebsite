from flask import Blueprint ,render_template #blueprint separates and can have multiple files
from flask_login import login_required,current_user

views = Blueprint('views',__name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html")
