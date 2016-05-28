#-*- coding: utf-8 -*-

import sys, random, math, time
from operator import itemgetter

random.seed(0)

class commonItemCF():

    def __init__(self):
        self.trainset = {}
        self.testset = {}

        self.n_sim_movie = 20
        self.n_rec_movie = 10

        self.movie_sim_mat = {}
        self.movie_popular = {}
        self.movie_count = 0

        print("Message: Initialization finishes!")

    @staticmethod
    def loadfile(filename):
        fp = open(filename, 'r')
        for i, line in enumerate(fp):
            yield line.strip('\r\n')
            if(i == 10000):
                break

        fp.close()
        print("Message: the %s opened" % filename)

    def generate_dataset(self, filename, pivot=0.8):
        trainset_len = 0
        testset_len = 0

        for line in self.loadfile(filename):
            user, movie, rating, timestamp = line.split('::')

            if(random.random() < pivot):
                self.trainset.setdefault(user, {})
                self.trainset[user][movie] = int(rating)
                trainset_len += 1
            else:
                self.testset.setdefault(user, {})
                self.testset[user][movie] = int(rating)
                testset_len += 1

        print("Message: Dataset generation finished!! trainset_len = %s, testset_len = %s" % (trainset_len, testset_len))

    def calc_movie_sim(self):
        for user, movies in self.trainset.items():
            for movie in movies:
                if movie not in self.movie_popular:
                    self.movie_popular[movie] = 0
                self.movie_popular[movie] += 1

        self.movie_count = len(self.movie_popular)

        itemsim_mat = self.movie_sim_mat

        for user, movies in self.trainset.items():
            for m1 in movies:
                for m2 in movies:
                    if m1 == m2:
                        continue
                    itemsim_mat.setdefault(m1, {})
                    itemsim_mat[m1].setdefault(m2, 0)
                    itemsim_mat[m1][m2] += 1

        simfactor_count = 0

        for m1, related_movies in itemsim_mat.items():
            for m2, count in related_movies.items():
                itemsim_mat[m1][m2] = count / math.sqrt(self.movie_popular[m1] * self.movie_popular[m2])
                simfactor_count += 1
                
                # if simfactor_count % 2000000 == 0 
                    # print("!!")

        print("Message: calculation finished!!!")

    def recommend(self, user):
        K = self.n_sim_movie
        N = self.n_rec_movie
        rank = {}
        watched_movies = self.trainset[user]

        for movie, rating in watched_movies.items():
            for related_movie, w in sorted(self.movie_sim_mat[movie].items(), key=itemgetter(1), reverse=True)[:K]:
                if related_movie in watched_movies:
                    continue
                rank.setdefault(related_movie, 0)
                rank[related_movie] += w * rating

        return sorted(rank.items(), key=itemgetter(1), reverse=True)[:N]
                
    def evaluate(self):
        N = self.n_rec_movie
        hit = 0
        rec_count = 0
        test_count = 0

        all_rec_movies = set()
        popular_sum = 0

        for i, user in enumerate(self.trainset):
            if i% 1000 == 0:
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

        precision = hit / (1.0 * rec_count)
        recall = hit / (1.0 * test_count)
        coverage = len(all_rec_movies) / (1.0 * self.movie_count)
        popularity = popular_sum / (1.0 * rec_count)

        print("Message: Recommendation finished !!!!!")
        print('precision=%.4f\trecall=%.4f\tcoverage=%.4f\tpopularity=%.4f' %  (precision, recall, coverage, popularity))


if __name__ == '__main__' :
    ratingfile = 'ratings.dat' 
    itemcf = commonItemCF()
    itemcf.generate_dataset(ratingfile)
    itemcf.calc_movie_sim()
    itemcf.evaluate()
