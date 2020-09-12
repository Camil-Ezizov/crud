import json
#jsondan melumati oxu
def melumatiOxu(_fileName):
    with open(_fileName,"r") as connect:
        return json.load(connect)
data=melumatiOxu("c:/Users/Lenovo/Desktop/python/crudtest/data.json")

#jsona melumati yazmaq
def melumatYaz():
    Id=int(input("Mehsul idsi: "))
    ad=input("Mahsul adi: ")
    qiymet=float(input("Mehsul qiymeti: "))
    say=int(input("Mehsulun sayi: "))
    kateqoriyasi=input("Mehsulun kateqoriyasi: ")

    #yeni dict yarat
    mehsul={
        "mehsulId":Id,
        "mehsulName":ad,
        "mehsulQiymeti":qiymet,
        "mehsulSayi":say,
        "mehsulKateqoriyasi":kateqoriyasi
    }
    data['mehsullar'].append(mehsul)
    with open("c:/Users/Lenovo/Desktop/python/crudtest/data.json","w") as connect:
         json.dump(data,connect)
melumatYaz()