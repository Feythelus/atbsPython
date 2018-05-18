import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile)) # class 'shelve.DbfilenameShelf'
print(shelfFile['cats']) # ['Zophie', 'Pooka', 'Simon']
shelfFile.close()