from PIL import Image
from pytesseract import *
import os
import re
import cv2
import datetime
from flask_opencv_streamer.streamer import Streamer
from flaskext.mysql import MySQL
import pymysql
from flask import Flask, render_template, request, url_for,make_response, render_template, Response
from werkzeug.utils import redirect

app = Flask(__name__)

mysql = MySQL()

rocky = 0
timeList = []
preTimeList = []
#f = open("/Users/kimseonmin/PycharmProjects/untitled6/test.txt", 'r')
#lines = f.readlines()
#for line in lines:
#    timeList.append(line)
#f.close()
#print(timeList)
pnumber=0
num2=0
asap=''
asap2=''
delnum2=[]
delnum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#num2 = len(os.walk('/Users/kimseonmin/PycharmProjects/untitled6/static').__next__()[2]);
#print(num2)
realList=[]
list = []
testList = []
imgList = []
common = 0
#for i in range(num2-1):
#    print(i)
#    img = Image.open('/Users/kimseonmin/PycharmProjects/untitled6/static/pic' + str(i + 1) + '.png')
#
#    text = pytesseract.image_to_string(img, lang='kor')
#    print(text)
#    list.append(text)
#print(list)



@app.route('/',methods=['GET','POST'])
def index():
    global timeList
    global list
    global testList
    global imgList
    global asap
    global asap2
    global realList
    global preTimeList
   # realList=[]
   # testList=[]

    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='project', charset='utf8')
    cursor = conn.cursor()

    query = "SELECT commonkey FROM information ORDER BY commonkey DESC limit 1"
    query2 = "SELECT img FROM information ORDER BY idx DESC limit 1"

    cursor.execute("set names utf8")
    cursor.execute(query)
    asap = (cursor.fetchall()[0][0])
    print(asap)

    cursor.execute(query2)

    asap2 = (cursor.fetchall()[0][0])
    cursor.execute(query2)
    a = cursor.fetchall()
    print(asap2)
    cursor.close()
    conn.close()
    print(a)

    f = open("/Users/kimseonmin/PycharmProjects/untitled6/test.txt", 'r')
    lines = f.readlines()

    for line in lines:
        timeList.append(line)
    f.close()
    print(timeList)
    global rocky
    global num2
    num2 = len(os.walk('/Users/kimseonmin/PycharmProjects/untitled6/static').__next__()[2])-1;
    num4 = int(asap2)
    num3 = int(asap2)
    print('num2-num3')
    print(num2-num3)
    print("num2")
    print(num2)
    print(num3)


    for i in range(num2-num3):

        if(rocky==1):
            break;
        print(i)
        img = Image.open('/Users/kimseonmin/PycharmProjects/untitled6/static/pic' + str(num3 + 1) + '.png')
        num3=int(num3)+1
        text = pytesseract.image_to_string(img, lang='kor')
        print(text)
        print(num4)
        realList.append([str(num3),text,i+1,timeList[i]])
        list.append(text)
        testList.append([str(num3),text,i+1,timeList[i]])

    rocky = 1
    print(list)
    print(imgList)
    print("realist")
    print(realList)


    print(num2-num3);
    print(list.__len__()-1)

    return render_template('index.html',list=list,timeList=timeList,num4=num4,delnum2=delnum2,testList=testList,realList=realList)

@app.route('/test', methods=['POST'])
def indexd():
    global delnum

    value = request.form['dnum']
    value2 = request.form['dnum2']
    print("value")
    print(value)
    print("value2")
    print(value2)
    value = int(value)
    value2 = int(value2)
    delnum[value2-1]=value2
    global list
    del list[value-1]
    del realList[value-1]
    print(list)
    print('delnum')
    print(delnum)
    return redirect('/')



@app.route('/login', methods=['post', 'get'])
def login():
    error = None
    if request.method == 'GET':

        conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='project', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT * FROM information"

        cursor.execute("set names utf8")
        cursor.execute(query)
        data = (cursor.fetchall())

        cursor.close()
        conn.close()


        for row in data:
            print(row)

        # return redirect(url_for('success', name=user))

    return render_template('c.html', error=error)


@app.route('/register', methods=['post'])
def regist():
    error = None
    global delnum
    global rocky
    global testList
    global realList
    global delnum
    common = int(asap);
    img = int(asap2)
    num2 = len(os.walk('/Users/kimseonmin/PycharmProjects/untitled6/static').__next__()[2])-1;
    num3 = int(asap2)


  #  for j in range((num2 - num3)-delnum.__len__()):
   #     delnum.append('0')
    #    print('new delnum')
     #   print(delnum)

    if request.method == 'POST':
        common = common+1
        title = request.form['title']
        conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='project', charset='utf8')
        cursor = conn.cursor()


        for i in range(num2 - num3):
            img = img+1

            content = testList[i][1]
            commonkey = common
            delpoint = delnum[i]
            time=testList[i][3]
            query = "INSERT INTO information (img, content, title, commonkey, delnum, time) values (%s, %s, %s, %s, %s, %s)"
            value = (img, content, title, commonkey, delpoint, time)
            cursor.execute(query,value)


        conn.commit()

        cursor.close()
        conn.close()
        rocky = 0
        realList=[]
        testList=[]
        delnum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


        # return redirect(url_for('success', name=user))

    return redirect('/list')

