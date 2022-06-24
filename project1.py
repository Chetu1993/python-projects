import sys
import clipboard
import json
#print(sys.argv[1:])

SAVED_DATA="clipboard.json"
def save_data(filepath,data):
    with open(filepath,"w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath,"r") as f:
            data=json.load(f)
            return data
    except:
        return {}

save_data("test.json",{"key":"value"})




if len(sys.argv)==2:
    command=sys.argv[1]
    data=load_data(SAVED_DATA)


    if command=="save":
        key=input("enter a key:",)
        data[key]=clipboard.paste()
        save_data(SAVED_DATA,data)
        print("data saved")
    if command=="load":
        key = input("enter a key:", )
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard.")
        else:
            print("key does not exist")
    elif command=="list":
        key = input("enter a key:", )
        print(data)
    #else:
     #   print("unknown command")

print("please pass exactly one command")
