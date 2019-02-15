diccionario = {1: 'Hola', 
               2:"Mundo", 
               3:"desde", 
               "cuatro": "diccionario"}

print(type(diccionario))

print(diccionario["cuatro"])

for keys, value in diccionario.items():
    print(f"""llave{keys}:valor-{value}""")

persona = {}

persona["nombre"]= "Leo"
persona["apellido"]= "García"
persona["edad"]= 21

for datos, value in persona.items():
    print(f"""{datos}-{value}""")

persona["correo"]= "leogarcia@alv.com"

if "correo" in persona:
    print(f"""el correo es {persona["correo"]}""")
else:
    print("no tiene correo")


if persona.get("altura")== None:
    persona["altura"]= "1.76mts"

print(persona.get("altura"))