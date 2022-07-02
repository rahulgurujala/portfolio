import requests
from lxml import html
import os


class Pdf:
    def __init__(self, usr_inpt) -> None:
        self.usr_inpt = usr_inpt
        self.links = []

    def pdf(self):

        query = "+".join(self.usr_inpt.split())

        url = f"https://www.google.com/search?q=%22{query}%22+filetype%3Apdf"

        response = requests.get(url)

        source = html.fromstring(response.text)
        self.links = source.xpath('//div[@id="main"]/div/div/div/a/@href')
        self.links = [
            link.replace("/url?q=", "")
            for link in self.links
            if link.startswith("/url?q=")
        ]
        self.links = [link.split("&")[0] for link in self.links]
        filename = [
            url.split("/")[-1] if url.endswith(".pdf") else url.split("/")[-1] + ".pdf"
            for url in self.links
        ]

        return self.links, filename, len(self.links)

    # return made  samjl
    def download(self):
        if not os.path.exists("pdf"):
            os.mkdir("pdf")
        print("Pdf is downloading")
        for url in self.links:
            try:
                response = requests.get(url)
                filename = (
                    url.split("/")[-1]
                    if url.endswith(".pdf")
                    else url.split("/")[-1] + ".pdf"
                )
                print(f"{filename} is downloading...")
                try:
                    with open(f"pdf/{filename}", "wb") as f:
                        f.write(response.content)
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
        print("All Done.")


if __name__ == "__main__":
    usr_inpt = input("Enter title for pdf book: ")
    data = Pdf(usr_inpt)
    data = data.pdf()
    print(data)
    # print(data)
    # data.download()
    for index in range(len(data[0])):
        print(data[0][index], data[1][index])
# print(pdf(usr_inpt))
# numbers = [1, 2, 3]
# letters = ["A", "B", "C"]

# for index in range(len(numbers)):
#     print(numbers[index], letters[index]) define kar manualy len tuja zinj la fek
