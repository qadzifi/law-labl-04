import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join('.', 'filelocation')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'md'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'tugas key'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/download', methods=['GET', 'POST'], defaults={'filepath': ''})
@app.route('/download/<path:filepath>', methods=['GET', 'POST'])
def download_file(filepath):
    if filepath:
        if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filepath)):
            return send_from_directory(app.config['UPLOAD_FOLDER'], filepath, as_attachment=True)
    file_list = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('downloads.html', file_list=file_list,
        folder_path=app.config['UPLOAD_FOLDER'])

@app.route('/')
def hello_world():
    return 'Hello, World download!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8002)
