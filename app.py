from flask import Flask, render_template
import os

app = Flask(__name__)
PDF_FOLDER = os.path.join('static', 'pdfs')

@app.route('/')
def index():
    files = os.listdir(PDF_FOLDER)
    pdfs = [f for f in files if f.lower().endswith('.pdf')]

    teacher_pdfs = ['TeacherMilliySertifikat.pdf', 'TeacherSAT.pdf']
    teachers = [f for f in pdfs if f in teacher_pdfs]
    students = [f for f in pdfs if f not in teacher_pdfs]
    students.sort(key=lambda f: f.lower() != 'ulug.pdf')

    return render_template('index.html', teachers=teachers, students=students)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
