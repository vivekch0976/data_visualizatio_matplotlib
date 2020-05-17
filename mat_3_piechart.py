import matplotlib.pyplot as plt
plt.style.use('ggplot')


slices = [59457, 54789, 51579, 49257, 34785,]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]
colors = ['#f5a31a', '#ad6989', '#5c2a9d', '#82c4c3', '#27496d']
plt.pie(slices, labels = labels, explode = explode,startangle = 24, colors = colors, 
        shadow = True,autopct ='%1.1f%%', wedgeprops = {'edgecolor': 'Black'})

plt.title('My awesome pie chart')
plt.tight_layout()
plt.show()
