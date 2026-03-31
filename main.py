# import cv2

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     for (x, y, w, h) in faces:
#         # Fake logic: assume mask if lower face darker (simple heuristic)
#         roi = gray[y:y+h, x:x+w]
#         avg_intensity = roi.mean()

#         if avg_intensity < 100:
#             label = "Mask"
#             color = (0, 255, 0)
#         else:
#             label = "No Mask"
#             color = (0, 0, 255)

#         cv2.rectangle(frame, (x,y), (x+w,y+h), color, 2)
#         cv2.putText(frame, label, (x, y-10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

#     cv2.imshow('Mask Detection', frame)

#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
print(cv2.data.haarcascades)