from PIL import Image #importing the PILLOW package

im=Image.open("pic.png") #open image
pix=im.load() #load image
img_size=im.size #image size

ldata=[]
data=input("Enter the data to be encrypted:")
grp=3
fill=0

for i in data:
	ldata.append(ord(i)) #to ASCII

temp=ldata+[fill]*grp
sublist=[tuple(temp[q:q+grp]) for q in range(0,len(ldata),grp)]
sub=tuple(sublist)

i=0#col
k=1#row
c=1
for j in range(len(sublist)):
    if(k<=img_size[0]):
        pix[k,i]=sub[j] #location for storing
        k=k+10
    else:
        k=0
        i=i+c
        c=c+1 #column location generator

if(k<=255 and i<=255):
    pix[0,0]=(0,k,0) #row limit
    pix[2,0]=(0,i,0) #col limit
else:
    rem=k%255
    quo=k//255
    remi=i%255
    quoi=i//255
    pix[0,0]=(quo,rem,0) #row limit
    pix[2,0]=(quoi,remi,0) #col limit

print("Data Successfully Encrypted!")
im.save('fsample.png')

im.close()