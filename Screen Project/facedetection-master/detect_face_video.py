import cv2,wx,time

app=wx.App()
dc=wx.ScreenDC()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:

    dc.SetBrush(wx.Brush("black",wx.SOLID)) 
    dc.SetPen(wx.Pen((0, 0, 0), width=3, style=wx.PENSTYLE_SOLID))
    x=0;y=0;w=0;h=0
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    print("%d %d   %d %d"%(x,y,w,h))

    dc.DrawRectangle(x,y,w,h)
'''
    time.sleep(2)
'''

    dc.SetBrush(wx.TRANSPARENT_BRUSH) 
    dc.SetPen(wx.TRANSPARENT_PEN)

    dc.DrawRectangle(x,y,w,h)
'''
    dc.Clear()
    dc.ClearBackground()

    dc.RefreshRect()
'''
    cv2.imshow('Capture', img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
  
cap.release()