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
f.write('test\n')
current_time = datetime.datetime.today()
print(current_time)

while (capture.isOpened):

    num1 = len(os.walk('/Users/kimseonmin/PycharmProjects/untitled6/static').__next__()[2])-1;
    ret, frame = capture.read()
    if ret == False:
        break

    cv2.imshow("VideoFrame", frame)






capture.release()
cv2.destroyAllWindows()







