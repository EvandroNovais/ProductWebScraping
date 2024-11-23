import requests

url = "https://www.mercadolivre.com.br/apple-iphone-16-128-gb-preto-distribuidor-autorizado/p/MLB1040287808#polycard_client=search-nordic&wid=MLB5054621100&sid=search&searchVariation=MLB1040287808&position=1&search_layout=stack&type=product&tracking_id=a9808f3a-2276-4a1b-b84c-1fcae354d802"

def fetch_page():
    response = requests.get(url) 
    print(response.text)
    
if __name__ == "__main__":
    new_url = url
    page_content = fetch_page(url)
    print(page_content)