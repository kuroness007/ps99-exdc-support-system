# ライブラリの読み込み
from bs4 import BeautifulSoup
import urllib.request
import ps99db
import time

# 未対応　ランキング　レベルごと 日にちごと

def ranking():
  # len(ps99db.db_list)
  list = []
  debug = ""
  for i in range(5):
    name = str(i+1)
    ans = ps99db.search(name)
    if(ans == "NULL"):
      return "致命的なエラー："+str(name)
    print(ans) # bison
    huge_name = "huge-"+ans

    # print(huge_name) # bison
    pre = ps99db.get_prefix()
    base_name = pre + huge_name
    # ここで各金虹シャイニーのRAPとエキストを取得
    nre  = read(pre + huge_name) # RAP EXISTS
    gre  = read(pre + "Golden-"+huge_name)
    rre  = read(pre + "Rainbow-"+huge_name)
    snre = read(pre + "Shiny-"+huge_name)
    sgre = read(pre + "Shiny-Golden-"+huge_name)
    srre = read(pre + "Shiny-Rainbow-"+huge_name)

    # Existを基にランクする
    rank = do_rank(convert_to_number(nre[1]))

    # ダイヤ量を計算
    nper  = calc(rank,"N",nre[0],"99")
    gper  = calc(rank,"G",gre[0],"99")
    rper  = calc(rank,"R",rre[0],"99")
    snper = calc(rank,"SN",snre[0],"99")
    sgper = calc(rank,"SG",sgre[0],"99")
    srper = calc(rank,"SR",srre[0],"99")

    # nper[0] = "200k" nper[1] = "33.3"
    # リストアップ
    if(nper[1] != "0.0"):
      list.append([nper[1],huge_name,nper[0]])
    if(gper[1] != "0.0"):
      list.append([gper[1],"Golden-"+huge_name,gper[0]])
    if(rper[1] != "0.0"):
      list.append([rper[1],"Rainbow-"+huge_name,rper[0]])
    if(snper[1] != "0.0"):
      list.append([snper[1],"Shiny-"+huge_name,snper[0]])
    if(sgper[1] != "0.0"):
      list.append([sgper[1],"Shiny-Golden-"+huge_name,sgper[0]])
    if(srper[1] != "0.0"):
      list.append([srper[1],"Shiny-Rainbow-"+huge_name,srper[0]])
    time.sleep(0.002)
    list = sorted(list)
    time.sleep(0.002)
    #リスト追加
    if(len(list) > 25):
      list = list[0:25]

  text = str(len(ps99db.db_list))+"匹のノーマルデカペを見ました\n"
  for i in range(len(list)):
    text += "第" + str(i+1)+"位:"+list[i][2]+"もらえる"+list[i][1]+"の"+list[i][0]+"日\n"
  return text +"\n"+debug

def func(msg):
  print(msg) # exdc bison
  name = msg[5:len(msg)] # bison
  ans = ps99db.search(name)
  if(ans == "NULL"):
    return "該当データがありません"
  print(ans) # bison
  return make_list("huge-"+ans)

