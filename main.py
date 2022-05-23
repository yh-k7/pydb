import os
import pandas as pd

from src.mapper.mysql import mysql
from src.utils.config import db_cfg

if __name__ == "__main__":
    # 데이터 저장 경로
    save_path = "./data"
    if not os.path.isdir(save_path):
        os.mkdir(save_path)

    cfg = db_cfg()

    cfg["db"] = "DB1"

    my = mysql(cfg)

    cols = ["NO", "ID", "DTTM"]
    table_name = "T1"
    where = "ID='a1'"

    res = my.select_many(
        cols,
        table_name,
        where,
        100,
        0
    )

    data = pd.DataFrame(res, columns=cols)
    sfname = f'{save_path}/{table_name}.csv'
    data.to_csv(sfname, index=False)
    print(f'{sfname}.csv 저장 완료')
