from flask import Flask,render_template

site_name='PASSVAP'

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title=site_name)




if __name__=="__main__":
    app.run(debug=True)




