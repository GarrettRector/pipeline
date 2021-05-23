import requests

'''
    raw_arr = 2d array of size [n][2]
    arr[0][0] = field 1, arr[0][1] = value 1
    arr[1][0] = field 2, arr[1][1] = value 2
    arr[2][0] = field 3, arr[2][1] = value 3
    .....
    arr[n][0] = field n, arr[n][1] = value n
'''
def create_add_args(raw_arr, password, filename):
    storage = "add,"
    storage += filename + ","
    storage += "password:" + str(password)
    for i in range(len(raw_arr)):
        if (i < (len(raw_arr))):
            storage += ","
        storage += str(raw_arr[i][0]) + ":" + str(raw_arr[i][1])
    return storage

def create_read_args(filename, password):
    return "read," + str(filename) + ",password:" + password

def send(address, args):
    r = requests.get(address + "/" + args)
    return r.text

def parse(raw, field):
    arr = raw.split(",")
    for term in arr:
        if field + ":" in term:
            return term.split(":")[1]
    return "client error - field not found: " + field
