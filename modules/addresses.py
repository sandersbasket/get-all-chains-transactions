import time
from typing import List
from lxml import html
from modules import files, proxy
from settings import settings 


def get_transactions(address: str) -> None:
    driver = proxy.get_connect_with_random_proxy()

    driver.get(f'https://debank.com/profile/{address}/history')
    time.sleep(settings.config["sleep"])

    tree: html.HtmlElement = html.fromstring(driver.page_source)
    elements: List[html.HtmlElement] = tree.xpath('/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/*')

    transactions: int = 0 
    
    if elements is None: 
        return 
    
    for element in elements:
        class_name: str = element.get('class')
        if class_name is None: 
            return 
        
        if class_name.startswith("History_tableLine"): 
            transactions += 1
    
    if transactions >= 1: 
        return files.save_address_to_file(address, settings.config["out"])