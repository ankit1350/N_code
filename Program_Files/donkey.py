word='donkey'

with open("donkey.txt","r")as f:
    content=f.read()
    
contentNew=content.replace(word,"cat")

with open("donkey.txt","w")as f:
    f.write(contentNew)
    print(contentNew)