from pyfirmata import Arduino, SERVO
import cv2
import face_recognition

board = Arduino('COM9')

CM = 0
pto1=90
pto2=90
pto3=20
MX1=MX2=MX3=MX4=5
pw=200
cst1=90
cst2=30

pin = board.digital[3]
pin.mode = SERVO
pin2 = board.digital[5]
pin2.mode = SERVO

pin.write(pto1)
pin2.write(pto1)
pin.write(2*pto1)
pin2.write(2*pto1)
pin.write(0)
pin2.write(0)
pin.write(cst1)
pin2.write(cst2)

cap = cv2.VideoCapture(CM)

while True:
    ret, frame = cap.read()
    h, w, _ = frame.shape
    FLp = face_recognition.face_locations(frame)
    for u, r, d, l in FLp:
        C1=l+r/2-l/2
        C2=u+d/2-u/2
        d1=w/2-C1
        d2=h/2-C2
        e1=w/2/90
        e2=h/2/90
        ed1=d1/2/pto1
        ed2=d2/2/pto1
        if d1!=0:
            vd1=e1-ed1
            if ed1>0:
                pin.write(pto2+vd1*pw/100)
                if 2*pto1-pto2<MX2:
                    pto2=2*pto1-MX2
                else:
                    pto2=pto2+vd1*pw/100
            if ed1<0:
                pin.write(pto2-vd1*pw/100)
                if pto2<MX4:
                    pto2=MX4
                else:
                    pto2=pto2-vd1*pw/100
        if d2!=0:
            vdy=e2-ed2
            if ed2>0:
                pin2.write(pto3+vdy*pw/10)
                if 2*pto1-pto3<MX1:
                    pto3=2*pto1-MX1
                else:
                    pto3=pto3+vd1*pw/100
            if ed2<0:
                pin2.write(pto3-vd1*pw/100)
                if pto3<MX3:
                    pto3=MX3
                else:
                    pto3=pto3-vd1*pw/100
        cv2.rectangle(frame, (l, u), (r, d), (0, 0, 255), 2)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(30) and 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()