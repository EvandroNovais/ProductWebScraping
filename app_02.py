import requests
from bs4 import BeautifulSoup

def fetch_page():
    url = "https://www.mercadolivre.com.br/apple-iphone-16-128-gb-preto-distribuidor-autorizado/p/MLB1040287808#polycard_client=search-nordic&wid=MLB5054621100&sid=search&searchVariation=MLB1040287808&position=1&search_layout=stack&type=product&tracking_id=a9808f3a-2276-4a1b-b84c-1fcae354d802"
    response = requests.get(url) 
    return response.text
    
def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_='ui-pdp-title').get_text()
    product_prices = soup.find_all('span', class_='andes-money-amount__fraction')
    old_price = product_prices[0].get_text()
    new_price =  product_prices[1].get_text()
    installment_price = product_prices[2].get_text()
    
    return{
        'product_name': product_name,
        'old_price' : old_price,
        'new_price': new_price,
        'installment_price': installment_price
    }
    
if __name__ == "__main__":
    page_content = fetch_page() 
    produto_info = parse_page(page_content)
    print(produto_info)