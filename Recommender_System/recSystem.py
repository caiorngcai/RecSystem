import myUserCF.py

if __name__ == '__main__':
    ratingfile = 'ratings.dat'
    usercf = commonUserCF()
    usercf.generate_dataset(ratingfile)
    usercf.calculateUserSimilarity()
