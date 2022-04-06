from flask import Blueprint,redirect,url_for,render_template,request,flash

bp = Blueprint('login1',__name__)

@bp.route('/',methods=['get','post'])
def login1():
    if request.method == "POST":
      res=request.form.get('email')
      passwd=request.form.get('password')
      if res == '*******' and passwd == '*******':
            return redirect(url_for('jizhang.afterlogin'))
      else:
            flash ('用户名或密码错误，请重试！')
            return render_template('/jizhang/index.html')
    if request.method == "GET":
      return render_template('/jizhang/index.html')



    
