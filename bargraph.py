import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd

plt.style.use('ggplot')

data = pd.read_csv('datasets/data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

languase_counter = Counter()

for responses in lang_responses:
    language_counter.update(responses.split(';'))
    
    
languages = []
popularity = []
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
    
plt.barh(languages, popularity)

plt.ylabel('Popular Languages')
plt.xlabel('Popularity')
plt.title('Languages popularity among th developers')
plt.legend()
plt.xticks(ticks = x_index, labels = ages_x)
plt.tight_layout()
plt.show()
