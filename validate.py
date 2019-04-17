# -*- coding: utf-8 -*-
import os
import json
import jsonschema

OK = 0
NG = 0
CASE = 0

LOOT_TABLE_JSON_DIR = "./playground/data/loot_manager/loot_tables/"
LOOT_TABLE_SCHEMA = "./java/data/loot_table.json"

ADVANCEMENT_JSON_DIR = "./playground/data/advancement_manager/advancements/"
ADVANCEMENT_SCHEMA = "./java/data/advancement.json"

MCMETA_JSON_DIR = "./playground/"
MCMETA_SCHEMA = "./java/data/pack.mcmeta.json"

def valid_check(schemaFile, dataDir,TestName):
  schema = json.load(open(schemaFile, 'r'))

  for pathname, dirnames, filenames in os.walk(dataDir.replace('/', os.sep)):
    global OK
    global NG
    global CASE
    if(TestName == "pack.mcmeta"):
      extension = ".mcmeta"
    else:
      extension = ".json"
    for datafile in filenames:
        if datafile.endswith('.json'):
          try:
            if(datafile != None):
              CASE += 1
              data = json.load(open(os.path.join(pathname, datafile), 'r'))
              print ("[{} - {}] Test: {}").format(TestName,CASE, datafile)
              result = jsonschema.validate(data, schema)
              if result == None:
                OK += 1
                print ("{} OK".format(datafile))
          except jsonschema.ValidationError as e: 
                NG += 1
                print('Invalid JSON - {0}'.format(e.message))
                print ("{} NG".format(datafile))
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
#TODO Json読み込み用Method作る
#TODO GitHubURL参照できるようにしとく