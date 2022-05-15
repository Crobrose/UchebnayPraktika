import requests
from bs4 import BeautifulSoup as BS
HEADERS = {
    'accept' :'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.3.852 Yowser/2.5 Safari/537.36'
}

def get_HTML():
    r = requests.get("https://coinmarketcap.com", headers=HEADERS)
    return r

def get_content(r):
    html = BS(r.content, 'html.parser')
    items = html.find_all('tr')
    cards = []
    for item in items:
        item1 = item.find_all('p', class_='sc-1eb5slv-0 iworPT')
        for x in item1:
            item3 = item.find_all('span', class_='sc-1ow4cwt-1 ieFnWP')
            for z in item3:
                item2 = item.find_all('div', class_='sc-131di3y-0 cLgOOr')
                for y in item2:
                    cards.append(
                        {
                            'Name' : x.text,
                            'Market_cap' : z.text,
                            'Price' : y.text
                        }
                    )
    return cards

def bubble_sort(cards):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(cards) - 1):
            if cards[i]['Name'] > cards[i + 1]['Name']:
                cards[i], cards[i + 1] = cards[i + 1], cards[i]
                swapped = True
    return cards

def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid]['Name'] == val:
            index = mid
        else:
            if val<lys[mid]['Name']:
                last = mid -1
            else:
                first = mid +1
    return index

def parserCripto():
    r = get_HTML()
    if r.status_code == 200:
        cards = []
        cards = get_content(r)
        bubble_sort(cards)
        for l in range(0,10):
            print(cards[l])
        while True:
            print("Enter Name: ")
            key = input()
            if (key == "Exit"):break
            index = BinarySearch(cards, key)
            print(cards[index])

    else:
        print("Error")
            
parserCripto()