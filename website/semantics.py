from flask import Flask
app = Flask(__name__)
UPLOAD_FOLDER = '/home/aowsenek/semantics/upload'
ALLOWED_EXTENSIONS = set(['txt','doc','docx','dat'])



app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/', methods=['GET','POST'])
def index():
   if request.method == 'POST':
      file=request.files['file']
      if file and allowed_file(file.filename):
          filename = secure_filename(file.filename)
          file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))        
          return render_template("download.html")
   return render_template("index.html")

if __name__=='__main__':
   app.run(port=5010)

