



def anlyzePage1(text):
    retList=[]
    pos=text.find('第')
    pos = text.find('号',pos)+1
    s1= text[0:pos]
    print(s1)
    retList.append(s1)
    keyList=['权利人','共有情况','坐落','不动产单元号','权利类型','权利性质','用途','面积','使用期限','房屋结构']
    
    def substring(strText,key,nextKey,startpos):
        pos2 = strText.find(keyList[key],startpos)
        if pos2 ==startpos :
            startpos=startpos+len(keyList[key])
            if nextKey==-1:
                pos2=-1
            else:
                pos2=strText.find(keyList[nextKey],startpos)   
        print(keyList[key],"--->",strText[startpos:pos2])
        return pos2,strText[startpos:pos2]
        
    for a in range(len(keyList)):
        #print(a,keyList[a])
        nextKey=a+1
        if nextKey>= len(keyList):
            nextKey=-1
        pos,s= substring(text,a,nextKey,pos)
        retList.append(s)
    return retList


def anlyzePage2(text):
    return text[2:]

def testPage2():
    text=''
    with open('page2.txt','r',encoding='utf-8') as f:
        text=f.read()
    print(text)
    return anlyzePage2(text)

def testPage1():
    
    text=''
    with open('page1.txt','r',encoding='utf-8') as f:
        text=f.read()
    print(text)
    return anlyzePage1(text)


if __name__ == '__main__':
    ret1=testPage1()
    ret2= testPage2()
    with open('ret.csv','w') as f:
        for a in ret1:
            f.write(a+',')
        f.write(ret2)