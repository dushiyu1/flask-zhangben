import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)

from flask import Blueprint,request,render_template
import dbsql

bp = Blueprint("jizhang",__name__)

adddatalist=[]
shourulist=[]
zhichulist=[]
yuerlist=[]
beizhulist=[]
iteamlist=set()
i=0

def addlist(res1):
    adddatalist.append(res1[i][0])
    shourulist.append(res1[i][1])
    zhichulist.append(res1[i][2])
    yuerlist.append(res1[i][3])
    beizhulist.append(res1[i][4])
    iteamlist.add(i)


@bp.route('/afterlogin',methods=['post','get'])
def afterlogin():
    global zhichuheji,shouruheji,yuerheji,i
    if request.method == "POST":
        shouru = float(request.form.get('shouru'))
        zhichu = float(request.form.get('zhichu'))
        beizhu = request.form.get('beizhu')
        yuer =  round(float(shouru)-float(zhichu),2)
        if shouru != '' and zhichu != '' and beizhu != '' and shouru != None and zhichu != None and beizhu != None:
            mysql=dbsql.db1()
            res=mysql.charudb(shouru=shouru,zhichu=zhichu,yuer=yuer,beizhu=beizhu)
            res1=mysql.chaxundb()
            addlist(res1)
            print(adddatalist)
            print(shourulist)
            print(zhichulist)
            print(yuerlist)
            print(beizhulist)
            print(iteamlist)
            shouruheji=sum(shourulist)
            zhichuheji=sum(zhichulist)
            yuerheji=sum(shourulist)-sum(zhichulist)

            i+=1

        return render_template('/jizhang/afterlogin.html',shouruheji=shouruheji,zhichuheji=zhichuheji,yuerheji=yuerheji,yuerlist=yuerlist,adddatalist=adddatalist,shourulist=shourulist,zhichulist=zhichulist,beizhulist=beizhulist,iteamlist=iteamlist)
    elif request.method == "GET":
        mysql=dbsql.db1()
        res1=mysql.chaxundb()
    
        for i in range(0,len(res1)):
            addlist(res1)
   
        print(iteamlist)

        shouruheji=sum(shourulist)
        zhichuheji=sum(zhichulist)
        yuerheji=sum(shourulist)-sum(zhichulist)


        return render_template('/jizhang/afterlogin.html',yuerlist=yuerlist,adddatalist=adddatalist,shourulist=shourulist,zhichulist=zhichulist,beizhulist=beizhulist,iteamlist=iteamlist,zhichuheji=zhichuheji,shouruheji=shouruheji,yuerheji=yuerheji)
       
