from flask import Blueprint ,render_template #blueprint separates and can have multiple files

views = Blueprint('views',__name__)


@views.route('/')
def home():
    return render_template("home.html")
