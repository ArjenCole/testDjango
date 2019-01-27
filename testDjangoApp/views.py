from django.shortcuts import render
from django.shortcuts import HttpResponse
import pymysql


# Create your views here.
user_list = [
    {"user": "jack", "pwd": "abc"},
    {"user": "tom", "pwd": "ABC"},
]


def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='test_schema')    # db:表示数据库名称
    return conn


def insert(sql, args):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()


def query(sql, args):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql, args)
    results = cur.fetchall()
    print(type(results))  # 返回<class 'tuple'> tuple元组类型
    user_list.clear()
    for row in results:
        print(row)
        name = row[1]
        pwd = row[2]
        user_list.append({"user": name, "pwd": pwd})
        pass
    conn.commit()
    cur.close()
    conn.close()


def index(request):
    if request.method == "POST":
        tusername = request.POST.get("username", None)
        tpassword = request.POST.get("password", None)
        sql = 'INSERT INTO test_table(NAME,PASSWORD)  VALUES(%s,%s);'
        insert(sql, (tusername, tpassword))

    sql = 'SELECT * FROM test_table;'
    query(sql, None)

    return render(request, "index.html", {"data": user_list})
