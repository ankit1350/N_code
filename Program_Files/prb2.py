import os,time
file='wonder.txt'
print(file)

created=os.path.getctime(file)
modified=os.path.getmtime(file)
accessed=os.path.getatime(file)

print('date created:'+time.ctime(created))
print('date modified:'+time.ctime(modified))
print('date accessed:'+time.ctime(accessed))