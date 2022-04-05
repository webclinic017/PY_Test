
file = open("books.txt", "r")

for cadena in file.readlines():
    listCadena = cadena.split()
    code = ""
    for x in listCadena:
        code += x[0]
        
    print(code)

file.close()