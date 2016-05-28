#-*- coding: utf-8 -*-

import sys, random, time, math
from operator import itemgetter

# nowSecond = time.strftime("%S")
# print(nowSecond)
# random.seed(nowSecond)
random.seed(0)

class commonUserCF():
    
    def __init__(self):
        self.trainset = {}
        self.testset = {}

        self.n_sim_user = 20
        self.n_rec_movie = 10

        self.user_sim_mat = {}
        self.movie_popular = {}
        self.movie_count = 0

        print("Message: Init finish!")

    def recommend(self, user):
        K = self.n_sim_user
        N = self.n_rec_movie
        rank = dict()
        watched_movies = self.trainset[user]

        # v=similar user, wuv = similarity factor
        for v, wuv in sorted(self.user_sim_mat[user].items(), key=itemgetter(1), reverse=True)[0:K]:
            for movie in self.trainset[v]:
                if movie in watched_movies:
                    continue
                rank.setdefault(movie, 0)
                rank[movie] += wuv

        # return the N best movies
        return sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]

        print("Message: recommendation finished!")

    def calculateUserSimilarity(self):
        movie2users = dict()    # movie2users is a dictionary

        for user, movies in self.trainset.items():
            for movie in movies:
                if movie not in movie2users:
                    movie2users[movie] = set()  # set
                movie2users[movie].add(user)

                if movie not in self.movie_popular:
                    self.movie_popular[movie] = 0
                self.movie_popular[movie] += 1
        
        # save the total movie number, which will be used in evaluation
        self.movie_count = len(movie2users)

        usersim_mat = self.user_sim_mat     # 感觉多余，python传递值，用usersim_mat就相当于用self.user_sim_mat
        
        for movie, users in movie2users.items():
            for u in users:
                for v in users:
                    if u == v :
                        continue
                    usersim_mat.setdefault(u, {})
                    usersim_mat[u].setdefault(v, 0)
                    usersim_mat[u][v] += 1

        for u, related_users in usersim_mat.items():
            for v, count in related_users.items():
                usersim_mat[u][v] = count/math.sqrt(len(self.trainset[u])*len(self.trainset[v]))
                # print("u & v : %s" % usersim_mat[u][v])
                
        print("Message: Similarity calculating finished!")

        '''test output'''
        # for u,vs in usersim_mat.items():
            # for v in vs:
                # if usersim_mat[u][v] >= 0.5:
                    # print("%s & %s: %s" % (u, v, usersim_mat[u][v]))

    def generate_dataset(self, filename, pivot=0.7):
        trainset_len = 0
        testset_len = 0

        for line in self.loadfile(filename):
            user, movie, rating, timestamp = line.split("::")
            # print("line:%s" % line)
            # print("user=%s, movie=%s, rating=%s, timestamp=%s" % (user, movie, rating, timestamp))
            
            if(random.random() < pivot):
                self.trainset.setdefault(user, {})
                self.trainset[user][movie] = int(rating)
                trainset_len += 1
            else:
                self.testset.setdefault(user, {})
                self.testset[user][movie] = int(rating)
                testset_len += 1

        print("Message: generate dataset success! trainset_len=%s , testset_len=%s" % (trainset_len, testset_len))

        '''print trainset and testset to test program'''
        # for user,movies in self.trainset.items():
            # print("user:%s" % user)
            # for movie in movies:
                # print("user:%s, movie:%s" % (user, movie))

        # for user,movies in self.testset.items():
            # print("user:%s" % user)
            # for movie in movies:
                # print("user:%s, moive:%s" % (user, movie))

    def evalute(self):
        N = self.n_rec_movie
        hit = 0
        rec_count = 0
        test_count = 0
        all_rec_movies = set()
        popular_sum = 0

        for i, user in enumerate(self.trainset):
            if i % 50 == 0:
                print("Message: recommended for %s users" % i)

            test_movies = self.testset.get(user, {})
            rec_movies = self.recommend(user)
            for movie, w in rec_movies:
                if movie in test_movies:
                    hit += 1
                all_rec_movies.add(movie)
                popular_sum += math.log(1 + self.movie_popular[movie])
            rec_count += N
            test_count += len(test_movies)

        precision = hit / (1.0*rec_count)
        recall = hit / (1.0*test_count)
        coverage = len(all_rec_movies) / (1.0*self.movie_count)
        popularity = popular_sum / (1.0*rec_count)

        print("Message: Evaluate finished")
        print('precision=%.4f\trecall=%.4f\tcoverage=%.4f\tpopularity=%.4f' %  (precision, recall, coverage, popularity))

    @staticmethod
    def loadfile(filename):
        '''load a file, return a generator'''
        fp = open(filename, 'r')
        for i, line in enumerate(fp):
            yield line.strip('\r\n')
            # if(i == 100000):
                # break
        fp.close()
        print("Message: load file %s success!" % filename)

if __name__ == '__main__':
    ratingfile = 'ratings.dat'
    usercf = commonUserCF()
    usercf.generate_dataset(ratingfile)
    usercf.calculateUserSimilarity()
    usercf.evalute()
