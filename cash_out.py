



def del_sum():
    global start_sum
    global count_replainishment
    global amount
    value = atm_entry.get()
    a = test(int(value))
    if a != None:
        atm_entry.delete(0, tk.END)
        atm_entry.insert(0, a)
        
    elif start_sum < int(atm_entry.get()):
        atm_balance.delete(0, tk.END)
        atm_info.insert(0, f"Ошибка! Недостаточно средств!")

    else:
        try:
            start_sum -= int(value)
            start_sum = withdrawal_percent(start_sum,amount)
            # if withdrawal_percent == True:
            #     atm_info.insert(0, "Вычтен процент за снятие")
            start_sum = wealth_tax(start_sum)
            # if wealth_tax == True:
            #     atm_info.insert(0, "Вычтен процент налога на богатство")
            count_replainishment += 1
            start_sum = percent_rep(start_sum,count_replainishment)
            # if percent_rep == True:
            #     atm_info.insert(0, "Начислен процент за третье пополнение")
            print(start_sum)
        except:
            traceback.print_exc()
            atm_entry.delete(0, tk.END)
            atm_info.insert(0, "Некорректный ввод")
            