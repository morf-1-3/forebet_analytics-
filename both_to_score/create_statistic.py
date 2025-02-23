# import bs, selector
# from bs import pars
# from selector import select_html
# from 
from both_to_score.bs import pars
from both_to_score.selector import select_html

# use function select_html (day,month,year) after pars(day,month,year)
def get_static_for_days(dates = None):
    if dates:
        pass
    else:

        dates = {
            # "12": [day for day in range(25,27)],
            "2": [day for day in range(16,17)]
        }
    # dates = {
    #     "12": [day for day in range(25,27)],
    #     # "1": [1,2,3,4]
    # }
    rezult = [0,0,0]
    for month,days in dates.items():
        for day in days:
            if(int(month) == 12 ):
                select_html(int(day),int(month),2024)
                rezult_function = pars(int(day),int(month),2024)
                rezult = [rezult_function[i] + rezult[i] for i in range(0,3)]
            else:
                select_html(int(day),int(month))
                rezult_function = pars(int(day),int(month))
                rezult = [rezult_function[i] + rezult[i] for i in range(0,3)]
    # write_all_statistic(rezult)        
    # print(rezult)

def write_all_statistic(rezults:list):
    with open(f"both_to_score/global_statistic.txt", "w", encoding="utf-8") as output_file:       
        output_file.write(f"count True : {rezults[0]},   count False : {rezults[1]}, count None : {rezults[2]} \n")
        if (rezults[0]+rezults[1]) > 0:
            output_file.write("winrate:" + str("{:.2f}".format((rezults[0] * 100)/(rezults[0]+rezults[1]))))
        
        print("Results saved to 'global_results.txt'.")


if __name__ == "__main__":
    get_static_for_days()
    # play_tuple()