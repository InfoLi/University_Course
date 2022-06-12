import requests
import time
import csv
import random
# import pymysql
from bs4 import BeautifulSoup

placelist = {
    # "bj":"beijing48",
    # "cd":"chengdu10",
    # "sh":"shanghai23",
    # "cq":"chongqing22",
    # "gz":"guangzhou45",
    # "sa":"sanya1",
    # "xa":"xian17",
    # "xm":"xiamen33",
    # "lj":"lijiang12",
    # "hz":"hangzhou7",
    # "qd":"qingdao8",
    # "dl":"dali3",
    # "wh":"wuhan55",
    # "nj":"nanjing9",
    # "shenzhen":"shenzhen49",
    # "cs":"changsha63",
    # "sz":"suzhou11",
    # "tj":"tianjin66",
    # "km":"kunming31",
    # "bh":"beihai251",

    # "am":"aomeny397",
    "cc":"changchun189",
    "gl":"guilin32",
    "heb":"haerbin64",
    "hf":"hefei50",
    }

# 获取整个页面
def getdate(url,header,i,filepath):
    datalist = [] 
    wbdata = requests.get(url,headers=header).text
    soup = BeautifulSoup(wbdata,'lxml')
    hotel = soup.find_all('div',class_="list-item-con")
    # 获取每个民宿的各个数据
    for item in hotel:
        title = item.find('a',class_="tit")
        price = item.find('span',class_="txt-price-now")
        viewpoint = item.find('span',class_="txt-viewpoint")
        comment = item.find('span',class_="txt-comment")
        point = item.find('span',class_="txt-point")
        people = item.find('span',class_="txt-people")
        # 处理为空的情况
        if (viewpoint != None):
            if(comment != None):
                datalist.append([title.text,price.text,viewpoint.text,comment.text.replace('条点评',''),point.text.replace('分',''),people.text.replace('人','')])
            else:
                datalist.append([title.text,price.text,viewpoint.text,"None","None",people.text.replace('人','')])
        else:
            if(comment != None):
                datalist.append([title.text,price.text,"None",comment.text.replace('条点评',''),point.text.replace('分',''),people.text.replace('人','')])
            else:
                datalist.append([title.text,price.text,"None","None","None",people.text.replace('人','')])

    # 写入数据
    with open(filepath,'a',newline="",encoding='gb18030') as csvfile:
        writer = csv.writer(csvfile)
        # writer.writerow(['民宿标题','价格','地利','评论数','得分','适合居住人数'])
        writer.writerows(datalist)
    
    # query = """insert into chongqing(title,price,viewpoint,comment,point,people)values(%s,%s,%s,%s,%s,%s)"""
    # value = (str(title.text),int(price.text),str(viewpoint.text),str(comment.text),str(point.text),str(people.text))
    # cur.execute(query,value)

