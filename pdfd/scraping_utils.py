import requests
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib3.exceptions import InsecureRequestWarning
from pdfd.models import notices
# Create your views here.
urllib3.disable_warnings(InsecureRequestWarning)



def download_pdf(website_url):
    response = requests.get(website_url,verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    target_ul_element = soup.find_all('ul')[14]
    links = target_ul_element.find_all('a', href=True)
    for link in links:
        if "B.Sc.CSIT" in link.text:
            titles=link.text
            existing_notice = notices.objects.filter(title=titles).exists()
            if existing_notice:
                pass
            else:
                urls = urljoin(website_url, link['href'])
                r = requests.get(urls,verify=False)
                soups = BeautifulSoup(r.content, 'html.parser')
                tds=soups.find_all('table')[0]
                linkd = tds.find_all('a', href=True)
                for li in linkd:
                    absolute_url = urljoin(website_url, li['href'])
                    if absolute_url.endswith('.pdf'):
                        pdf_resp=requests.get(absolute_url,verify=False)
                        download_pdf=notices(title=titles,pdf_content=pdf_resp.content)
                        download_pdf.save()
