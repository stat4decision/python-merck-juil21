import pandas as pd

class IMDB(object):
    RAW_FILE = "movie_metadata.csv"
    
    def __init__(self):
        self.full_info = pd.read_csv(self.__class__.RAW_FILE)
        self.ratings = self._keep_only_interesting_info()
        self._drop_duplicated_movies()
        
    def _keep_only_interesting_info(self):
        to_keep = ["num_critic_for_reviews", 
                   "duration",
                   "actor_1_facebook_likes",
                   "gross",
                   "budget",
                   "imdb_score",
                   "movie_title"]
        return self.full_info[to_keep].set_index("movie_title")


    def _drop_duplicated_movies(self):
        self.ratings = self.ratings.groupby(self.ratings.index).first()



