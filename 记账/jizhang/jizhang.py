import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)

import pymysql
from flask import Blueprint,request,render_template
import dbsql

bp = Blueprint("jizhang",__name__)

adddatalist=[]
shourulist=[]
zhichulist=[]
yuerlist=[]
beizhulist=[]
iteamlist=[]

@bp.route('/afterlogin',methods=['post','get'])
def afterlogin():
    global zhichuheji,shouruheji,yuerheji
    if request.method == "POST":
        shouru = float(request.form.get('shouru'))
        zhichu = float(request.form.get('zhichu'))
        beizhu = request.form.get('beizhu')
        yuer =  round(float(shouru)-float(zhichu),2)
        if shouru != '' and zhichu != '' and beizhu != '' and shouru != None and zhichu != None and beizhu != None:
            mysql=dbsql.db1(host='****',user='****',password='****',database='****')
            #res=mysql.charudb(shouru=shouru,zhichu=zhichu,yuer=yuer,beizhu=beizhu)
     
            for i in range(0,len(res)):
                adddatalist.append(res[i][0])
                shourulist.append(res[i][1])
                zhichulist.append(res[i][2])
                yuerlist.append(res[i][3])
                beizhulist.append(res[i][4])
                iteamlist.append(i)
            print(adddatalist)
            print(shourulist)
            print(zhichulist)
            print(yuerlist)
            print(beizhulist)
            print(iteamlist)
            shouruheji=sum(shourulist)
            zhichuheji=sum(zhichulist)
            yuerheji=sum(shourulist)-sum(zhichulist)

        return render_template('/jizhang/afterlogin.html',shouruheji=shouruheji,zhichuheji=zhichuheji,yuerheji=yuerheji,zhichu=zhichu,shouru=shouru,yuer=yuer,beizhu=beizhu,zhichulist=zhichulist,shourulist=shourulist,yuerlist=yuerlist,beizhulist=beizhulist)
    elif request.method == "GET":
        mysql=dbsql.db1(host='****',user='****',password='****',database='****')
        res=mysql.chaxundb()
    
        for i in range(0,len(res)):
            adddatalist.append(res[i][0])
            shourulist.append(res[i][1])
            zhichulist.append(res[i][2])
            yuerlist.append(res[i][3])
            beizhulist.append(res[i][4])
            iteamlist.append(i)
   
        print(iteamlist)
        if len(res) == 0:
            return render_template('/jizhang/afterlogin1.html')
   
       
        zhichuheji=sum(zhichulist)
        shouruheji=sum(shourulist)
        yuerheji=sum(shourulist)-sum(zhichulist)

        return render_template('/jizhang/afterlogin1.html',yuerlist=yuerlist,adddatalist=adddatalist,shourulist=shourulist,zhichulist=zhichulist,beizhulist=beizhulist,iteamlist=iteamlist,zhichuheji=zhichuheji,shouruheji=shouruheji,yuerheji=yuerheji)
       
