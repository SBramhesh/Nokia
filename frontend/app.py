from flask import url_for
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import os
from flask import Flask, flash, request, jsonify, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = b'_conj#y2L"F890z\n\cloj]/'
cwd = os.getcwd()
app.config['UPLOAD_FOLDER'] = cwd + '\\uploads'
# app.config['UPLOAD_FOLDER'] = 'C:\\Users\\bramh\\python\\environments\\streamlit\\nokia\\frontend\\uploads'


@app.route('/')
def index():
    resp = make_response(render_template('nokia.html'))
    resp.set_cookie('username', 'the username')
    return resp


@app.route("/me")
def me_api():
    # user = get_current_user()
    return {
        "username": "Hick",
        "theme": "dark",
        "image": "RRR",
    }


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


# @app.route('/')
# def index():
#     return 'index'


# @app.route('/login')
# def login():
#     return 'login'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('nokia.html', name=name)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_files = flask.request.files.getlist("file[]")
        print(uploaded_files)
        return ""


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route("/download/")
# def download_file(name=None):
#     path = os.path.join(app.config['UPLOAD_FOLDER'],
#                         'PH20115B_NR_CIQ_EXPORT.xlsx')
#     try:
#         return send_file(path)
#     except Exception as e:
#         print(e)
@app.route("/downloads/<path:name>")
def download_file(name):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], name, as_attachment=True
    )


@app.route('/file', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        flash('method is POST')
        # check if the post request has the file part
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return 'No file part'
        try:
            file = request.files['file']
            # uploaded_files = request.files.getlist("file[]")
            # print(uploaded_files)
            return str(file.filename)
        except Exception:
            return str(Exception)

        else:
            pass  # execute if no exception

        finally:
            file_list = []
            # for file in request.files:
            # file_list.append(file.filename)
            # print(dict(request.files).keys)
            file_list = request.files
            file = request.files['nrciq']
            file2 = request.files['lteciq']
            # return dict(file_list)
            # return dict(zip(file_list, iter(file_list).next().filename))
            if file:
                filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
            return str(file2.filename + ' and ' + file.filename)
            # Some code .....(always executed)
            # If the user does not select a file, the browser submits an
            # empty file without a filename.

            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('download_file', name=filename))
    else:
        flash('method is not POST')

    return render_template('nokia.html')
