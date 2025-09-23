import os



# открываем файл :: 
with open("metrics.md" , 'r' , encoding="utf-8") as f: 
    metrics = f.read()

tables = metrics.split("№")

while True :

    name = str(input())

    i = 0


    for table in tables:
        if name in table:
            print("№"+table)
            break
