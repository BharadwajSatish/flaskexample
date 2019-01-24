from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    marks={'Maths':80,'c':40,'java':90}
    return render_template('mar.htm',marks=marks)

if __name__=="__main__":
    app.run(debug=True)
    
