# -*- coding: utf-8 -*-
import os
import json
import jsonschema


LOOT_TABLE_JSON_DIR = "../playground/loot_tables/"
LOOT_TABLE_SCHEMA = "../java/data/loot_table.json"

def main():
  valid_check(LOOT_TABLE_SCHEMA, LOOT_TABLE_JSON_DIR)


def valid_check(schemaFile, dataDir):
  schema = json.load(open(schemaFile, 'r'))

  for pathname, dirnames, filenames in os.walk(dataDir):
    for filename in filenames:
        if filename.endswith('.json'):
         try:
          if(filename != None):
            data = json.load(open(dataDir + filename, 'r'))
            print ("Check: {} -> {}").format(schemaFile, dataDir + filename)
            result = jsonschema.validate(data, schema)
            if result == None:
              print ("{} OK".format(filename))
         except jsonschema.ValidationError as e: 
                print('Invalid JSON - {0}'.format(e.message))
                print ("{} NG".format(filename))
        
if __name__=='__main__':
    main()

#TODO 各種リソース類のValidate用の呼び出しMethodを分けて作成する
#TODO Json読み込み用Method作る
#TODO OK / NG 数カウントする
#TODO Exceptionは全てMainへ返して終了コードを 0 / 1 返す
#TODO GitHubURL参照できるようにしとく

#TODO 終了コードメモ
# 0 正常終了
# 1 NG終了
# -1 例外(バリデート失敗時の例外は除く)終了