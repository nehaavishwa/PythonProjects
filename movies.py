__author__ = 'nehaavishwa'


import pandas as pd

unames = ['user_id', 'gender']
users = pd.read_table('/Users/nehaavishwa/Documents/Python/pydata-book-master/ch02/movielens/users.dat'
                      , sep='::'
                      , header=None
                      , names=unames
                      , engine='python')
print(users[:5])
