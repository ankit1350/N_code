try:
    with open ('txt.txt','r') as f:
        f= f.read()
    with open ('ak.txt','r')as f:
        f=f.read()

except Exception as e:
    print(e)