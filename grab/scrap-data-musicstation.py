"""this is for grab song title, artist, genre,album """
from lxml import html
import requests
from models.Song import Song
import csv


def grabSongsDetailFromPage(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    textContacts = tree.xpath('//div[@class="textcontact-music"]')
    songs = []
    for detail in textContacts:
        title = detail[0].text
        artist = detail[2].text
        album = detail[4].text
        record = detail[6].text
        emotion = detail[8].text
        genre = detail[10].text
        songs.append(Song(title, artist, album, record, emotion, genre))
    return songs

if __name__ == "__main__":
    songs = grabSongsDetailFromPage("https://musicstation.kapook.com/genre.html?v=%E0%B8%A5%E0%B8%B9%E0%B8%81%E0%B8%97%E0%B8%B8%E0%B9%88%E0%B8%87-%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%8A%E0%B8%B5%E0%B8%A7%E0%B8%B4%E0%B8%95&page=108")
    print(len(songs))
    with open("songsList.csv", 'w', newline='', encoding='utf-8') as csv_file:
        wr = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for cdr in songs:
            wr.writerow(cdr.getDetailCSV())
