import pymysql
class db1():
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
    
    def chaxundb(self):
        mysql=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        cur=mysql.cursor()
        sql1='select * from zhangben'
        cur.execute(sql1)
        res=cur.fetchall()
        #print(res)
        cur.close()
        return res

    def charudb(self,zhichu,shouru,yuer,beizhu):
        mysql=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        cur=mysql.cursor()
        sql = "insert into  zhangben value (now(),{0},{1},{2},'{3}')".format(zhichu,shouru,yuer,beizhu)
        cur.execute(sql)
        mysql.commit()
        res=cur.fetchall()
        #print(res)
        cur.close()
        return res
