from pyfav import get_favicon_url
from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor
import re
import rank_provider
import requests
import seolib
from bs4 import BeautifulSoup
from rank_provider import RankProvider
# favicon_url = get_favicon_url('http://admissions.iisc.ac.in')
# print(favicon_url)
import whois
import phishtank
from pyphishtank import phishtank

archive_url = "http://www.pythonforbeginners.com/error-handling/exception-handling-in-python"

site = 'https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')
anchor_tags = soup.find_all('a')
meta_tags = soup.find_all('meta')
scripts_tags = soup.find_all('script')
link_tags = soup.find_all('link')
link_onmouseover = soup.find_all('onmouseover')
link_mailto = soup.find_all('mailto')
link_mail = soup.find_all('mail')
link_disable = soup.find_all('event.button==2')
link_prompt = []
for wrapper in soup.find_all('script'):
    link_prompt.append(wrapper.text)
img_url = [img['src'] for img in img_tags]
a_url = [img['href'] for img in anchor_tags]
print (img_tags)
print(a_url)
print(link_tags)
print (scripts_tags)
print (meta_tags)

response = requests.get(site)
if response.history:
    print "Request was redirected"
    for resp in response.history:
        print resp.status_code, resp.url
    print "Final destination:"
    print response.status_code, response.url
else:
    print "Request was not redirected"

w = whois.whois(site)
print w
# function writetostatus(input){
#    window.status=input
#   return true

print link_onmouseover
print link_mail
print link_mailto
print link_disable
# print(link_prompt)
# r = re.compile(".*prompt")
# newlist = filter(r.match, link_prompt)
# r = re.compile(".*event.button==2")
# newlist2 = filter(r.match, link_prompt)
# print newlist
# print newlist2
newlist = []
str1 = ''.join(link_prompt)
parser = Parser()
pattern = r'prompt\("(.*?)"\)'
newlist.append(re.search(pattern, str1).group(1))
print newlist
seo = seolib
alexa_rank = seo.get_alexa(site)
print(alexa_rank)
api = phishtank.PhishTank()
print(api.check('http://alices-dagbog.dk/images/online.php').unsafe)
