import json
#jsondan melumati silmek
def melumatiOxu(_fileName):
    with open(_fileName,"r") as connect:
        return json.load(connect)
data=melumatiOxu("c:/Users/Lenovo/Desktop/python/crudtest/data.json")

mehsulId=int(input("mehsulun ID sini secerek mehsulu silmek:"))


for item in data['mehsullar']:
    if item['mehsulId']==mehsulId:
        data['mehsullar'].remove(item)
with open("c:/Users/Lenovo/Desktop/python/crudtest/data.json","w") as connect:
    json.dump(data,connect)