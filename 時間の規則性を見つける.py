import datetime
import decimal
from collections import Counter

#hh:mm:ss型の文字列をint型の秒数に変換してくれる関数
def changeDateToMinute(Time):
    #時間、分、秒ごとに変数に格納
    hour = int(Time.split(':')[0])
    minute = int(Time.split(':')[1])
    second = int(Time.split(':')[2])
    tempTime = datetime.timedelta(hours = hour,minutes = minute,seconds = second)
    
    return tempTime.seconds

#score100%
timeData1 = ['2019-10-22 19:38:10','2019-10-22 19:38:14','2019-10-22 19:38:18','2019-10-22 19:38:22',
            '2019-10-22 19:38:26','2019-10-22 19:38:30','2019-10-22 19:38:34','2019-10-22 19:38:38',
            '2019-10-22 19:38:42','2019-10-22 19:38:46','2019-10-22 19:38:50','2019-10-22 19:38:54',
            '2019-10-22 19:38:58','2019-10-22 19:39:02','2019-10-22 19:39:06','2019-10-22 19:39:10']
#score90%以下
timeData2 = ['2019-10-22 19:33:10','2019-10-22 19:38:14','2019-10-22 19:38:18','2019-10-22 19:38:22',
            '2019-10-22 19:38:26','2019-10-22 19:38:30','2019-10-22 19:38:34','2019-10-22 19:38:38',
            '2019-10-22 19:38:42','2019-10-22 19:38:46','2019-10-22 19:38:50','2019-10-22 19:38:54',
            '2019-10-22 19:38:58','2019-10-22 19:39:02','2019-10-22 19:40:06','2019-10-22 19:40:10']
#score90%以上100%未満
timeData3 = ['2019-10-22 19:38:09','2019-10-22 19:38:14','2019-10-22 19:38:18','2019-10-22 19:38:22',
            '2019-10-22 19:38:26','2019-10-22 19:38:30','2019-10-22 19:38:34','2019-10-22 19:38:38',
            '2019-10-22 19:38:42','2019-10-22 19:38:46','2019-10-22 19:38:50','2019-10-22 19:38:54',
            '2019-10-22 19:38:58','2019-10-22 19:39:02','2019-10-22 19:39:06','2019-10-22 19:39:10']
#最頻値が二つある場合のデータ
timeData4 = ['2019-10-22 19:38:10','2019-10-22 19:38:14','2019-10-22 19:38:18','2019-10-22 19:38:22',
            '2019-10-22 19:38:27','2019-10-22 19:38:32','2019-10-22 19:38:37',
            '2019-10-22 19:38:42','2019-10-22 19:38:47','2019-10-22 19:38:51','2019-10-22 19:38:55']
#ログ数が少なすぎる場合
timeData5 = ['2019-10-22 19:38:10','2019-10-22 19:38:14']

uniqueTimeData = list(sorted(set(timeData5),key=timeData5.index))

#求めたい等差をリストとして格納する
diff = []
#初項を格納する変数
a1 = 0
for i in range(0,len(uniqueTimeData)):
    uniqueTimeData[i] = uniqueTimeData[i].split(' ')[1]
    if i == 0:
        #初項格納(単位秒)
        a1 = changeDateToMinute(uniqueTimeData[i])
    else:
        #ひとつ前の時間との差分を計算(絶対値でほしい)
        tempDiff = abs((changeDateToMinute(uniqueTimeData[i]) - changeDateToMinute(uniqueTimeData[i-1])))
        #本当は(an-a)/(n-1)って公式だけど、iはnよりも1少ない(0からスタートなので)
        diff.append(tempDiff)

#diff配列から最頻値を取得
mode = Counter(diff).most_common()[0][0]
#正当率を格納
cnt = Counter(diff).most_common()[0][1]
#差が等しい確率を算出
probDiff = (cnt/(len(diff))) *100
#確率の有効数字を指定する
probDiff = round(probDiff,1)

#ログ数が10個以上欲しい
if len(uniqueTimeData) >= 10:
    #最頻値が100%の時、最頻値が2つあった場合の時にエラーを出力してしまう。エラーが出たらscore100%で間違いない
    try:
        #最頻値がふたつあった場合かつログ数が10個以上の場合(ログ数が少ないと過検知しちゃいそうだから)
        if cnt == Counter(diff).most_common()[1][1]:
            secondMode = Counter(diff).most_common()[1][0]
            print('規則性を2つ検知　間隔 : ' + str(mode) + "秒　と　" + str(secondMode) + '秒')
        #最頻値が1つで、scoreが90以上の場合
        elif probDiff > 90:
            print("規則性あり　間隔 : " + str(mode) +"秒　　　　score : " + str(probDiff) + "%")
        #最頻値が1つで、かつscoreが90未満の場合
        else:
            print("規則性なし　　　　score : " + str(probDiff) + "%")
    except:
        #ログが10個以上で、かつ、Counter(diff).most_common()の配列長さが1の場合は、scoreは100%
        print("規則性あり　間隔 : " + str(mode) +"秒　　　　score : " + str(probDiff) + "%")
else:
    print("ログ数が少なすぎます。測定できません。")
