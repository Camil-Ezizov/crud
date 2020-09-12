import json
import os
#json dan melumati oxumaq
def melumatiOxu(_fileName):
    with open(_fileName,"r") as connect:
        return json.load(connect)
data=melumatiOxu("c:/Users/Lenovo/Desktop/python/crudtest/data.json")
for item in data['mehsullar']:
     print(f"{item['mehsulId']} :{item['mehsulName']} | {item['mehsulQiymeti']} | {item['mehsulSayi']} | {item['mehsulKateqoriyasi']}")


 