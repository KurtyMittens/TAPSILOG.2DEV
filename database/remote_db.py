import pyrebase


class remote_tapsilog:
    def __init__(self):
        self.tapsilog_config = {
            'apiKey': "AIzaSyBST6UlthaLkKP_7xBhpNy6H8akx2ehZZw",
            'authDomain': "tapsilog2022-d2809.firebaseapp.com",
            'databaseURL': "https://tapsilog2022-d2809-default-rtdb.asia-southeast1.firebasedatabase.app",
            'projectId': "tapsilog2022-d2809",
            'storageBucket': "tapsilog2022-d2809.appspot.com",
            'messagingSenderId': "599125571136",
            'appId': "1:599125571136:web:9b949b6c4c681eb70851a5",
            'measurementId': "G-8BB0W6LJNE"
        }

        self.firebase = pyrebase.initialize_app(self.tapsilog_config)

