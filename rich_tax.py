


def wealth_tax(start_sum):
    if int(start_sum) >= 5000000:
        start_sum = start_sum - (start_sum * 10 / 100)
        return start_sum
    else:
        return start_sum