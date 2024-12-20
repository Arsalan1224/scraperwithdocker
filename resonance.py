# This code will scrap product URLs from resonance link and give product URLs
# Working good

from requests_html import HTMLSession
import json

# Initialize the session
session = HTMLSession()

# The provided API URL
api_url = "https://www.res-x.com/ws/r2/Resonance.aspx?appid=autozone02&tk=114282261620256&pg=res24120916839749690816461&sg=1&ev=product&ei=232746&bx=true&sc=pla2_rr&sc=partproduct2_rr&sc=product5_rr&sc=product6_rr&no=20&Category1=Battery&parttype=00175&ccb=certonaRecommendations&vr=5.12x&url=https%3A%2F%2Fwww.autozone.com%2Fbatteries-starting-and-charging%2Fbattery%2Fp%2Fduralast-gold-battery-bci-group-size-75-700-cca-75-dlg%2F232746_0_0&ref=https%3A%2F%2Fwww.google.com%2F"

# Send GET request to the API
response = session.get(api_url)

# Check if request was successful
if response.status_code == 200:
    try:
        # Parse JSON response (strip the callback function wrapper)
        response_json = response.text[response.text.find('(')+1 : response.text.rfind(')')]
        data = json.loads(response_json)

        # Use a set to store unique product URLs
        product_urls = set()

        # Loop through the 'schemes' and 'items' in the response structure
        for scheme in data.get('resonance', {}).get('schemes', []):
            for item in scheme.get('items', []):
                product_url = item.get('product_url')
                if product_url:
                    product_urls.add(product_url)  # Using a set to ensure uniqueness

        # Display the product URLs
        if product_urls:
            print("Unique Product URLs:")
            for url in product_urls:
                print(url)
        else:
            print("No product URLs found.")
    
    except Exception as e:
        print(f"Error parsing response: {e}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")