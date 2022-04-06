from jizhang.login1 import bp as bp1
from jizhang.jizhang import bp as bp2
from flask import Flask,render_template


app=Flask(__name__)
app.register_blueprint(bp1)
app.register_blueprint(bp2)
app.config["SECRET_KEY"]='dushiyuwoaini'

@app.route('/register',methods=['get','post'])
def register():
    return render_template('/jizhang/register.html')

@app.route('/forget',methods=['get','post'])
def forgot():
    return render_template('/jizhang/forgot.html')

@app.route('/test')
def test():
    return render_template('/jizhang/test.html') 

@app.route('/error')
def error():
    return render_template('/jizhang/error.html')



if __name__ == "__main__":
    app.run(debug=True)
