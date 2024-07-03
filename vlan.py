vlan = int (input("Ingrese numero de vlan: "))
if vlan >= 1 and vlan <= 1005:
    print("Corresponde a vlan de rango normal.") 
elif vlan >= 1006 and vlan <= 4094:
    print("Corresponde a vlan de rango extendido.")