from bs4 import BeautifulSoup
import requests


def _get_data_from_web(address="https://www.enamad.ir/DomainListForMIMT", isFile=False):
    """Get data from web page and return it."""
    if isFile:
        with open(address, "r") as f:
            html = f.read()
    else:
        html = requests.get(address).text
    soup = BeautifulSoup(html, "html.parser")

    div_content = soup.find("div", id="Div_Content")
    return div_content


def _get_data():
    """Get data from web page and return it."""
    text = []
    data = _get_data_from_web()
    for div in data.find_all("div", class_="row"):
        text.append(div.text)
    return text


def sort_data():
    """Sort data and return it."""
    work_info: dict = {}
    for i in _get_data():
        if i == " ":
            continue
        if int(i.split()[0]) < 11:
            work_info[i.split()[0]] = i.split()
            work_info[i.split()[0]].pop()
            work_info[i.split()[0]].pop()
            if len(work_info[i.split()[0]]) > 5:
                for _ in range(len(work_info[i.split()[0]]) - 5):
                    work_info[i.split()[0]][2] += " " + work_info[i.split()[0]][3]
                    work_info[i.split()[0]].pop(3)
    return work_info
