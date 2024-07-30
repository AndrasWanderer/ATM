



def percent_rep(start_sum,count_replainishment):
     if count_replainishment % 3 == 0:
        start_sum = start_sum + (start_sum * 3 / 100)
        return start_sum
     else:
         return start_sum