import requests
from bs4 import BeautifulSoup


def fakeWebsite(urlFiki, string_to_replace, string_to_use):
    source = requests.get(f'{urlFiki}')
    fiki = BeautifulSoup(source.text, 'lxml')
    mixed_soup = fiki.strings
    for string in mixed_soup:
        if string == string_to_replace:
            string.replace_with(string_to_use)
        else:
            pass
    return fiki

def main():
    print(fakeWebsite("ENTER_YOUR_URL_AS_A_STRING_HERE", "some text to find", "replacement text !!!!!!!!!!!fuckyeah!!!!!!!!!!!!!!!!!"))

if __name__=="__main__":
    main()

