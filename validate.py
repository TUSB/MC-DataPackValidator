#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib2
import json
from json.decoder import WHITESPACE
import jsonschema

OK = 0
NG = 0
CASE = 0

LOOT_TABLE_JSON_DIR = "./playground/TheUnusualSkyBlock/data/loot_manager/loot_tables/"
LOOT_TABLE_SCHEMA = "https://raw.githubusercontent.com/CommandBlockLogic/minecraft-json-schemas/master/java/data/loot_table.json"

ADVANCEMENT_JSON_DIR = "./playground/TheUnusualSkyBlock/data/advancement_manager/"
ADVANCEMENT_SCHEMA = "https://raw.githubusercontent.com/CommandBlockLogic/minecraft-json-schemas/master/java/data/advancement.json"

MCMETA_JSON_DIR = "./TheUnusualSkyBlock/playground/"
MCMETA_SCHEMA = "https://raw.githubusercontent.com/CommandBlockLogic/minecraft-json-schemas/master/java/data/pack.mcmeta.json"

def valid_check(schemaFile, dataDir,TestName):
  try:
    r = urllib2.urlopen(schemaFile)
    schema = json.loads(r.read())
    # print (schema)
  finally:
      r.close()
  for pathname, dirnames, filenames in os.walk(dataDir.replace('/', os.sep)):
    global OK
    global NG
    global CASE
    if(TestName == "pack.mcmeta"):
      extension = ".mcmeta"
    else:
      extension = ".json"
    for datafile in filenames:
        if datafile.endswith(extension):
          try:
            if(datafile != None):
              CASE += 1
              with open(os.path.join(pathname, datafile)) as fh:
                j = json.loads(fh.read(), "utf-8")
                d = json.dumps(j, ensure_ascii=False)
                data = json.loads(d)
                # print (data)
              print ("[{} - {}] Test: {}").format(TestName,CASE, datafile)
              result = jsonschema.validate(data, schema)
              if result == None:
                OK += 1
                print ("{} OK".format(datafile))
          except jsonschema.ValidationError as e: 
                NG += 1
                print('Invalid JSON - {0}'.format(e.message))
                print ("{} NG".format(datafile))
          except Exception as e:
              print('ERROR - {0}'.format(e))
          finally: print("")
        
if __name__=='__main__':
    valid_check(LOOT_TABLE_SCHEMA, LOOT_TABLE_JSON_DIR,"Loottable")
    print("Case: {0} - OK: {1} / NG: {2}").format(CASE, OK, NG)

    print("")
    print("* ------ *")
    print("")
    valid_check(ADVANCEMENT_SCHEMA, ADVANCEMENT_JSON_DIR,"advancement")
    print("Case: {0} - OK: {1} / NG: {2}").format(CASE, OK, NG)

    print("")
    print("* ------ *")
    print("")

    if(CASE == OK + NG):
      if(CASE == OK): exit(0)
      else: exit(1)
#TODO 各種リソース類のValidate用の呼び出しMethodを分けて作成する
#TODO レシピ
#TODO Json読み込み用Method作る