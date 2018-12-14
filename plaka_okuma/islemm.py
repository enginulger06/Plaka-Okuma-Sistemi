import fonksiyonlar as fonk
import text

def goruntu(resim):

    try:

        sec= resim # buraya mainden direk yolunu göster
        b=""

        if len(sec)!="": #Seçilen dosya adı null değilse

            img=fonk.resimAc(sec)  #Resim Açma İşlemi

            img_gray=fonk.griyecevir(img)  #griye cevirme fonk


            gurultuazalt=fonk.gurultuAzalt(img_gray) #Gurultu azaltma fonksiyonu


            h_esitleme=fonk.histogramEsitleme(gurultuazalt) #Histogram Eşitleme


            morfolojik_resim=fonk.morfolojikIslem(h_esitleme) #Morfolojik islem


            goruntucikarma=fonk.goruntuCikarma(h_esitleme,morfolojik_resim) #Goruntu Çıkarma İşlemi



            goruntuesikleme=fonk.goruntuEsikle(goruntucikarma)  ##Goruntu Eşikleme İşlemi


            cannedge_goruntu=fonk.cannyEdge(goruntuesikleme)     #Canny_Edge İşlemi


            gen_goruntu=fonk.genisletmeIslemi(cannedge_goruntu)  #Dilated (Genişletme İşlemi)


            screenCnt=fonk.konturIslemi(img,gen_goruntu)                   #Kontur İşlemi


            yeni_goruntu=fonk.maskelemeIslemi(img_gray,img,screenCnt)    #Maskeleme İşlemi


            son_resim= fonk.plakaIyilestir(yeni_goruntu)   #Maskelenmiş görüntü üzerinde işlemler.

            b= text.text_yazi(yeni_goruntu,son_resim)

            fonk.cv2.waitKey()  #Bir tuşa basarsan pencereyi kapatır.
        return b

    except :
        print("Lütfen Resim adını kontrol ediniz...")
