def conf():
    import os
    import sys
    count=0
    intent=0
    i=0

    print ("1. Congelar")
    print ("2. Descongelar")
    print ("3. Paquetes Congelados")
    print ("4. Paquetes Habilitados")
    print ("5. Eliminar Apps")
    input_var = input("Ingrese opcion: ")
    path='C:/Users/KG/Desktop/t.txt'
    devices = os.popen('adb devices ');
    listDevices = devices.read().replace('\n',',').replace('\t',',').split(',')
    listDevices
    for device in listDevices:
        i=i+1
        if (device!='' and device!='List of devices attached' and device!= 'device'  and  device!='unauthorized' and device!= 'adb server is out of date.  killing...' and device!='* daemon started successfully *'):
            count = count+1
            if (input_var=='1'):
                print ('\n','Dispositivo selecionado:', device,'\n')
                print()
                com = open(path, "r+")
                pack = com.read(1);
                for pack in com :
                    os.system('adb -s '+ '"' + device + '"' + ' shell su -c pm disable '+ '"' + pack +'\n')
                os.system('adb -s '+ '"' + device + '"' + ' shell su -c pm enable com.android.phone '+'\n')
                print("EXITO!")

            elif (input_var=='2'):
                print ('\n','Dispositivo selecionado:', device,'\n')
                print()
                com = open(path, "r+")
                pack = com.read(1);
                for pack in com :
                    os.system('adb -s '+ '"' + device + '"' + ' shell su -c pm enable '+ '"' + pack +'\n')
                print("EXITO!")

            elif (input_var=='3'):
                print ('\n','Dispositivo selecionado:', device,'\n')
                freez = os.system('adb -s '+ '"' + device + '"' + ' shell pm list packages -d '+'\n')

            elif (input_var=='4'):
                print ('\n','Dispositivo selecionado:', device,'\n')
                freez = os.system('adb -s '+ '"' + device + '"' + ' shell pm list packages -e '+'\n')

            elif (input_var=='5'):
                print ('\n','Dispositivo selecionado:', device,'\n')
                print()
                com = open(path, "r+")
                pack = com.read(1);
                for pack in com :
                    os.system('adb -s '+ device +' shell pm uninstall -k --user 0 '+ pack +'\n')
                print("EXITO!")

            else:
                input("Ingrese opción valida!")
                os.system("cls")
                conf()
        else:
            intent = intent+1
        devices = os.popen('adb devices ');
        listDevices = devices.read().replace('\n',',').replace('\t',',').split(',')
        listDevices

    if (intent!=0 and count==0):
        print("")
        input("No hay dispositivo para instalar")
        os.system("cls")
        conf()
    print("")
    input("SALIR!")
    os.system("cls")
    conf()
    return
conf()
