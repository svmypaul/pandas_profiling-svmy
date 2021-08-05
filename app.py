from flask import Flask, render_template,request
import pandas as pd
from pandas_profiling import ProfileReport


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data',methods = ['POST'])
def data():
    if request.method == 'POST':
      result = request.files['file']
      filename=result.filename
      if filename =="":
          data1="no file selected"
          return render_template('index.html',df1=data1)

      else:
          data=pd.read_csv(result, error_bad_lines=False)
          profile=ProfileReport(data)
          profile.to_file(output_file="templates/report.html")
          fp=("report_"+filename+"")
          return render_template('index.html',df=data.to_html(),filename=fp)

if __name__ == "__main__":  
    app.run(debug=True)
