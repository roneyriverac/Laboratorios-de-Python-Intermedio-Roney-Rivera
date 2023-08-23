import requests as req
import json

moviedb_api_key = "ec4cd91ff39ba4625d4f544d9ce71ab1"
movie_response = req.get(f"https://api.themoviedb.org/3/movie/62?api_key={moviedb_api_key}")
movie_response2 = req.get(f"https://api.themoviedb.org/3/movie/63?api_key={moviedb_api_key}")
movie_response3 = req.get(f"https://api.themoviedb.org/3/movie/64?api_key={moviedb_api_key}")
movie_response4 = req.get(f"https://api.themoviedb.org/3/movie/65?api_key={moviedb_api_key}")
movie_response5 = req.get(f"https://api.themoviedb.org/3/movie/66?api_key={moviedb_api_key}")
movie_response6 = req.get(f"https://api.themoviedb.org/3/movie/67?api_key={moviedb_api_key}")
movie_response7 = req.get(f"https://api.themoviedb.org/3/movie/68?api_key={moviedb_api_key}")
movie_response8 = req.get(f"https://api.themoviedb.org/3/movie/69?api_key={moviedb_api_key}")
movie_response9 = req.get(f"https://api.themoviedb.org/3/movie/70?api_key={moviedb_api_key}")

#print(movie_response.status_code)
#print(movie_response.text)
#print(type(movie_response.text))
movie_json = json.loads(movie_response.text)
movie_json2 = json.loads(movie_response2.text)
movie_json3 = json.loads(movie_response3.text)
movie_json4 = json.loads(movie_response4.text)
movie_json5 = json.loads(movie_response5.text)
movie_json6 = json.loads(movie_response6.text)
movie_json7 = json.loads(movie_response7.text)
movie_json8 = json.loads(movie_response8.text)
movie_json9 = json.loads(movie_response8.text)
lista = [];
lista1 = [];
lista2 = [];
lista3 = [];
lista4 = [];

for key, value in movie_json.items():
    #print(key, ':', value)
    lista.append(key)
    
    if key == "title" or key == "release_date" or key == "vote_average":
        lista1.append(key)
    if key == "title":
        lista2.append(value)
    if key == "release_date":
        lista3.append(value)

    if key == "vote_average":
        lista4.append(value)

        
for key, value in movie_json2.items():
    #print(key, ':', value)
    
   
    if key == "title":
        lista2.append(value)
    if key == "release_date":
        lista3.append(value)

    if key == "vote_average":
        lista4.append(value)

for key, value in movie_json3.items():
    #print(key, ':', value)
    
    
    if key == "title":
        lista2.append(value)
    if key == "release_date":
        lista3.append(value)

    if key == "vote_average":
        lista4.append(value)

        
for key, value in movie_json4.items():
    #print(key, ':', value)
    
    
        
    if key == "title":
        lista2.append(value)
    if key == "release_date":
        lista3.append(value)

    if key == "vote_average":
        lista4.append(value)

for key, value in movie_json5.items():
    #print(key, ':', value)
    
    
        
    if key == "title":
        lista2.append(value)
    if key == "release_date":
        lista3.append(value)

    if key == "vote_average":
        lista4.append(value)

        
for key, value in movie_json6.items():
    #print(key, ':', value)
    
    
    if key == "title":
        lista2.append(value)
    if key == "release_date":
        lista3.append(value)

    if key == "vote_average":
        lista4.append(value)

for key, value in movie_json7.items():
    #print(key, ':', value)
    
    
    if key == "title":
        lista2.append(value)
    if key == "release_date":
        lista3.append(value)

    if key == "vote_average":
        lista4.append(value)

        
for key, value in movie_json8.items():
    #print(key, ':', value)
   
    
      
    if key == "title":
        lista2.append(value)
    if key == "release_date":
        lista3.append(value)

    if key == "vote_average":
        lista4.append(value)
        
for key, value in movie_json9.items():
    #print(key, ':', value)
   
    
    if key == "title":
        lista2.append(value)
    if key == "release_date":
        lista3.append(value)

    if key == "vote_average":
        lista4.append(value)



        
#print(movie_json)
print("-----------------------------------------------------------------------------")
print("Nombres de todas columnas",lista)
print("-----------------------------------------------------------------------------")

print("-----------------------------------------------------------------------------")

print("Nombres de columnas",lista1)
print("Valor de titulo",lista2)
print("Valor de fecha",lista3)
print("Valor de calificación",lista4)

moviedb_base_url = 'https://api.themoviedb.org/3'


    


