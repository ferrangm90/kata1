personas= {'nombre':'Rosa','edad':30,'ciudad':'Valencia' }
lista_personas=[ {'nombre':'Rosa','edad':30,'ciudad':'Valencia' },
                {'nombre':'Rosa','edad':30,'ciudad':'Valencia' },
                {'nombre':'Rosa','edad':30,'ciudad':'Valencia' },
                {'nombre':'Rosa','edad':30,'ciudad':'Valencia' }]

print(len(personas))
print(personas['nombre'])
print(personas['edad'])
print(personas['ciudad'])

personas['nombre']="Jose"
print(personas['nombre'])
print(personas.keys())#obtengo todas las claves o keys
print(personas.values())#obtengo todos los valores del diccionario
print(personas.items())#obtengo valor y clave
print(personas.get('nombre'))#obtener el valor por su key
print(personas.pop('edad'))#eliminar un elemento por su clave
print(personas)
print(personas.update({'pais':'España'}))#añadir un elemento nuevo
print(personas)

for key,value in personas.items():
    print(f"key: {key}, value: {value}")