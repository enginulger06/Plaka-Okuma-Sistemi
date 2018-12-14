from PIL import Image
import pytesseract
def text_yazi(yeni_goruntu,son_resim):
    dizi=[]
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    text1=pytesseract.image_to_string(yeni_goruntu)
    text2=pytesseract.image_to_string(son_resim)
    dizi.append(text1)
    dizi.append(text2)
    print(text1)
    print(text2)
    il_kodu=""
    return(text1,":",text2)



