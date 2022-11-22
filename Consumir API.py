import requests

url="https://api.jikan.moe/v4/top/anime"

#nos devuelve la lista de los 25 animes mas populares y su ranking en la pagina Myanimelist

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for element in data['data']:
        print(str(element['rank'])+ " " + element['title'])
elif response.status_code == 400:
    print("Bad Request")
elif response.status_code == 500:
    print("Internal Server Error")    

