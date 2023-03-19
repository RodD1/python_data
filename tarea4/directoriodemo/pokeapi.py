import requests
url='https://pokeapi.co/api/v2/pokemon/'

data=requests.get(url).json()

#listPokemon=data['pokemon_entries']

#for i,value in enumerate(listPokemon):
#    name=value['pokemon_species']['name']
#    print(i,"=)",name)

url="https://pokeapi.co/api/v2/pokemon/"


msg="""
    1)listar pokemons
    2)buscar pokemon
    
    3)salir
"""

while(True):
    print(msg)
    opcion=float(input("ingrese una opcion"))
    listaPokemon=data['results']
    if opcion==1:
            for i,value in enumerate(listaPokemon):
                name=value['name']
                print(i+1,"=)",name)
            pass
    if opcion==2:
                
                namePoke=input("que pokemon desea buscar?: ")
                for i,value in enumerate(listaPokemon):
                    urlImg="https://pokeapi.co/api/v2/pokemon/",i,"/"
                    dataimg=requests.get(urlImg).json()
                    listaPokemonimg=dataimg['sprites']['front_default']
                    name=value['name']
                    urlpoke=value['url']
                    if namePoke==name:
                        print(i+1,"=)",name)
                        print(urlpoke)
                    result=input("deseas ver el url de la imagen del pokemon? (S=1,N=0)")
                    if result==1:
                          print(dataimg)
                    if result==1:
                          print("saliendo")
                    else:
                          print("no se encontro el pokemon")
                    break
  
    if opcion==3:
        pass
        print("gracias hasta luego")
        break