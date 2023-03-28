from bs4 import BeautifulSoup
import requests


response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text, "html.parser")

soup = soup.find_all(name='h3', class_='title')
movies = [movie.text for movie in soup]
movies = movies[::-1]

with open("movie_top.txt", "a") as file:
    for movie in movies:
        file.write(f"{movie}\n")

