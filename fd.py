import cv2
import tkinter
window=tkinter.Tk()

window.title("FaceD")
def gui1():
    n=int(e1_val.get())
    cap=cv2.VideoCapture(0)
    face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    i=0
    while(True and i<n) :

        check,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
        for x,y,w,h in faces:
            frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)
        ri=cv2.resize(frame,(int(frame.shape[1]/3),int(frame.shape[0]/3)))
        cv2.imshow("1st",frame)
        out = cv2.imwrite('captn'+str(i)+'.jpg', frame)
        if cv2.waitKey(1) & 0xFF== ord('q') :
            break
        i=i+1
    cap.release()
    cv2.destroyAllWindows()
l1=tkinter.Label(window,text='Enter the number of pictures you want to take :')
l1.grid(row=0,column=0)
b1=tkinter.Button(window,text="Enter",command=gui1)
b1.grid(row=2,column=1)
e1_val=tkinter.StringVar()
e1=tkinter.Entry(window,textvariable=e1_val)
e1.grid(row=1,column=1)


window.mainloop()
