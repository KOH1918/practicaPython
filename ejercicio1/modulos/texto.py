#abrir y leer archivo de texto
def abrir():
    with open("recursos\\log.txt", encoding= "UTF-8") as archivo:
        archivo = archivo.read()
        print (archivo)

#editar achivo de texto
def escribir(txt):
    
    with open("recursos\\log.txt", "w", encoding= "UTF-8") as archivo:
        archivo = archivo.write(f"{txt}\n")
