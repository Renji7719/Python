#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-

 

import sys,io

#pipでpyperclipをインストールする必要あり

import pyperclip

import re

import webbrowser

import time

import requests

#########################################Read Me############################################

#OpenVAS便利ツール

#クリップボードに張り付けたパケット情報からパスを取得し、ユーザー入力値（第一引数）の

#Hostと結合することでフルパスを作成し、テキスト（第二引数）に出力するプログラム。

#

#拡張要素として、フルパスから?以降のパラメーターを取り除いたURLをChromeで検索しHTTPステータスを取得。

#404以外のステータスが得られたURLをパラメータ(パスの?以降)と結合してテキストに出力。

#アナリストはテキストに出力されたフルパスだけを調査すればよい。

###########################################################################################

 

#接続先URLが格納されたList型を返す関数

def Make_url_list(host):

    text_list=pyperclip.paste().split('\n') #クリップボードにコピーされた文字列を改行で分割してリストに格納

    url_list=[]                               #path_listとhost_listを結合したものを格納する

 

    for item in text_list:

        if 'GET' in item:  

                path=Remake_text(item)

                url_list.append(host+"/"+path)

    return url_list

 

#GET直後に出てきたパス（つまり接続先）を抽出

def Remake_text(default_text):

    removeGET_line=default_text.replace('GET','')

    removeHTTP_line=removeGET_line.replace('HTTP/1.1','')

    removeN_line=removeHTTP_line.replace('\n','')

    out='/'.join(removeN_line.split('/')[1:])  #"/"以降の文字列を取得

    path=out.split(" ")  #取得したpath以降の不要な文字列の除去  

    return path[0]

 

#リスト内パスをブラウザ検索かける関数

def Search_google(url_list):

    browser = webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s')

    for url in url_list:

        browser.open(url,new=2)

        time.sleep(1)

       

        

#HttpStatusのチェック。戻り値はHTTPステータス

#import requestsをする必要性あり

#Check_Http_Statusの関数の実用性は検証済みだが、リダイレクト処理に対しても200Statusを返してしまう。

#要検討

def Check_Http_Status(url):
    
    try:
        httpStatus=requests.get(url,allow_redirects=False)
        httpStatus.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(err)
        return False
    else:
        tempStatus=httpStatus.status_code
        print('------------------------------')
        print(url+":")
        print(tempStatus)
        print(" 調査の必要あり")
        print('------------------------------')


        return True
       

        

def yes_no_input():

    while True:

        print("上記のURLに接続してもよいですか?")

        choice = input("'yes' or 'no' [y/N]: ").lower()

        if choice in ['y', 'ye', 'yes']:

            return True

        elif choice in ['n', 'no']:

            return False

 

   

 

########################################################MAIN関数###########################################################

if __name__ == '__main__':

    args=sys.argv

    argCount=len(args)

    #Key値は重複なしURL、値は?以降のパラメーター（"せぱれーたー"区切り）

    url_dict={}

    #引数のIPアドレスのフォーマットチェック

    ipJudge=re.match('((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))',args[1])

 

    #引数チェック

    if(argCount!=3):

        print("引数の指定が間違っています。以下のフォーマットを参考に指定ください。")

        print("python OenVAS_Tool ホストIP 出力先テキストファイルのパス")

        quit()

       

    if ipJudge:

        default_url_list=Make_url_list(args[1])

        eliminate_duplication_url=set(default_url_list)   #重複しているURLを削除

       

        #URLとパラメータの分離作業

        for URLwithParam in eliminate_duplication_url: 

            param='?'.join(URLwithParam.split('?')[1:])

            
            if "=" in param:
                separateParam="?"+param                       #パラメータを取得
            else:
                separateParam=""
                

            separateURL=URLwithParam.split('?')

           

             #URLを格納。既に存在しているURLならurl_dictのvalueにパラメータに'せぱれーたー'文字列を付加し追加。

             #存在していないならURLをKeyに登録して、valueにパラメータを追加。

            if separateURL[0] in url_dict:

                url_dict[separateURL[0]]=url_dict[separateURL[0]]+"せぱれーたー"+separateParam

            else:

                url_dict.update({"http://"+separateURL[0]:separateParam}) 

                

       
        for url in url_dict.keys():
            print(url)

        #出力先テキストを開き、url_dictのkey値（url）に対して検索をする。200ならパラメーターと共にテキストに出力

        if yes_no_input():

            file=open(args[2],'w')

            for url in url_dict.keys():

                if Check_Http_Status(url):
                    
                    tempPath_list=url_dict[url].split("せぱれーたー")

                    for path in tempPath_list:
                            
                        if "せぱれーたー" in tempPath_list:
                            file.write(url+path)
                            file.write('\n')   
                        else:
                            file.write(url+path)
                            file.write('\n')

            file.close()

 

        quit()

      

        

 

       

        

        

        

    else:

        print("ipアドレスの形式が間違っています。")

        quit()

 

########################################################MAIN関数###########################################################

   

 

