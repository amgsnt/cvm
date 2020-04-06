#!/usr/bin/python


#Os arquivos referentes ao mês corrente (M) e anterior (M-1) serão atualizados 
#diariamente com as eventuais reapresentações. 
#A atualização ocorre de terça a sábado, às 08:00h, 
#com os dados recebidos pelo CVMWeb até as 23:59h do dia anterior.
#Os arquivos referentes aos meses M-2 e M-3 serão atualizados semanalmente 
#com as eventuais reapresentações.
#Os arquivos referente aos meses M-4, M-5, ..., até M-11 serão atualizados 
#mensalmente com as eventuais reapresentações.

import urllib.request
import urllib.error
from datetime import datetime, timedelta

import os, zipfile

def downloadFundosHist():

    baseURL = "http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/"

    baseHistURL = "http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/HIST/"

    baseName = "inf_diario_fi_{:04d}{:02d}.csv"

    baseHistName = "inf_diario_fi_{:04d}.zip"

    baseDate = datetime.now()

    refDate = baseDate

    lOk = True

    print("Starting...{}".format(datetime.now()))

    while(lOk):
        
        mes = refDate.month
        ano = refDate.year

        fileName = baseName.format(ano,mes)

        url = baseURL + fileName

        try:
            urllib.request.urlretrieve(url, filename=fileName)
            print("Download OK: {}".format(fileName))

        except urllib.error.HTTPError as e:
            if e.code != 404:
                print("HTTPError error: {0}".format(e.code))
                raise
            else:
                lOk = False            

        urllib.request.urlcleanup()

        refDate = (refDate.replace(day=1) - timedelta(days=1)).replace(day=1)

    lOk = True

    while(lOk):
        
        fileName = baseHistName.format(ano)

        url = baseHistURL + fileName

        try:
            urllib.request.urlretrieve(url, filename=fileName)
            print("Download OK: {}".format(fileName))

        except urllib.error.HTTPError as e:
            if e.code != 404:
                print("HTTPError error: {0}".format(e.code))
                raise
            else:
                lOk = False            

        urllib.request.urlcleanup()

        ano = ano -1

  
    for item in os.listdir(os.getcwd()):
        if item.endswith(".zip"):
            print("Extracting: {}".format(item))
            
            file_name = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(file_name)
            zip_ref.extractall(os.getcwd())
            zip_ref.close()
            
            print("Removing: {}".format(item))

            os.remove(file_name)
    
    print("Finish...{}".format(datetime.now()))
    
downloadFundosHist()