def gospider():
    for p in placelist:
        filepath = "F:\python\Grade2_training\data\\" + str(p) + ".csv"
        place = placelist[p] #地方
        s = 1   #和**优先有关
        p = 1   #页面数
        # conn = pymysql.connect(host="127.0.0.1",user="root",passwd="a11129718",port=3306,db="python_shixun2",charset="utf8")
        # cur = conn.cursor()
        print("正在爬取"+place)
        with open(filepath,'w',newline="",encoding='gb18030') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['民宿标题','价格','地利','评论数','得分','适合居住人数'])
        for i in range(1,51):
            try:
                url = "https://inn.ctrip.com/onlineinn/newlist/"+place+"/?d1=2021-07-21&d2=2021-07-22&s="+str(s)+"&p="+str(p)+""
                cookie = '''ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; _RGUID=45128a26-b26c-4c67-9d01-4d9e1fe74704; _RDG=282a523ff346a926420d7dad2906008923; _RSG=dn4RoQYYIK44SqvVuPJ1q9; MKT_CKID=1625813933952.hb13c.8157; _ga=GA1.2.490019672.1625813934; StartCity_Pkg=PkgStartCity=2; GUID=09031018315428579336; nfes_isSupportWebP=1; nfes_isSupportWebP=1; cticket=AE184F19CF9A3E5392960261A00FCD8623FFD5D5A59AA677E4FC9F517937BF7F; AHeadUserInfo=VipGrade=10&VipGradeName=%BB%C6%BD%F0%B9%F3%B1%F6&UserName=&NoReadMessageCount=1; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yojXN5UTMe2Bf3nq5PW21dBIex1LXDdjDqqOcfA3lg2nItTlq08Y4auzZfKddTb6qcUu3Ryp9mwAdUI6etvQ1jo+TTwtBq7AYUw4Q3YjRGnu9+/iwBNQnMtNTauqUBJYdIHCcMRI9eCIx1eHlupuaGe1KuRzTY7BzTstq2bbkEWN3se9sExcdfhFIzGdIsmrBxb0hUVIlXKEIgooscXkhmNJmtSms2gYP6xoc84stJ5po87vZeQYDV/f2zKVeB4KdiNDK/Qdh2KlgEd+6pnU1NnMA==; DUID=u=5E979C27086F5A430455206BB2FA5387DD326BDF5E490B5584FF350B64DBD95C&v=0; IsNonUser=F; IsPersonalizedLogin=F; UUID=74D46955CF4D4880A6662122A42BBAF9; _gid=GA1.2.1374654894.1625902048; MKT_CKID_LMT=1625905236415; UM_distinctid=17a8f876ac4b72-09f8bddabc43e1-7a697e6d-1fa400-17a8f876ac5f01; U_TICKET_SELECTED_DISTRICT_CITY={%22value%22:{%22districtid%22:2%2C%22districtname%22:%22%E4%B8%8A%E6%B5%B7%22%2C%22isoversea%22:false%2C%22stage%22:%22inipageCity%22}%2C%22updateDate%22:1625906666830%2C%22createTime%22:1625906666670}; _abtest_userid=83f722b9-3935-4909-8296-64f16e56321d; _gcl_au=1.1.1259937470.1625906691; Session=SmartLinkCode=csdn&SmartLinkKeyWord=&SmartLinkQuary=_UTF.&SmartLinkHost=link.csdn.net&SmartLinkLanguage=zh; _RF1=218.70.255.165; Union=OUID=pp&AllianceID=4897&SID=155950&SourceID=&createtime=1625908564&Expires=1626513364249; MKT_OrderClick=ASID=4897155950&AID=4897&CSID=155950&OUID=pp&CT=1625908564250&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fallianceid%3D4897%26sid%3D155950%26ouid%3Dpp%26bd_vid%3D7961680554877864693%26keywordid%3D160662196614&VAL={"pc_vid":"1625813930669.gxsv9"}; _bfi=p1%3D102001%26p2%3D100101991%26v1%3D91%26v2%3D74; _jzqco=%7C%7C%7C%7C1625905236578%7C1.746096529.1625813933963.1625908564258.1625908567855.1625908564258.1625908567855.undefined.0.0.12.12; __zpspc=9.3.1625908564.1625908567.2%232%7Cwww.baidu.com%7C%7C%7C%7C%23; MKT_Pagesource=H5; _pd=%7B%22r%22%3A1%2C%22d%22%3A1331%2C%22_d%22%3A1330%2C%22p%22%3A1478%2C%22_p%22%3A147%2C%22o%22%3A1499%2C%22_o%22%3A21%2C%22s%22%3A1511%2C%22_s%22%3A12%7D; _bfa=1.1625813930669.gxsv9.1.1625905206839.1625911600242.3.107.10650016817; _gat=1'''
                header={
                    "cookie":cookie
                }
                getdate(url,header,p,filepath)
                print("正在爬取第"+str(p)+"页")
                p = p+1
                # 反爬休眠
                time.sleep(random.randrange(1, 4))
            except:
                print("error")
            finally:
                pass
    
gospider()



