
import urllib.request
import cv2
import numpy as np
import time
from PIL import Image
import pytesseract
import islemm

def resimler(say,dizi):
    dizi2=[]
    ####img=cv2.imread("resimler/"+say+".png")
    v="resimler/"+say+".png"

    img=islemm.goruntu(v)
    #a=islemler.goruntu("resimler/"+say+".png")
    #img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ###img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ###cv2.equalizeHist(img)
    ###cv2.imshow("son_resim", img)

    ###pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    ###text1 = pytesseract.image_to_string(img)#resim
    ##dizi.append(text1)
    ##dizi2.append(text1)
    print(img)

def kesme(img,say,dizi,url):
    if say>0:
        #crop_img = img[440:500, 360:520]
        crop_img = img[0:850, 0:540]
        cv2.imshow("cropped", crop_img)
        imge=cv2.imwrite("resimler/"+str(say)+".png", crop_img)
        resimler(str(say),dizi)
    else:
        aynı=[]
        yazdır=[]
        for i in range(0,len(dizi)-1):
            for j in range(i+1,len(dizi)):
                if dizi[i]!="" and dizi[i]==dizi[j] and dizi[i] not in aynı:
                    aynı.append(dizi[i])
                else:
                    break
        print("üsteki for aynı",aynı)
        if len(aynı)==1:
            print("len(aynı)==1", aynı)
        else:
            if len(aynı)==2:
                x=dizi.count(aynı[0])
                y=dizi.count(aynı[1])
                if x>y:
                    print("x>y",aynı[0])
                elif x==y:
                    print("x==y",aynı)
                else:
                    print("x<y",aynı[1])
            else:
                for i in range(0,len(aynı)-1):
                    for j in range(i+1,len(aynı)):
                        if aynı[i]==aynı[j] and aynı[i] not in yazdır:
                            yazdır.append(aynı[i])
                        else:
                            continue
                print("yazdır", yazdır)
        islem(url)

def islem(url):
    print(url)
    #url=
    say = 15
    dizi=[]
    x2 = 230
    y2 = 320
    w2 = 400
    h2 = 150
    while True:
        imgResp=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)
        img= cv2.resize(img, (850, 540))
        #cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (255, 255, 0), 2)
        cv2.imshow('test',img)
        #cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (255, 255, 0), 2)
        #cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
        say=say-1
        if ord('q')==cv2.waitKey(10):
            exit(0)
        kesme(img,say,dizi,url)
#img = cv2.imread("lenna.png")
#crop_img = img[y:y+h, x:x+w]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)
