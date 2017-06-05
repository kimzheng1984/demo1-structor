import pymysql


# v3cn环境数据库连接，供调用
# account库
def connect_v3cndb_account(sql):
    # 连接数据库
    conn_v3cn_account = pymysql.connect(
        host='114.215.111.29',
        port=3306,
        user='yjw0223',
        passwd='f9a<)6hh>0pP',
        db='fzaccount',
    )
    # 创建游标
    cur = conn_v3cn_account.cursor()
    # 获得表中有多少条数据
    a = cur.execute(sql)
    # 打印表中所有数据
    info = cur.fetchmany(a)
    for i in info:
        print(i)
    # 关闭游标
    cur.close()
    # 提交事物，对数据库的更新操作时需要
    conn_v3cn_account.commit()
    # 关闭数据库连接
    conn_v3cn_account.close()


# exam库
def connect_v3cndb_exam(sql):
    # 连接数据库
    conn_v3cn_account = pymysql.connect(
        host='114.215.111.29',
        port=3312,
        user='yjw0223',
        passwd='f9a<)6hh>0pP',
        db='fzexam',
    )
    # 创建游标
    cur = conn_v3cn_account.cursor()
    # 获得表中有多少条数据
    a = cur.execute(sql)
    # 打印表中所有数据
    info = cur.fetchmany(a)
    for i in info:
        print(i)
    # 关闭游标
    cur.close()
    # 提交事物，对数据库的更新操作时需要
    conn_v3cn_account.commit()
    # 关闭数据库连接
    conn_v3cn_account.close()


# family库
def connect_v3cndb_family(sql):
    # 连接数据库
    conn_v3cn_account = pymysql.connect(
        host='114.215.111.29',
        port=3313,
        user='yjw0223',
        passwd='f9a<)6hh>0pP',
        db='fzfamily',
    )
    # 创建游标
    cur = conn_v3cn_account.cursor()
    # 获得表中有多少条数据
    a = cur.execute(sql)
    # 打印表中所有数据
    info = cur.fetchmany(a)
    for i in info:
        print(i)
    # 关闭游标
    cur.close()
    # 提交事物，对数据库的更新操作时需要
    conn_v3cn_account.commit()
    # 关闭数据库连接
    conn_v3cn_account.close()


# report库
def connect_v3cndb_report(sql):
    # 连接数据库
    conn_v3cn_account = pymysql.connect(
        host='114.215.111.29',
        port=3314,
        user='yjw0223',
        passwd='f9a<)6hh>0pP',
        db='fzreport',
    )
    # 创建游标
    cur = conn_v3cn_account.cursor()
    # 获得表中有多少条数据
    a = cur.execute(sql)
    # 打印表中所有数据
    info = cur.fetchmany(a)
    for i in info:
        print(i)
    # 关闭游标
    cur.close()
    conn_v3cn_account.commit()
    # 关闭数据库连接
    conn_v3cn_account.close()