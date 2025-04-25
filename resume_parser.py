import os
import re
import docx2txt
import textract
import spacy
from PyPDF2 import PdfReader

nlp = spacy.load("en_core_web_sm")


SKILLS_DB = [
   
    'python', 'java', 'c++', 'c#', 'javascript', 'typescript', 'ruby', 'go', 'rust',
    
   
    'html', 'css', 'react', 'angular', 'vue', 'node.js', 'express', 'next.js', 'tailwind css', 'bootstrap',

   
    'django', 'flask', 'spring boot', '.net core', 'laravel', 'ruby on rails',

   
    'sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'sqlite', 'oracle',

    
    'git', 'github', 'docker', 'kubernetes', 'jenkins', 'ci/cd', 'jira', 'slack',

   
    'aws', 'azure', 'google cloud', 'gcp', 'firebase', 'heroku',

   
    'machine learning', 'deep learning', 'data analysis', 'data visualization',
    'pandas', 'numpy', 'matplotlib', 'seaborn', 'scikit-learn', 'tensorflow', 'keras',
    'pytorch', 'nlp', 'computer vision', 'jupyter', 'anaconda',

    # DevOps & Automation
    'ansible', 'terraform', 'shell scripting', 'bash',

    # BI & Analytics
    'power bi', 'tableau', 'excel', 'google sheets',

    # Mobile Development
    'android', 'kotlin', 'swift', 'flutter', 'react native',

    # Soft/General Skills (Optional)
    'agile', 'scrum', 'communication', 'teamwork', 'leadership'
]

def extract_text(file_path):
    text = ""
    if file_path.endswith('.pdf'):
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
    elif file_path.endswith('.docx'):
        text = docx2txt.process(file_path)
    else:
        text = textract.process(file_path).decode('utf-8')
    return text

def extract_skills(text):
    doc = nlp(text.lower())
    extracted_skills = set()
    for token in doc:
        if token.text in SKILLS_DB:
            extracted_skills.add(token.text)
    return list(extracted_skills)
