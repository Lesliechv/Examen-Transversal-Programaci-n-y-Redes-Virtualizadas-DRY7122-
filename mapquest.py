import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "ycrmGMKE97Lv1OZa5auJ1lwKaoDG8DzS"

def obtener_tipo_transporte():
    while True:
        print("\nSelecciona el tipo de transporte:")
        print("1. Automóvil")
        print("2. Caminar")
        print("3. Bicicleta")
        print("4. Tránsito Público")
        opcion = input("Ingresa el número correspondiente al tipo de transporte (1-4): ")
        
        if opcion == "1":
            return "fastest"
        elif opcion == "2":
            return "pedestrian"
        elif opcion == "3":
            return "bicycle"
        elif opcion == "4":
            return "multimodal"
        else:
            print("Opción no válida. Por favor, selecciona nuevamente.")

while True:
   orig = input("Ciudad de origen: ")
   if orig == "s":
        break
   dest = input("Ciudad de destino: ")
   if orig == "s":
        break

   tipo_transporte = obtener_tipo_transporte()

   url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "routeType":tipo_transporte, "locale":"es_ES"})
   print("url: " + (url))

   json_data = requests.get(url).json()
   json_status = json_data ["info"] ["statuscode"]

   if json_status == 0:
    print("API Status: " + str(json_status) + " = Una llamada de ruta exitosa.\n ") 
    print("=============================================")
    print("Desde " + (orig) + " a " + (dest))
    print("Duracion de viaje: " + (json_data["route"]["formattedTime"]))
    print("Kilometros:" + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
    print ("Millas:" + str (json_data ["route"] ["distance"]))
    print("Combustible (Ltr):" + str("{:.2f}".format((json_data["route"]["distance"])*3.78)))
    print("=============================================")
    print("Narrativa del viaje:")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + "km"))
    print("=============================================\n")
