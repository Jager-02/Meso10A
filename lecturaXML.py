import xml.etree.ElementTree as ET

#Se define la ruta del archivo XML
ruta = "10o A\clases.xml"

#Se crea un objeto de tipo ElementTree
arbol = ET.parse(ruta)

#Se obtiene el elemento raiz del archivo
raiz = arbol.getroot()

#Se accede al archivo y se recorre con un ciclo for
for clase in raiz.findall("clase"):
    identi = clase.find("identi").text
    nombre = clase.find("nombre").text
    profesor = clase.find("profesor").text
    punteo = clase.find("punteo").text
    creditos = clase.find("creditos")

    #Se imprime la información almacenada en las variables
    print(f"id : {identi} - Clase: {nombre} - Profesor: {profesor} - Punteo: {punteo} - Creditos: {creditos}")