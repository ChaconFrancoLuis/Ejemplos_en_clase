import untangle

archivo = open("respuesta.xml")

respuesta = untangle.parse(archivo)

print(respuesta.services.service[1].name.cdata,respuesta.services.service[1].status.cdata)
#print(respuesta.services.service[0].status.cdata)