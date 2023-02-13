import requests
from bs4 import BeautifulSoup
import inflection

# Response Object
r = requests.get('http://www.dailysmarty.com/topics/python')

# BeautifulSoup Object
soup = BeautifulSoup(r.text, 'html.parser')

# Find all links
soup_a = soup.find_all('a')

soup_a_posts = []
lowercase_list = ['a ', 'an ', 'and ', 'as ', 'at ', 'by ', 'for ', 'from ', 'in ', 'into ', 'of ', 'the ', 'to ', 'with ']

def formating(word):
  word = word.split('/')[-1]
  word = ' '.join(word.split('-'))
  word = inflection.titleize(word)
  
  for lowercase in lowercase_list:
    word = word.replace(lowercase.title(), lowercase)
    
  return word


for link in soup_a:
  if link.get('href'):
    if '/posts/' in link.get('href'):
      soup_a_posts.append(formating(link.get('href')))
      print(soup_a_posts[-1])
     