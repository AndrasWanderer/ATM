from shell_atm import atm_entry
from exam import test


def check_sum():
    global start_sum
    global count_replainishment
    value = atm_entry.get()
    a = test(int(value))
    if a != None:
        atm_entry.delete(0, tk.END)
        atm_entry.insert(0, a)
    try:
        start_sum += int(value)
        start_sum = int(wealth_tax(start_sum))
        # if wealth_tax == True:
        #         atm_info.insert(0, "Вычтен процент налога на богатство")
        count_replainishment += 1
        start_sum = percent_rep(start_sum,count_replainishment)
        # if percent_rep == True:
        #         atm_info.insert(0, "Начислен процент за третье пополнение")
        print(start_sum)
    except:
        traceback.print_exc()
        atm_entry.delete(0, tk.END)
        atm_info.insert(0, "Некорректный ввод")