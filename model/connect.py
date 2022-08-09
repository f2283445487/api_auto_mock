import pymysql
from common import com
from dbutils.pooled_db import PooledDB

read = com.read_yaml('db')
pool_db = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=1,
    maxcached=5,
    blocking=True,
    maxusage=None,
    ping=0,
    host=read.get('host'),
    user=read.get('user'),
    password=read.get('password'),
    database=read.get('database'))


class SQLHelper():

    @staticmethod
    def con():
        db = pool_db.connection()
        cur = db.cursor(pymysql.cursors.DictCursor)
        return db, cur

    @staticmethod
    def close(cur, db):
        cur.close()
        db.close()

    @classmethod
    def select(cls, sql, args):
        try:
            db, cur = cls.con()
            cur.execute(sql, args)
            data = cur.fetchall()
            cls.close(cur, db)
            return data
        except Exception as e:
            print(e)

    @classmethod
    def create(cls, sql):
        try:
            db, cur = cls.con()
            cur.execute(sql)
            db.commit()
            cls.close(cur, db)
        except Exception as e:
            print(e)
