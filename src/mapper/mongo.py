import pymongo
import warnings

warnings.filterwarnings(action='ignore')


class mongo(object):
    def __init__(self, cfg: dict):
        """
        About mongo database connect.
        :param cfg: host, port dict type
        """
        print("DB 접근 정보:", cfg['host'])
        print(cfg)
        try:
            # MongoDB 클라이언트 선언
            self.conn = pymongo.MongoClient(
                host=cfg["host"],
                port=int(cfg["port"])
                # username=cfg["user"]
                # password=cfg["pwd"]
                # replica=replica set
                # authSource=auth database
            )

            # DB 선택
            self.cursor = self.conn[cfg["db"]]
            print('MongoDB Connected.')
        except Exception as e:
            print(e)

    # def __del__(self):
    #     self.conn.close()

    def select(self, columns: list, collection: str, filters: dict) -> list:
        """
        fillers, columns 조건으로 MongoDB 검색 결과 반환
        :param collection: Collection name of MongoDB DB
        :param columns:
        :param filters:
        :param s_cnt: 시작할 데이터 index
        :param e_cnt: 한번에 불러올 데이터의 갯수
        :return: res(list)
        """
        columns = dict([(_, 1) for _ in columns])
        # Collection 선택
        cursor = self.cursor[collection]

        res = cursor.find(filters,
                          projection=columns,
                          no_cursor_timeout=True)
        res = list(res)

        return res

    def select_many(self, columns: dict, collection: str, filters: dict, odc: int = 1000, s_cnt: int = 0) -> list:
        """
        fillers, columns 조건으로 MongoDB 검색 결과 반환
        :param columns: column names
        :param filters: select option
        :param collection: Collection name of MongoDB DB
        :param odc: limit count, 한번에 불러올 데이터의 갯수
        :param s_cnt: start data index
        :return: list
        """
        columns = dict([(_, 1) for _ in columns])
        # Collection 선택
        cursor = self.cursor[collection]

        try:
            rc_cnt = 0
            len_cnt = s_cnt
            res = []

            while len_cnt == s_cnt:
                print(len_cnt)
                temp_data = cursor.find(filters,
                                        projection=columns,
                                        no_cursor_timeout=True).skip(s_cnt).limit(odc)
                temp_data = list(temp_data)
                len_cnt = len(temp_data)
                res.extend(temp_data)
                del temp_data
                cnt += 1
                rc_cnt = rc_cnt + s_cnt

            print("총 데이터 수:", len(res))
        except Exception as e:
            print(f'exec_fetchall error: {e}')

        return res
