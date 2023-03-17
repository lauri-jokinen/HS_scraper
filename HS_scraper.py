import requests
from datetime import datetime

def paper_ID():
    # Finds paper ID from the regular HS-website
    # Here, we use today's paper
    today_string = datetime.today().strftime('%d%m%Y')
    paper_today_url = "https://www.hs.fi/paivanlehti/{}/".format(today_string) 
    paper_today_html = str(requests.get(paper_today_url).content)
    
    # Fetch a 'nodeID' from the HTML code (this is magic)
    return paper_today_html.split('nodeID":')[1].split(',')[0].split('}')[0]     # returns, e.g., '3601'
  
def paper_contents():
    # Uses hidden API to fetch the paper's contents
    ID = paper_ID()
    paper_contents_hidden_api_url = "https://www.hs.fi/api/editions/{}/toc".format(ID)
    return requests.get(paper_contents_hidden_api_url).json()

print(paper_contents())
