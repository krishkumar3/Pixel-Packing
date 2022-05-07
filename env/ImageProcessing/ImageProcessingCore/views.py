from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ImageProcessingCore.serializers import CoreSerializer
from rest_framework import viewsets
from ImageProcessingCore.models import Core
import os
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent
output_path = os.path.join(BASE_DIR, 'outputs')


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Core.objects.all()
    serializer_class = CoreSerializer


def homepage(request):
    context = {}
    return render(request, "index.html", context)


@csrf_exempt
def encryption(request, id, message):
    context = {}
    obj = Core.objects.get(id = id)
    path = obj.inputImage
    message = obj.message
    file_name = encrypt(id,path,message)
    obj.outputImage = file_name
    obj.save()
    return HttpResponse(file_name)

@csrf_exempt
def decryption(request,id):
    context = {}
    obj = Core.objects.get(id = id)
    path = obj.inputImage
    message = decrypt(path)
    obj.message = message
    obj.save()
    return HttpResponse(message)

def encrypt(id,path,message):
    print(path)
    print("output_path", output_path)
    im = Image.open(path)  # open image
    pix = im.load()  # load image
    img_size = im.size  # image size
    ldata = []
    data = message
    grp = 3
    fill = 0

    for i in data:
        ldata.append(ord(i))  # to ASCII

    temp = ldata + [fill] * grp
    sublist = [tuple(temp[q:q + grp]) for q in range(0, len(ldata), grp)]
    sub = tuple(sublist)

    col = 0  # col
    row = 1  # row
    c = 1
    for j in range(len(sublist)):
        if row <= img_size[0]:
            pix[row, col] = sub[j]  # location for storing
            row = row + 10
        else:
            row = 0
            col = col + c
            c = c + 1  # column location generator

    if row <= 255 and col <= 255:
        pix[0, 0] = (0, row, 0)  # row limit
        pix[2, 0] = (0, col, 0)  # col limit
    else:
        rem = row % 255
        quo = row // 255
        remi = col % 255
        quoi = col // 255
        pix[0, 0] = (quo, rem, 0)  # row limit
        pix[2, 0] = (quoi, remi, 0)  # col limit

    print("Data Successfully Encrypted!")
    file_name = output_path + "\output" + str(id)+'.png'
    im.save(file_name)
    im.close()
    return file_name


def decrypt(path):
    im = Image.open(path)  # open image
    pix = im.load()
    s = im.size  # image size
    ldata = []
    data = list(pix[0, 0])
    data1 = list(pix[2, 0])
    row = data[0] * 255 + data[1]  # row limit
    col = data1[0] * 255 + data1[1]  # col limit

    c = 1
    row_j = 1  # row
    col_i = 0  # col

    while col_i <= col:  # traverse through image
        while row_j < s[0]:
            if col_i == col and row_j == row:
                break
            else:
                ldata.append(list(pix[row_j, col_i]))
                row_j = row_j + 10
        col_i = col_i + c
        c = c + 1  # column location generator
        row_j = 0

    # print(l)
    output_string = ''
    for i in ldata:  # String extraction from list
        for j in i:
            if j == 255:
                continue
            output_string = output_string + chr(j)

    print("Decryption Successful!\n")
    print(output_string)  # Decrypted text
    im.close()
    return str(output_string)
