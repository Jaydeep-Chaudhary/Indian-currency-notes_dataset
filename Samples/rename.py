import os 
arr= os.listdir(".")
j=0
for source1 in arr:
    j=j+1
    destination1=str(j)+".jpg"
    os.rename(source1,destination1) 
