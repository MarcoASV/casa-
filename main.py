from gpiozero import LED
from time import sleep
from gpiozero import Button 

luzSala = LED(2)
luzCocina = LED(3)
button_1 = Button(17)
button_2 = Button(27) 
button_3 = Button(22)
motora = LED(10)
motorb = LED(9)
motora.off()
motorb.off()
luzCocina.on()
luzSala.on()

name = input("ingresa tu nombre de usuario: ")
contra = input("sin contraseña no hay pan: ")

def Accion():
    print("1.-prender luces | 2.-leer temperatura | 3.-conversar ")
    sleep (1)
    accion = input("ingrese el numero de la accion que quieres: ")
    if accion == "1":
        print("que luces quieres prender? comedor, cocina, sala: ")
        sleep(1)
        luces = input("ingresa el lugar donde quieres prender las luces: ")
        if luces == "cocina":
            print("luces de la cocina prendidas")
            luzSala.on()
            luzCocina.off()
        elif luces == "comedor":
            print("luces del comedor prendidas")
            luzSala.on()
            luzCocina.on()
        elif luces == "sala":
            print("luces de la sala prendidas")
            luzSala.off()
            luzCocina.on()
        else:
            print("pon una vela pops")
    elif accion == "2":
        print("de donde quieres la temperatura? ")
    elif accion == "3":
        print("presiona el en el panel el numero de la charla")



def validacion(usuario,contrasenia):
    if name == "Marco" and contra == "silvavargas" or name == "Alberto" and contra == "torreslanda":
        print('bienvenido {}'.format(name))
        Accion()
    else:
        print("tas mal")
        
def nohayagua(boton):
        if button_1.is_pressed:
            print("no hay agua")
            motora.on()
            motorb.off()
        else:
            motora.off()
            motorb.off()
            print()


validacion(name,contra)



while True:
    nohayagua(button_1)
    print("hola")
