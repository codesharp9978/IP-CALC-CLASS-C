import os
import time
import sys

print("  _____ _____     _____          _      _____")
print(" |_   _|  __ \   / ____|   /\   | |    / ____|")
print("   | | | |__) | | |       /  \  | |   | |    ")
print("   | | |  ___/  | |      / /\ \ | |   | |     ")
print("  _| |_| |      | |____ / ____ \| |___| |____ ")
print(" |_____|_|       \_____/_/    \_|______\_____|")
print("\n")
def autoketik(x): 
    for y in x + "\n":
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(0.030)
print("IPCALC FOR CLASS C")
print("From Telejoker\n")

command = ""

while command != "exit":
    #input ip dan cari optep3
    command = input("Enter IP Address (Exp : 192.168.1.1): ")
    optep3 = command.split(".")
    ambiloptep3 = optep3[3]
    
    #cari SubnetMask
    command = input("Enter Netmask : ")
    prefix = {
        "24" : "0",
        "25" : "128",
        "26" : "192",
        "27" : "224",
        "28" : "240",
        "29" : "248",
        "30" : "252",
        "31" : "254",
        "32" : "255",
    }
    perangka = command.split(" ")
    output = ""
    for i in perangka:
        hasil = prefix.get(i)
        output = f"SubnetMask : {hasil}"
    time.sleep(0.3)
    print(output)

    #mencari hasil pangkat 
    if command == "24":
        result = 32 - 24
        final = 2 ** result
    
    elif command == "25":
        result = 32 - 25
        final = 2 ** result
    
    elif command == "26":
        result = 32 - 26
        final = 2 ** result

    elif command == "27":
        result = 32 - 27
        final = 2 ** result
    
    elif command == "28":
        result = 32 - 28
        final = 2 ** result

    elif command == "29":
        result = 32 - 29
        final = 2 ** result

    elif command == "30":
        result = 32 - 30
        final = 2 ** result

    elif command == "31":
        result = 32 - 31
        final = 2 ** result
    
    elif command == "32":
        result = 32 - 32
        final = 2 ** result
    
    ambiloptep3 = int(ambiloptep3)
    carina = (ambiloptep3 // final) * final
    time.sleep(0.3)
    print(f"Nework : {carina}")

    caribc = carina + final - 1
    time.sleep(0.3)
    print(f"Broadcast : {caribc}")

    carina += 1
    caribc -= 1
    time.sleep(0.3)
    print(f"HostMin : {carina}")
    time.sleep(0.3)
    print(f"HostMax : {caribc}")

    TotalHost = caribc
    time.sleep(0.3)
    print(f"Host For Client : {TotalHost} IP ")
    autoketik("=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>")
    
    time.sleep(0.3)
    tanya = input("Do You Want Calcu Again ? Y/n ")
    if tanya == "Y" or tanya == "y":
        os.system('cls')
        continue
    elif tanya == "N" or tanya == "n":
        time.sleep(0.3)
        print("Thank For Using My Tool")
        print("More Tool : https://github.com/codesharp9978")
        break
    else:
        print("Invalid !!!")
        continue
            