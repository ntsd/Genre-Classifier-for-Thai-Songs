"""this is for grab song title, artist, genre,album """
from lxml import html
import requests
from models.Song import Song
import csv


def grabSongsDetailFromPage(url):
    print("requests:"+url)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    textContacts = tree.xpath('//div[@class="textcontact-music"]')
    songs = []
    for detail in textContacts:
        title, artist, album, record, category, genre = "", "", "", "", "", ""
        for a in detail:
            href = a.get("href")
            if href is not None and ".html" in href:
                if "artist" in href:
                    artist = a.text
                elif "album" in href:
                    album = a.text
                elif "recording" in href:
                    record = a.text
                elif "category" in href:
                    category = a.text
                elif "genre" in href:
                    genre = a.text
                else:
                    title = a.text
        songs.append(Song(title, artist, album, record, category, genre))
    return songs

if __name__ == "__main__":
    with open("songsList.csv", 'w', newline='', encoding='utf-8') as csv_file:
        wr = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        songs = []
        # songs = grabSongsDetailFromPage("https://musicstation.kapook.com/genre.html?v=%E0%B8%A5%E0%B8%B9%E0%B8%81%E0%B8%97%E0%B8%B8%E0%B9%88%E0%B8%87-%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%8A%E0%B8%B5%E0%B8%A7%E0%B8%B4%E0%B8%95&page=1")
        # print(songs)
        for page in range(1,109):
            songs += grabSongsDetailFromPage("https://musicstation.kapook.com/genre.html?v=%E0%B8%A5%E0%B8%B9%E0%B8%81%E0%B8%97%E0%B8%B8%E0%B9%88%E0%B8%87-%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%8A%E0%B8%B5%E0%B8%A7%E0%B8%B4%E0%B8%95&page="+page.__str__())
        for page in range(1,386):
            songs += grabSongsDetailFromPage("https://musicstation.kapook.com/genre.html?v=%E0%B9%84%E0%B8%97%E0%B8%A2&page="+page.__str__())
        for cdr in songs:
            wr.writerow(cdr.getDetailCSV())
