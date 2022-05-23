# pydb
python db connect mapper

pymysql, pymongo

0. 준비   
- 디비 접근 정보
  - rsc/config.cfg
  ```
  host=127.0.0.1
  port=3306
  user=root
  pwd=password
  ```
  - 디비 설정
  ``` python
  cfg = db_cfg()
  cfg["db"] = "Database"
  ```
   
   
1. 쿼리

- 단순 셀렉
  - mysql
  ```
  my = mysql(cfg)
  
  cols = ["NO", "DATA", "REG_DT"]
  table_name = "tableA"
  where = "REG_DT='" + date + "'"
  
  res = my.select(
      cols,
      table_name,
      where
  )
  ```
  
  - mongo
  ```
  mg = mongo(cfg)
  
  columns = ["NO", "DATA", "REG_DT"]
  collection = "collectA"
  filters = {
      "REG_DT": {
          "$gt": start_date,
          "$lt": end_date,
      },
  }
   
  res = mg.select(
      columns,
      collection,
      filters
  )
  ```

- 대량 데이터 페이징
  - mysql
  ```
  my = mysql(cfg)
  
  cols = ["NO", "DATA", "REG_DT"]
  table_name = "tableA"
  where = "REG_DT='" + date + "'"
  
  res = my.select_many(
      cols,
      table_name,
      where,
      10000,
      0
  )
  ```

  - mongo
  ```
  mg = mongo(cfg)
  
  columns = ["NO", "DATA", "REG_DT"]
  collection = "collectA"
  filters = {
      "REG_DT": {
          "$gt": start_date,
          "$lt": end_date,
      },
  }
   
  res = mg.select_many(
      columns,
      collection,
      filters,
      10000,
      0
  )
  ```