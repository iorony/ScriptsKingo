def goto():
    import os
    devices = os.popen('adb devices ');
    count=0
    intent=0
    i=0
    print ("------------MENU-----------")
    print ("(1)  Personal Huawei")
    print ("(2)  Tendero")
    print ("(3)  Apps de ROOT")
    print ("(4)  Personal Samsung")
    print ("(6)  Bmobile")
    input_var = input("\nIngrese opcion: ")
    if (input_var=='1'):
        path = 'C:/AppCorp/'
    elif(input_var=='2'):
        path = 'C:/AppTend/'
    elif (input_var=='4'):
        path = 'C:/AppCorp2/'
    elif(input_var=='6'):
        path = 'C:/Bmobile/'
    elif(input_var=='3'):
        path = 'ROOT'
        print("\n(1)  KINGO ROOT")
        print("(2)  KINGROOT")
        print("(3)  ROOT360")
        print("(4)  iROOT")
        print("(5)  TowelROOT")
        print("(6)  FramaRoot")
        input_var = input("\nIngrese opcion: ")
    else:
        input("Ingrese opcion valida!")
        os.system("cls")
        goto()
    devices = os.popen('adb devices ');
    listDevices = devices.read().replace('\n',',').replace('\t',',').split(',')
    for device in listDevices:
        i=i+1
        lstDir = os.walk(path)
        if (device!="" and device!="List of devices attached" and device!= "device"  and  device!="unauthorized" and device!= "adb server is out of date.  killing..." and device!="* daemon started successfully *"):
                count = count+1
                print ('Seleccionando dispositivo', device)
                if(path=='C:/AppCorp/' or path=='C:/AppCorp2/'):
                    print ("(1)  bloqueo para AT")
                    print ("(2)  bloqueo para CS")
                    input_var = input("\nIngrese opcion: ")
                    if (input_var=='1'):
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.android.chrome")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.sec.android.app.sbrowser")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.browser")
                    elif (input_var=='2'):
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.android.chrome")
                    elif(input_var=='3'):
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.apps.docs.editors.sheets ")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.bluetooth")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.providers.calendar")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.browser")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.providers.downloads.ui")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.mms")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.googlequicksearchbox")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.exchange")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.backuptransport")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.apps.docs")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.providers.downloads")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.sec.android.app.easylauncher")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.videos")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.onetimeinitializer")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.stk")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.configupdater")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.sec.android.app.samsungapps")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.providers.contacts")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.kingoapp.apk")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.apps.plus")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.vending ")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.apps.magazines")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.keyguard")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.syncadapters.contacts    ")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.contacts")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.calendar")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.marvin.talkback")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.sec.android.app.launcher")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.music")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.sec.android.emergencylauncher")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.tts")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.email")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.apps.books")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.sec.android.app.camera")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.feedback")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.talk	")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.whatsapp")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.syncadapters.calendar")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.play.games")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.youtube")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.chrome")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.chrome")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.sec.android.app.sbrowser")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.browser")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "deezer.adnroid.app")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.play.games")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.google.android.music")
                        os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ "com.android.browser")
                        
                    else:
                        input("Que Configuras?")
                        os.system("cls")
                        goto()
                    os.popen("adb -s " + device + " uninstall com.kingo.shopkeeper")
                    os.popen("adb -s " + device + " uninstall com.example.ulices.passwo")
                    os.popen("adb -s " + device + " uninstall com.babyturtleapps.device.lock")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.ppswipe.blurewards")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.android.vending")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.facebook.orca")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.facebook.katana")                
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.google.android.youtube")                    
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.sec.android.app.camera")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.luckydeveloper.apkshare")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.android.chrome")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.google.android.googlequicksearchbox")
                    for root, dirs, files in lstDir:
                        for fichero in files:
                            (nombreFichero, extension) = os.path.splitext(fichero)
                            if(extension == ".apk"):
                                print ('Instalando ', nombreFichero + extension)
                                apk='adb -s ' + device + ' install -r ' + '"' + path + nombreFichero + extension + '"'
                                install=os.popen(apk)
                                apkSuccess=install.read().split('\n\n')
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.android.launcher3")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.huawei.android.launcher")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.motorola.launcher3")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.sec.android.app.launcher")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.sec.android.app.easylauncher")
                if(path == 'C:/Bmobile/'or path=='C:/AppTend/' ):
                    os.popen("adb -s " + device + " uninstall com.kingo.shopkeeper")
                    os.popen("adb -s " + device + " uninstall com.example.ulices.passwo")
                    os.popen("adb -s " + device + " uninstall com.babyturtleapps.device.lock")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.android.chrome")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.google.android.apps.photos")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.google.android.music")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.google.android.videos")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.google.android.youtube")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.android.vending")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.google.android.apps.docs")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.google.android.gm")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.google.android.googlequicksearchbox")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.google.android.apps.tachyon")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.android.fmradio")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.google.android.apps.maps")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.android.dialer")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.mediatek.camera")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.android.vending")
                    for root, dirs, files in lstDir:
                        for fichero in files:
                            (nombreFichero, extension) = os.path.splitext(fichero)
                            if(extension == ".apk"):
                                print ('Instalando ', nombreFichero + extension)
                                apk='adb -s ' + device + ' install -r ' + '"' + path + nombreFichero + extension + '"'
                                install=os.popen(apk)
                                apkSuccess=install.read().split('\n\n')
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.android.launcher3")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.huawei.android.launcher")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.motorola.launcher3")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.sec.android.app.launcher")
                    os.popen('adb -s '+ device +' shell pm uninstall -k --user 0 '+ " com.sec.android.app.easylauncher")
                if(path == 'ROOT'):
                    if (input_var=='1'):
                        print("install KINGO ROOT")
                        in1="adb -s " + device + " install -r C:\Roots\KingoRoot.apk"
                        install=os.popen(in1)
                    elif(input_var=='2'):
                        print("install KINGROOT")
                        in2="adb -s " + device + " install -r C:\Roots\KingrootV503.apk"
                        install=os.popen(in2)
                    elif(input_var=='3'):
                        print("install ROOT360")
                        in3="adb -s " + device + " install -r C:\Roots\sroot360.apk"
                        install=os.popen(in3)
                    elif(input_var=='4'):
                        print("install iROOT")
                        in4="adb -s " + device + " install -r C:\Roots\RomasterSu.apk"
                        install=os.popen(in4)
                    elif(input_var=='5'):
                        print("install TowelROOT")
                        in5="adb -s " + device + " install -r C:\Roots\SUr.apk"
                        install=os.popen(in5)
                    elif(input_var=='6'):
                        print("install Framaroot")
                        in5="adb -s " + device + " install -r C:\Roots\\ramaroot.apk"
                        install=os.popen(in5)
                    else:
                        input("Ingrese opción valida!")
                        os.system("cls")
                        goto()
                    apkSuccess=install.read().split('\n\n')
        else:
            intent = intent+1
    if (intent!=0 and count==0):
            input('\nNo hay dispositivos para instalar')
            os.system("cls")
            goto();
    input('\nListo')
    os.system("cls")
    goto();
goto()