@app.route('/update', methods=['post'])
def update():
    global realList
    if request.method == 'POST':

        t1 = request.form['t1']
        t2 = request.form['t2'] #고유값
        t3 = request.form['t3'] #인덱스
        print(t1)
        print(t2)
        s=int(t2)-1
        ss = int(t3) - 1
        #list[s] = t1
        testList[s][1]=t1
        try:
            realList[ss][1] = t1
        except TypeError:
            print("ok")

        print("reallists")
        #print(realList[s][1])
        print(list)
        return redirect('/')

        # return redirect(url_for('success', name=user))

@app.route('/list', methods=['post', 'get'])
def getList():
    error = None
    if request.method == 'GET':

        conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='project', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT * FROM information"

        cursor.execute("set names utf8")
        cursor.execute(query)
        data = (cursor.fetchall())
        print(data)

        cursor.close()
        conn.close()

        ps = 0
        ds = []
        for row in data:

            if(row[4] != ps):
                ds.append(row)
            ps = row[4]
        print(ds)


        # return redirect(url_for('success', name=user))

    return render_template('list.html', datas=data,ds=ds)


@app.route('/detail', methods=['post', 'get'])
def getDetail():
    error = None
    if request.method == 'POST':
        global pnumber
        pnumber = request.form['p']
        print(pnumber)

        conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='project', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT * FROM information WHERE commonkey=%s"
        value=(pnumber)

        cursor.execute("set names utf8")
        cursor.execute(query,value)
        data = (cursor.fetchall())
        print(data)

        cursor.close()
        conn.close()
        pss = []
        for row in data:
            print(row)

        for s in data:
            if(s[5]=='0'):
                pss.append(s)

    return render_template('detail.html',datas=pss)

@app.route('/detailUpdate', methods=['post', 'get'])
def getDetailUpdate():
    error = None
    if request.method == 'POST':
        t0 = request.form['t0']
        t1 = request.form['t1']
        print("t0")
        print(t0)
        print(t1)

        conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='project', charset='utf8')
        cursor = conn.cursor()

        query = "UPDATE `information` SET `content`=%s WHERE `idx`=%s"
        value=(t1,t0)

        cursor.execute("set names utf8")
        cursor.execute(query,value)
        conn.commit()

        query2 = "SELECT * FROM information WHERE commonkey=%s"
        value = (pnumber)

        cursor.execute("set names utf8")
        cursor.execute(query2, value)
        data = (cursor.fetchall())
        print(data)

        cursor.close()
        conn.close()
        pss = []
        for row in data:
            print(row)

        for s in data:
            if (s[5] == '0'):
                pss.append(s)


    return render_template('detail.html',datas=pss)


@app.route('/detailDelete', methods=['post', 'get'])
def getDetailDelte():
    error = None
    if request.method == 'POST':
        t3 = request.form['t3']
        t4=1

        print("t3")
        print(t3)

        conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='project', charset='utf8')
        cursor = conn.cursor()

        query = "UPDATE `information` SET `delnum`=%s WHERE `idx`=%s"
        value=(t4,t3)

        cursor.execute("set names utf8")
        cursor.execute(query,value)
        conn.commit()

        query2 = "SELECT * FROM information WHERE commonkey=%s"
        value = (pnumber)

        cursor.execute("set names utf8")
        cursor.execute(query2, value)
        data = (cursor.fetchall())
        print(data)

        cursor.close()
        conn.close()
        pss = []
        for row in data:
            print(row)

        for s in data:
            if (s[5] == '0'):
                pss.append(s)


    return render_template('detail.html',datas=pss)

@app.route('/sumnail', methods=['post', 'get'])
def getSumnail():
    error = None
    if request.method == 'POST':
        number = request.form['nail']
        print(number)

        conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='project', charset='utf8')
        cursor = conn.cursor()

        query = "SELECT * FROM information WHERE commonkey=%s"
        value=(number)

        cursor.execute("set names utf8")
        cursor.execute(query,value)
        data = (cursor.fetchall())
        print(data)

        cursor.close()
        conn.close()
        pss = []
        for row in data:
            print(row)

        for s in data:
            if(s[5]=='0'):
                pss.append(s)

    return render_template('sum.html',datas=pss)

@app.after_request
def set_response_headers(r):
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    r.headers['Pragma'] = 'no-cache'
    r.headers['Expires'] = '0'
    return r

if __name__ == '__main__':
    app.debug = True
    app.run()




