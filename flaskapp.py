import os
import base64
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from forms import Base64InputForm

UPLOAD_FOLDER = '.\\filelocation'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'md'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'tugas key'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def base64_decode(string):
    try:
        string = str.encode(string)
    except:
        pass
    return bytes.decode(base64.decodestring(string))

def base64_encode(string):
    try:
        string = str.encode(string)
    except:
        pass
    return bytes.decode(base64.encodestring(string))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('uploads.html')

@app.route('/base64', methods=['GET', 'POST'])
def base64_operation():
    if request.method == 'GET':
        form = Base64InputForm()
        return render_template('base64.html', input_form=form)
    result = 'Non working operation'
    operation = request.form['operation']
    if operation:
        string = request.form['text']
        if string:
            if operation == 'encode':
                result = base64_encode(string)
            if operation == 'decode':
                result = base64_decode(string)
    return result

@app.route('/')
def hello_world():
    return 'Hello, World!'
