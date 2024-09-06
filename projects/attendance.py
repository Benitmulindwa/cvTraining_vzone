import face_recognition
import cv2 as cv
import numpy as np
from datetime import datetime

cap = cv.VideoCapture(0)

benit_img = face_recognition.load_image_file("assets/9876.jpg")
benit_encod = face_recognition.face_encodings(benit_img)[0]

elon_img = face_recognition.load_image_file("assets/elon.jpg")
elon_encod = face_recognition.face_encodings(elon_img)[0]

known_face_encodings = [benit_encod, elon_encod]
known_face_names = ["Benit", "Elon Musk"]
"""
|nom|Date|Heure|

nom,date,heure
"""

date = datetime.now().date().strftime("%d/%m/%Y")
heure = datetime.now().time().strftime("%H:%M")


#Une fonction qui Ajoute le nom de la personne detectEe dans un fichier .csv 
def add_presence(name):
    with open("files/attendance.csv", "r+") as f:
        mydata = f.readlines()
        namelist = []
        for line in mydata:
            entry = line.split(",")
            namelist.append(entry[0])
        if name not in namelist:
            f.writelines(f"\n{name},{date},{heure}")


face_locations = []
face_encodings = []
face_names = []
etat = True

while True:
    ret, frame = cap.read()

    # Only process every other frame of video to save time
    if etat:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = cv.cvtColor(small_frame, cv.COLOR_BGR2RGB)

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations
        )

        face_names = []
        for face_encoding in face_encodings:
            # Verifie si la face detecEe est parmi face(s) connues
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding
            )  # -> [True,False]
            name = "Unknown"
            # 0-1
            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding
            )

            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            add_presence(name)

            face_names.append(name)

    etat = not etat

    # Resultats
    for (top, right, bottom, left), name in zip(face_locations, face_names):

        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Dessine un rectangle autour de la face detectEe
        cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Dessine un petit rectangle avec le nom de la personne dessus
        cv.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), -1)
        cv.putText(
            frame,
            name,
            (left + 6, bottom - 6),
            cv.FONT_HERSHEY_DUPLEX,
            1.0,
            (255, 255, 255),
            1,
        )

    cv.imshow("Video", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
