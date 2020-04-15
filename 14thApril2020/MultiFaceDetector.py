import cv2
cap = cv2.VideoCapture(0)
face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count = []
while True:
    status, photo = cap.read()
    face = face_model.detectMultiScale(photo)
    if len(face)==0:
        pass
    else:
        # For multiple face
        # While loop can also be used here
        for x in range(len(face)):
            x1 = face[x][0]
            y1 = face[x][1]
            x2 = x1 + face[x][2]
            y2 = y1 + face[x][3]          
            photo = cv2.rectangle(photo, (x1,y1), (x2,y2), [0,255,0], 3)
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (10,50)
    fontScale = 2
    fontColor = (255,255,255)
    lineType = 2
    cv2.putText(photo, str(len(face)), org, font, fontScale, fontColor, 10, cv2.LINE_AA, False)
    
    count.append(len(face))
    cv2.imshow('hell', photo)
    if cv2.waitKey(1) == 13:
            break
cv2.destroyAllWindows()
cap.release()
count1 = sum(count)/len(count)

import statistics 
# To find most frequent no of faces in Array
count2 = statistics.mode(count)

count3 = max(count)
count4 = min(count)

attandance = "Attandance Average: '{}' \nAttandance Mode(Max frequency): '{}' \n Attandance Max recorded: '{}' \n Attandance Max recorded: '{}'".format(count1,count2,count3,count4)
print(attandance)
#Using smtplib other alternative was through Gmail API
import smtplib

# importing MIME for standard Email template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content = attandance

# You can also input you password here since entering password while running lead to security issues
sender_address = input("Sender address : ")
sender_pass = input("Sender password : ")
receiver_address = input("Receiver address : ")

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Attandance of Students'

message.attach(MIMEText(mail_content, 'plain'))

#Using Gmail SMTP server 
session = smtplib.SMTP('smtp.gmail.com', 587) 
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Your mail has been Sent')
