# 동영상 프로세싱

import datetime
from datetime import timedelta
import time
import webbrowser
from glob import glob
import os
import cv2
fourcc = cv2.VideoWriter_fourcc(*'XVID')
capture = cv2.VideoCapture("/Users/kimseonmin/Downloads/bang.mov")

frame_len = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
record = False;
recordNum = 0
width = int(capture.get(3))  # 가로

height = int(capture.get(4))  # 세로값 가져와서
print(width);
print(height);
print(frame_len);

num = int(0)
list = []
f = open('/Users/kimseonmin/PycharmProjects/untitled6/test.txt', mode='wt', encoding='utf-8')

current_time = datetime.datetime.today()
print(current_time)
while (capture.isOpened):

    num1 = len(os.walk('/Users/kimseonmin/PycharmProjects/untitled6/static').__next__()[2])-1;

    ret, frame = capture.read()
    if ret == False:
        break

    cv2.imshow("VideoFrame", frame)

    now = datetime.datetime.now().strftime("%d_%H-%M-%S")

    key = cv2.waitKey(33)  # 1) & 0xFF

    if key == 50:  # esc 종료
        #record = False
        #print("녹화중")
        #video.release()
        webbrowser.open("http://127.0.0.1:5000/")
        break

    elif key == 51:  # ctrl + z
        num = num1 + 1
        print("click");

        #cv2.IMREAD_UNCHANGED
        print("click2");

        cv2.imwrite("/Users/kimseonmin/PycharmProjects/untitled6/static/pic"+ str(num) + ".png", frame)
        current_time2 = datetime.datetime.today()
        print(current_time2 - current_time)
        f.write(str((current_time2-current_time).seconds)+':'+str((current_time2-current_time).microseconds)+'\n')

        #record = True
        #video = cv2.VideoWriter("/Users/kimseonmin/Documents/" + str(now) + ".mp4", fourcc, 0.1, (frame.shape[1], frame.shape[0]))
        #recordNum=recordNum+1;


        list.append(str((current_time2-current_time).seconds)+':'+str((current_time2-current_time).microseconds))
        print(list)
        print("click3");
        #if record == True:
         #   print("녹화 중..")
          #  video.write(frame)

#current_time2 = datetime.datetime.today()
#print(current_time2)
#print(current_time2-current_time)

capture.release()
cv2.destroyAllWindows()







