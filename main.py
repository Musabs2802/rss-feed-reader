import requests
from bs4 import BeautifulSoup
import sys


class RSSReader:
    def __init__(self, url: str) -> None:
        self.page = requests.get(url)
        self.__extract()

    def __extract(self):
        soup = BeautifulSoup(self.page.content, "xml")

        if not soup.find("channel"):
            return

        channel = soup.channel

        if not channel.find("title"):
            return

        print("Page Title:", channel.title.text)
        print("Description: ", channel.description.text)
        print("Link: ", channel.link.text)
        print("-" * 100)
        print()

        items = soup.find_all("item")
        for id, item in enumerate(items):
            print("{}. Title:".format(id + 1), item.title.text)
            if item.description:
                print("Description: ", item.description.text)
            print("link: ", item.link.text)
            print()


if __name__ == "__main__":
    args = sys.argv
    urls = args[1:]

    for url in urls:
        RSSReader(url)
