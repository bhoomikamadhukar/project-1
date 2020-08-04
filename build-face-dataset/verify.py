import face_recognition 
known_image = face_recognition.load_image_file("C:/Users/Madhukar/Downloads/build-face-dataset/build-face-dataset/video-match/final/00000.png") 
unknown_image = face_recognition.load_image_file("C:/Users/Madhukar/Downloads/build-face-dataset/build-face-dataset/examples/example_01.jpg") 
 
biden_encoding = face_recognition.face_encodings(known_image)[0] 
unknown_encoding = face_recognition.face_encodings(unknown_image)[0] 
 
results = face_recognition.compare_faces([biden_encoding], unknown_encoding) 
print(results)

