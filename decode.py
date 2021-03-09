from PIL import Image #importing the PILLOW package

im=Image.open("fsample.png")
pix=im.load()
s=im.size #image size
l=[]
data=list(pix[0,0])
data1=list(pix[2,0])
row=data[0]*255+data[1] #row limit
col=data1[0]*255+data1[1] #col limit

c=1
j=1 #row
i=0 #col

while(i<=col): #traverse through image
    while(j<s[0]):
        if(i==col and j==row):
            break
        else:
            l.append(list(pix[j,i]))
            #print(j,i,list(pix[j,i]))
            j=j+10
    i=i+c
    c=c+1 #column location generator
    j=0

#print(l)
k=''
for i in l: #String extraction from list
    for j in i:
        if(j==255):
            continue
        k=k+chr(j)

print("Decryption Successful!\n")
print(k) #Decrypted text

im.close()