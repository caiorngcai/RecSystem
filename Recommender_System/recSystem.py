#-*- coding: utf-8 -*-

import myUserCF
import myItemCF
import sys, random, time, math
import pymysql

def runItemCF():
    conn = pymysql.Connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = '123456',
            db = 'InforRec',
            charset = 'utf8',
            )
    cursor = conn.cursor()

    ratingfile = 'ratings.dat'
    itemcf = myItemCF.commonItemCF()
    itemcf.generate_dataset(ratingfile)
    itemcf.calc_movie_sim()

    for m1, related_movies in itemcf.movie_sim_mat.items():
        for m2, count in related_movies.items():
            try:
                sql = "insert into item_sim(item1Id, item2Id, weight) values(%s, %s, %s)" % (m1, m2, itemcf.movie_sim_mat[m1][m2])
                cursor.execute(sql)
                conn.commit()
                print("insert %s and %s" % (m1, m2))
            except Exception as e:
                print(e)
                conn.rollback()
    print("Message: movie similiarity has been put into database.")

    for i, user in enumerate(itemcf.trainset):
        rec_movies = itemcf.recommend(user)

        for movie, w in rec_movies:
            try:
                sql = "insert into rec_result(userId, artId, weight) values(%s, %s, %s)" % (user, movie, w)
                cursor.execute(sql)
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
    print("Message: the result of itemCF has been put into database.")

    cursor.close()
    conn.close()

def runUserCF():
    conn = pymysql.Connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = '123456',
            db = 'InforRec',
            charset = 'utf8',
            )
    cursor = conn.cursor()

    ratingfile = 'ratings.dat'
    usercf = myUserCF.commonUserCF()
    usercf.generate_dataset(ratingfile)
    usercf.calculateUserSimilarity()

    for u, related_users in usercf.user_sim_mat.items():
        for v, count in related_users.items():
            try:
                sql = "insert into user_sim(user1Id, user2Id, count) values(%s, %s, %s)" % (u, v, count)
                cursor.execute(sql)
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
    print("Message: user similiarity has been put into database.")

    cursor.close()
    conn.close()

if __name__ == '__main__':
    # ratingfile = 'ratings.dat'
    # usercf = commonUserCF()
    # usercf.generate_dataset(ratingfile)
    # usercf.calculateUserSimilarity()
    runItemCF()
    runUserCF()
