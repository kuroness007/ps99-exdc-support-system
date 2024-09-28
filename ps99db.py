import csv

db_list = []
def init_read():
  global db_list
  with open('ps99db.csv', encoding="shift-jis") as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    l_f = [row for row in reader]

  #print(l_f)
  db_list = l_f
  return db_list

def search(name):
  global prefix
  global db_list
  prefix = ""
  for i in range(len(db_list)):
    array = db_list[i]
    rtn_value = db_list[0]
    for j in range(len(array)):
      if(name == array[j]):
        return rtn_value
  return "NULL"
  #elif(name == "purple-chroma-phoenix"):
  #  set_prefix("P")
  #  return "chroma-phoenix"


# クロマデカペ対応
def get_prefix():
  global prefix
  return prefix

def set_prefix(text):
  global prefix
  if(text=="R"):prefix = "red-"
  elif(text=="O"):prefix = "orange-"
  elif(text=="Y"):prefix = "yellow-"
  elif(text=="G"):prefix = "green-"
  elif(text=="B"):prefix = "blue-"
  elif(text=="P"):prefix = "purple-"