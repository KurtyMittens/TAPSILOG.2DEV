import math
from sklearn import neighbors
import os
import os.path
import pickle
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
import numpy as np


class HUCK:
    def __init__(self):
        self.trained_dir = []
        self.trained_face = []
        self.progress = 0


    def train_huck(self, train_dir, huck_model_save=None, nNeighbors=None, verbose=False, algo='ball_tree'):
        for class_dir in os.listdir(train_dir):
            if not os.path.isdir(os.path.join(train_dir, class_dir)):
                continue

            for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
                image = face_recognition.load_image_file(img_path)
                face_bounding_boxes = face_recognition.face_locations(image)

                for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
                    image = face_recognition.load_image_file(img_path)
                    face_bounding_boxes = face_recognition.face_locations(image)

                    if len(face_bounding_boxes) != 1:
                        # If there are no people (or too many people) in a training image, skip the image.
                        if verbose:
                            print("Image {} not suitable for training: {}".format(img_path, "Didn't find a face" if len(
                                face_bounding_boxes) < 1 else "Found more than one face"))
                    else:
                        # Add face encoding for current image to the training set
                        self.trained_dir.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
                        self.trained_face.append(class_dir)


        # Determine how many neighbors to use for weighting in the KNN classifier
        if nNeighbors is None:
            n_neighbors = int(round(math.sqrt(len(self.trained_dir))))
            if verbose:
                print("Chose n_neighbors automatically:", n_neighbors)

        # Create and train the KNN classifier
        knn_clf = neighbors.KNeighborsClassifier(n_neighbors=nNeighbors, algorithm=algo, weights='distance')
        (knn_clf.fit(self.trained_dir, self.trained_face))
        # Save the trained KNN classifier
        if huck_model_save is not None:
            with open(huck_model_save, 'wb') as f:
                pickle.dump(knn_clf, f)

        self.progress = 1
        return knn_clf

    def huck_predicts(self, frame, knn_clf=None, clf=None, model_path=None, threshold=0.5):

        if knn_clf is None and model_path is None:
            raise Exception("Must supply knn classifier either thourgh knn_clf or model_path")

        # Load a trained KNN model (if one was passed in)
        if knn_clf is None:
            with open(model_path, 'rb') as f:
                knn_clf = pickle.load(f)

        X_face_locations = face_recognition.face_locations(frame)

        # If no faces are found in the image, return an empty result.
        if len(X_face_locations) == 0:
            return []

        # Find encodings for faces in the test image
        faces_encodings = face_recognition.face_encodings(frame, known_face_locations=X_face_locations)

        # Use the KNN model to find the best matches for the test face
        closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)
        are_matches = [closest_distances[0][i][0] <= threshold for i in range(len(X_face_locations))]

        # Predict classes and remove classifications that aren't within the threshold
        return [(pred, loc) if rec else ("unknown", loc) for pred, loc, rec in
                zip(knn_clf.predict(faces_encodings), X_face_locations, are_matches)]


