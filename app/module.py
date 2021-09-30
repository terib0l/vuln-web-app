import sqlite3, json

def data_to_dict(data):
    objects = [] 

    for i in range(len(data)):
        dict = {}
        dict["id"] = data[i][0]
        dict["title"] = data[i][1]
        dict["answer"] = data[i][2]
        dict["image"] = data[i][3]

        objects.append(dict)

    return objects
