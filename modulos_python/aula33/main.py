from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#Caminho para a pasta raiz do projeto
ROOT_FOLDER = Path(__file__).parent

#Caminho para a pasta onde o chromedriver está
CHROMEDRIVE_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver'


def make_chrome_browser(*optinos: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if optinos is not None:
        for option in optinos:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROMEDRIVE_EXEC)
    )
    browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options,
    )

    return browser

if __name__ == '__main__':
    # options = ('--disable-gpu', '--no--sandbox',)
    options = ()
    browser = make_chrome_browser(*options)

#Como antes
browser.get('https://www.google.com.br/')

#Dorme por 10s
sleep(10)