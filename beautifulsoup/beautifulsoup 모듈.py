from bs4 import BeautifulSoup
import re

html ='''
<html>
  <head>
    <title>BeautifulSoup test</title>
  </head>
  <body>
    <div id='upper' class='test' custom='good'>
      <h3 title='Good Content Title'>Contents Title</h3>
      <p>Test contents</p>
    </div>
    <div id='lower' class='test' custom='nice'>
      <p>Test Test Test 1</p>
      <p>Test Test Test 2</p>
      <p>Test Test Test 3</p>
    </div>
  </body>
</html>'''

soup = BeautifulSoup(html,'html.parser')

print(soup.find('h3'))
print(soup.find('div',class_='test'))

attr = {'id' : 'upper', 'class' : 'test'}
print(soup.find('div',attrs=attr))

txt = soup.find('h3',title='Good Content Title')
txt2 = soup.find('div', id='upper')
print(txt2.get_text())


print(txt['title'])

