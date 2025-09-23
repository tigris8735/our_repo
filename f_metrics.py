import os



# открываем файл :: 
with open("metrics.md" , 'r' , encoding="utf-8") as f: 
    metrics = f.read()


# инпут имя + фамилия
name = str(input())


# функция проверки (поиск по инпуту)
print (metrics)  

# аутпут 
# зациклить 