def make_list(huge_name):
  pre = ps99db.get_prefix()
  base_name = pre + huge_name
  nre  = read(pre + huge_name) # RAP EXISTS
  gre  = read(pre + "Golden-"+huge_name)
  rre  = read(pre + "Rainbow-"+huge_name)
  snre = read(pre + "Shiny-"+huge_name)
  sgre = read(pre + "Shiny-Golden-"+huge_name)
  srre = read(pre + "Shiny-Rainbow-"+huge_name)

  rank = do_rank(convert_to_number(nre[1]))
  nper = calc(rank,"N",nre[0],"1")
  gper = calc(rank,"G",gre[0],"1")
  rper = calc(rank,"R",rre[0],"1")
  snper = calc(rank,"SN",snre[0],"1")
  sgper = calc(rank,"SG",sgre[0],"1")
  srper = calc(rank,"SR",srre[0],"1")
  nper_mx = calc(rank,"N",nre[0],"99")
  gper_mx = calc(rank,"G",gre[0],"99")
  rper_mx = calc(rank,"R",rre[0],"99")
  snper_mx = calc(rank,"SN",snre[0],"99")
  sgper_mx = calc(rank,"SG",sgre[0],"99")
  srper_mx = calc(rank,"SR",srre[0],"99")
  
  n  = "N :" + gen_1(nre)  + "(LV1)" + gen_2(nper)  + "(LV99)" + gen_2(nper_mx)
  g  = "G :" + gen_1(gre)  + "(LV1)" + gen_2(gper)  + "(LV99)" + gen_2(gper_mx)
  r  = "R :" + gen_1(rre)  + "(LV1)" + gen_2(rper)  + "(LV99)" + gen_2(rper_mx)
  sn = "SN:" + gen_1(snre) + "(LV1)" + gen_2(snper) + "(LV99)" + gen_2(snper_mx)
  sg = "SG:" + gen_1(sgre) + "(LV1)" + gen_2(sgper) + "(LV99)" + gen_2(sgper_mx)
  sr = "SR:" + gen_1(srre) + "(LV1)" + gen_2(srper) + "(LV99)" + gen_2(srper_mx)
  
  return base_name + "※30日として計算(ランク：" + rank + ")\n" + n + "\n" + g + "\n" + r + "\n" + sn + "\n" + sg + "\n" + sr

def gen_1(re):
  return "RAP:" + re[0] + " Exist:" + re[1]
  
def gen_2(per):
  return "ダイヤ:" + per[0] + " 原価回収:" + per[1] + "日"

def read(huge_name):
  # URL
  url = "https://db.biggames.io/pet/v2/" + huge_name + "?game=ps99"
  # URLにアクセス 
  try:
    html = urllib.request.urlopen(url)
  except:
    return "0","0"
  time.sleep(0.01)
  # HTMLをBeautifulSoupで扱う
  soup = BeautifulSoup(html, "html.parser")
  # 出力
  list = soup.find_all("span", class_="__className_6592b5")
  try:
    name = soup.find("h2").get_text()
  except:
    return "0","0"
  exist = list[0].get_text()
  rap = list[1].get_text()
  print(rap,exist)
  return rap,exist


def calc(rank, type, rap, level):
  con_rap = convert_to_number(rap) # 38m
  time.sleep(0.002)
  daycare_diamond = round(calc_diamond(rank,type,level),4) # 1m
  time.sleep(0.002)
  print("diamond"+ str(daycare_diamond))
  if((con_rap==0) | (daycare_diamond==0)):return "0M","0"
  per = con_rap / daycare_diamond
  return str(daycare_diamond/1000000)+"M", str(round(per, 2))

def calc_diamond(rank, type, level):
  multi = 1
  if(  type == "G" ): multi = 1.3
  elif(type == "R" ): multi = 1.9
  elif(type == "SN"): multi = 2
  elif(type == "SG"): multi = 2.3
  elif(type == "SR"): multi = 2.9

  diamond = 0
  
  if(  rank == "S"): diamond = 1500000
  elif(rank == "A"): diamond = 1000000
  elif(rank == "B"): diamond = 750000
  elif(rank == "C"): diamond = 625000
  elif(rank == "D"): diamond = 500000
  elif(rank == "E"): diamond = 400000
  elif(rank == "F"): diamond = 300000
  elif(rank == "G"): diamond = 200000

  spend = diamond * multi
  if(level == "99"):
    spend = spend + diamond
    
  return spend
  
def do_rank(exist):
  if(  exist > 100000): return "G"
  elif(exist > 50000):  return "F"
  elif(exist > 25000):  return "E"
  elif(exist > 10000):  return "D"
  elif(exist > 5000):   return "C"
  elif(exist > 1000):   return "B"
  elif(exist > 500):    return "A"
  elif(exist > 0):      return "S"
  else:                 return "N"
  

def convert_to_number(s):
  units = {"k": 1000, "m": 1000000, "b": 1000000000}
  if s[-1].lower() in units:
      return int(float(s[:-1]) * units[s[-1].lower()])
  return int(s)