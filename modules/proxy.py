import random, fake_useragent
from typing import List
from settings import settings
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import seleniumwire.undetected_chromedriver as uc

def get_connect_with_random_proxy() -> webdriver.Chrome:
    options: Options = Options()
    options.add_argument("--log-level=3") 
    options.add_argument(f'user-agent={fake_useragent.UserAgent().random}')

    proxylist: List[str] = open(settings.config['proxy_file'], 'r').read().splitlines()
    proxy: str = random.choice(proxylist)

    proxy_parts: List[str] = proxy.split(':')
    proxy_address: str = proxy_parts[0]
    proxy_port: int = int(proxy_parts[1])
    proxy_username: str = proxy_parts[2]
    proxy_password: str = proxy_parts[3]

    proxy_options = {
        'proxy': {
            'http': f'http://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}',
            'https': f'https://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}',
            'no_proxy': None,
        }
    }

    driver: webdriver.Chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options, seleniumwire_options = proxy_options)
    return driver