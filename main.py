from bs4 import BeautifulSoup
import requests
import codecs

# getting the website html code
response = requests.get("https://web.archive.org/web/20200518073855/https:"
                        "//www.empireonline.com/movies/features/best-movies-2/")
empire_movies = response.text

# preparing the soup
soup = BeautifulSoup(empire_movies, "html.parser")

# getting hold of the movies list
titles = soup.find_all(name="h3", class_="title")
movies_titles_list = []
for title in titles:
    movie_title = title.string
    try:
        un_numbered_title = movie_title.split(") ")[1]

    except IndexError:
        corrected_title = movie_title.replace(": ", ") ")
        un_numbered_title = corrected_title.split(") ")[1]

    movies_titles_list.insert(0, un_numbered_title)


# writing the top 100 movies to a file function
def write_top_100_movies():
    with open("top_100_movies.txt", mode="w", encoding='ISO-8859-1') as top_100_movies_file:
        for _ in range(len(movies_titles_list)):
            top_100_movies_file.write(f"{_ + 1}) {movies_titles_list[_]}\n")


write_top_100_movies()
