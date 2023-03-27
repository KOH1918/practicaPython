#se importa el modulo desde el archivo texto.py y se define como "t"
import modulos.texto as t
import msvcrt
import sys

def func():
    #recibimos el texto para escribir en "log.txt"
    print ('cambia el texto de arriba:')
    while True:
        #leemos la siguiente tecla a presionar
        if msvcrt.kbhit():
            key_stroke = msvcrt.getche()
            #si la tecla es escape, se sale del programa
            if key_stroke==chr(27).encode():
                print ("adios!")
                sys.exit()
            else:
                #modificamos el archivo "log.txt" y salimos del bucle para continuar
                i=str(key_stroke).split("'")[1]+input()
                t.escribir(i)
                break

cambio = ""
while True:
    #se llama a la función "abrir" del modulo texto.py
    t.abrir()
    #llamado a la función que modifica el archivo
    func()

