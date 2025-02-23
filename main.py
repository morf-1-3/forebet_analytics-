import os
# from .under_over.create_statistic import get_static_for_days as get_static_both_score
# from .both_to_score.create_statistic import get_static_for_days as get_static_under

import time
from under_over.create_statistic import get_static_for_days as get_static_both_score
from both_to_score.create_statistic import get_static_for_days as get_static_under
from mix_file.mix import merge_files

if __name__ == "__main__":
    dates = {
            # "12": [day for day in range(25,27)],
            "2": [day for day in range(16,17)]
        }
    
   
    
    get_static_both_score(dates)
    time.sleep(2)
    print("ready first")
    get_static_under(dates)
    time.sleep(2)
    print("start merge")
    merge_files()