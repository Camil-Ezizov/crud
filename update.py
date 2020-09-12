import json
#jsondan melumati oxumaq
def melumatiOxu(_fileName):
    with open(_fileName,"r") as connect:
        return json.load(connect)
data=melumatiOxu("c:/Users/Lenovo/Desktop/python/crudtest/data.json")

mehsulId=int(input("Mehsulun ID sin yaz: "))
yeniQiymet=int(input("Mehsulun yeni qiymetini daxil et: "))

for item in data['mehsullar']:
    if item['mehsulId']==mehsulId:
        item['mehsulQiymeti']=yeniQiymet

with open("c:/Users/Lenovo/Desktop/python/crudtest/data.json","w") as connect:
    json.dump(data,connect)


