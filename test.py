import requests
import random
import re

dictionary = requests.get('https://launchlibrary.net/1.4/launch?fields=name&limit=1000').json()

#print ', '.join(array)

random1 = random.randint(1,201)

print dictionary['launches'][random1]['name']
