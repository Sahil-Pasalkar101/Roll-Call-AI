
import dlib
import sklearn
import numpy as np 
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st 

from src.database.db import get_all_images 

@st.cache_resource
def load_dlib_models():
    # Load the face detection model
    detector = dlib.get_frontal_face_detector() # type: ignore

    # Load the shape predictor model
    sp = dlib.shape_predictor(face_recognition_models.pose_predictor_model_location()) # type: ignore

    # Load the face recognition model
    facerec = dlib.face_recognition_model_v1(face_recognition_models.face_recognition_model_location()) # type: ignore

    return detector, sp, facerec


def get_face_embedding(image_np):
    detector,sp,facerec = load_dlib_models()
    faces = detector(image_np,1)

    encodings = []

    for face in faces:
        shape = sp(image_np,face)
        face_descriptor = facerec.compute_face_descriptor(image_np,shape,1) # 128 embdding

        encodings.append(np.array(face_descriptor))
    return encodings 
@st.cache_resource
def get_trained_model():

    X = []
    y = []

    student_db = get_all_images()

    if not student_db:
        return None

    # Collect all student embeddings first
    for student in student_db:
        embedding = student.get("face_embedding")

        if embedding:
            X.append(np.array(embedding))
            y.append(student.get("student_id"))

    # No face embeddings found
    if len(X) == 0:
        return None

    # SVC needs at least 2 different students/classes
    if len(set(y)) < 2:
        return {
            "clf": None,
            "X": X,
            "y": y
        }

    clf = SVC(
        kernel="linear",
        probability=True,
        class_weight="balanced"
    )

    try:
        clf.fit(X, y)

    except ValueError as e:
        print("Classifier training error:", e)
        return None

    return {
        "clf": clf,
        "X": X,
        "y": y
    }

def train_classifier():
    st.cache_resource.clear()

    print("TRAIN CLASSIFIER: started")

    model_data = get_trained_model()

    print("TRAIN CLASSIFIER: get_trained_model finished")
    print("TRAIN CLASSIFIER: model_data =", model_data)

    if model_data is None:
        print("TRAIN CLASSIFIER: No model data")
        return False

    print("TRAIN CLASSIFIER: completed")

    return True

def predict_attendance(class_image_np): 

    encoding = get_face_embedding(class_image_np)

    detected_student = {}

    # No face detected
    if encoding is None or len(encoding) == 0:
        return detected_student, [], 0

    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encoding)

    clf = model_data['clf']  # type: ignore
    X_train = model_data['X']  # type: ignore
    y_train = model_data['y']  # type: ignore

    all_students = sorted(list(set(y_train)))

    # No trained students
    if len(all_students) == 0:
        return detected_student, [], len(encoding)

    for current_encoding in encoding:

        if len(all_students) >= 2:
            predicted_id = int(clf.predict([current_encoding])[0])
        else:
            predicted_id = int(all_students[0])

        student_embedding = X_train[y_train.index(predicted_id)]

        best_match_score = np.linalg.norm(
            student_embedding - current_encoding
        )

        resemblance_threshold = 0.6

        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True

    return detected_student, all_students, len(encoding)