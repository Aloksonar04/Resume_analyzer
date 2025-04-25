from flask import Flask, request, render_template
import os
from resume_parser import extract_text, extract_skills
from ranker import rank_resumes

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    files = request.files.getlist('resumes')
    target_skills = request.form['skills'].lower().split(',')

    resume_data = []
    for file in files:
        if allowed_file(file.filename):
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            text = extract_text(path)
            skills = extract_skills(text)
            resume_data.append({
                'filename': file.filename,
                'skills': skills
            })

    ranked_resumes = rank_resumes(resume_data, target_skills)
    return render_template('results.html', resumes=ranked_resumes)

if __name__ == '__main__':
    print("App is running at http://127.0.0.1:5000")
    app.run(debug=True)  