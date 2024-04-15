import os


with open ('Gullivers_Travels.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print (text)

chardic = dict()  #Guarda repetición de letras
counter = 0 #Caracteres que se repiten

for char in text: #Por cada letra
    if char in chardic: #Si ya estaba en el dic() significa que se repite
        if chardic[char] == 1: 
            counter += 1 #Se agrega al contador
        chardic[char] += 1 #Continua el conteo
    else:
        chardic[char] = 1 #Si la letra no esta en el diccionario, la agrega


# Función para obtener el número de repeticiones de un carácter
def get_repetitions(item):
    return item[1]

# Ordenar el diccionario por número de repeticiones de mayor a menor
sorted_chardic = sorted(chardic.items(), key=get_repetitions, reverse=True)

# Imprimir el resultado
for char, repetitions in sorted_chardic:
    print(f"character: {char}, repetitions: {repetitions}")

print("Total repited characters:", counter)

with open ('new_text.txt','w', encoding='utf-8') as newtext:
    for char, repetitions in sorted_chardic:
        newtext.write(f"character: {char}, repetitions: {repetitions}\n")