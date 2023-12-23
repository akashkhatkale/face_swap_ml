import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCzQXmfLVSD4vg7TxO_rqtfwp7KVZP7Pj4",
    "authDomain": "faceswap-f1d83.firebaseapp.com",
    "projectId": "faceswap-f1d83",
    "storageBucket": "faceswap-f1d83.appspot.com",
    "messagingSenderId": "755495271701",
    "appId": "1:755495271701:web:00024aa06e9d7d5d04bd1c",
    "measurementId": "G-WTZCPCXGJF",
    "databaseURL": "xxxxxx"
}
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()