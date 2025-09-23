import os



# открываем файл :: 
with open("metrics.md" , 'r' , encoding="utf-8") as f: 
    metrics = f.read()

tables = metrics.split("№")


name = str(input('!Важно! : если вы напишете только имя , программа выдаст метрики всех людей ,\n чьи имена совпадают '))

i = 0


for table in tables:
    if name in table:
        print("№"+table)
    else :
        i+=1

if i != 0 :
    print ('информация не найдена')