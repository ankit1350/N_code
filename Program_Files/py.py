with open("txt.txt","r")as f:
    content=f.read()
    word=('a','an','the')
    for word in word:
        content=content.replace(word," ")
    
print(content)

