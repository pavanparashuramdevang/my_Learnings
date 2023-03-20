from flask import Flask,render_template
from forms import RegistrationForm,LoginForm
app=Flask(__name__)


posts=[
    {
    'author':'pavan p',
    'title':'blog post1',
    'content':'nothing'
    },
    {
    'author':'pavan p',
    'title':'blogpost2',
    'content':'this also nothing'
    }
]

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html',posts=posts,title='home page')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    form=RegistrationForm()
    return render_template('register.html',title='register',form=form)

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',title='login',form=form)

if __name__=='__main__':
    app.run(debug=True)