


def withdrawal_percent(start_sum,amount):
    if amount > 30 and amount < 600:
                amount = amount - (amount * 1.5 / 100)
                start_sum -= amount
                return start_sum
    else:
        return start_sum