# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get("https://news.ycombinator.com/")
# your_page = response.text
# # print(your_page)
#
# soup= BeautifulSoup(your_page, "html.parser")
# s = soup.find(name="span", class_="titleline")
# a= s.get_text()
# b=s.get("href")
#
# print(b)
# # print(s)
#
#
# from bs4 import BeautifulSoup
#
# with open("website.html", encoding="utf-8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# loop = soup.find(name="h3", class_="heading" )
# print(loop)
# for item in loop:
#     print(item.get("href"))


# challenge project
from bs4 import BeautifulSoup
import requests
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
your_page = response.text
soup = BeautifulSoup(your_page, "html.parser")
print("the top 100 film on the world")
new_title = soup.find_all(name="h3")

for film in reversed (new_title) :
    list_of_movies = film.get_text()


with open("list_of_movies.text",mode="w", encoding="utf-8") as file:
    for film in reversed(new_title):
        list_of_movies = film.get_text()

        file.write(f"{list_of_movies}\n")

#
#








#





# from soup import BeautifulSoup
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup= BeautifulSoup(contents, "html.parser")
# all = soup.find(name="h3" , class_="heading" )
# print(all)