import pymysql


class mysql:
    def __init__(self, cfg: dict, debug: bool = False):
        """
        About mysql database connect.
        mysql 커넥트 사용.
        :param cfg: database info.
        :param debug: debug check.
        """
        self.debug = debug
        print("DB 접근 정보:", cfg["host"], cfg["user"])
        try:
            self.conn = pymysql.connect(
                host=cfg["host"],
                port=int(cfg["port"]),
                user=cfg["user"],
                passwd=cfg["pwd"],
                db=cfg["db"],
                charset='utf8'
            )

            self.cursor = self.conn.cursor()
            print('MySQL Connected.')
        except Exception as e:
            print(e)

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        self.conn.close()

    def select(self, columns: list, table_name: str, where: str) -> list:
        """
        셀렉 쿼리 생성
        :param columns: list, column names
        :param table_name: str, table
        :param where: str, select option
        :return:
        """
        try:
            query = f'SELECT {", ".join(columns)} FROM {table_name}'
            if where:
                query += f' WHERE {where}'

            if self.debug:
                print(query)

            self.cursor.execute(query)
            res = self.cursor.fetchall()

            if self.debug:
                print(res[:5])
        except Exception as e:
            print(f'exec_fetchall error: {e}')
        return res

    def select_many(self, columns: list, table_name: str, where: str, odc: int = 2000, s_cnt: int = 0) -> list:
        """
        리밋을 이용한 셀렉 쿼리 생성
        :param columns: list, column names
        :param table_name: str, table
        :param where: str, select option
        :param odc: int, limit count, 한번에 불러올 데이터의 갯수
        :param s_cnt: int, start data index
        :return: list
        """
        try:
            query = f'SELECT {", ".join(columns)} FROM {table_name}'
            if where:
                query += f' WHERE {where}'

            cnt = 0
            len_cnt = odc
            res = list()

            while len_cnt == odc:
                temp_query = f'{query} limit {s_cnt}, {odc}'
                # print(temp_query)
                self.cursor.execute(temp_query)
                temp_data = self.cursor.fetchall()
                len_cnt = len(temp_data)
                res.extend(list(temp_data))
                del temp_data
                cnt += 1
                s_cnt += odc

            print("총 데이터 수:", len(res))
        except Exception as e:
            print(f'exec_fetchall error: {e}')
        return res

    def exec_query(self, query, *args):
        """
        삽입, 수정, 삭제 쿼리 실행.
        :param query:
        :param args:
        """
        try:
            if args:
                query = query.replace("%s", "\'%s\'")
                query = "{}".format(query) % args

            if self.debug:
                print(query)

            self.cursor.execute(query)
        except Exception as e:
            print(f'exec_auto_commit error: {e}')

    def commit(self):
        """
        커밋
        """
        self.conn.commit()

    def exec_auto_commit(self, query, *args):
        """

        :param query:
        :param args:
        :return:
        """
        try:
            if args:
                query = query.replace("%s", "\'%s\'")
                query = "{}".format(query) % args
            if self.debug:
                print(query)
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print(f'exec_auto_commit error: {e}')
