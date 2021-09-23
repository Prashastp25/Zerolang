import mimetypes
from firebase import firebase
import requests
import json
config = {
"apiKey": "AIzaSyAblsApi4a-W2mlMlSi0P_pM3IAocb6fSg",
"authDomain": "zero-ae545.firebaseapp.com",
"databaseURL": "https://zero-ae545-default-rtdb.firebaseio.com",
"projectId": "zero-ae545",
"storageBucket": "zero-ae545.appspot.com",
"messagingSenderId": "240760199305",
"appId": "1:240760199305:web:684c9d9aa67b2604624e58",
"measurementId": "G-0BHGLL4QWY"
}
print("Welcome to Zero! Please be patient while we get your prefrences. V 1.4")
db = firebase.FirebaseApplication("https://zero-ae545-default-rtdb.firebaseio.com",None)
result = db.get('/zero-ae545/Data','input')
req_data = requests.get("https://zero-ae545-default-rtdb.firebaseio.com/Data.json").json()
data_key, data_val = zip(*req_data.items())
arr_keywords = list(data_key)
arr_desire_wrds = list(data_val)
temp_store = []
def main():
    fin = input(">>>")
    temp_store.append(fin)
    for index in range(0, len(arr_keywords)):
        if(type(arr_desire_wrds[index])==dict):
            dict_key, dict_val = zip(*arr_desire_wrds[index].items())
            key_name = dict_key
            dict_list_val = []
            dict_list_key = []
            dict_list_key.append(dict_val[0])
            dict_list_val.append(dict_val[-1])
            for x in range(0, len(dict_list_key)):
                temp_store.append(temp_store[-1].replace(dict_list_val[x],dict_list_key[x]))
        else:
            temp_store.append(temp_store[-1].replace(arr_desire_wrds[index],arr_keywords[index]))
    exec(temp_store[-1])

while True:
    main()
