parties = {}
seats = 450
total_votes = 0
total_seats = 0

def allocate_one_seat(result_dict, temp_dict):
    """
    Функция получает на вход в качестве параметров - словарь в котором хранится наш ответ result_dict,
    и временный словарь temp_dict, из которого мы будем удалять элементы по ходу вычисления.
    Функция возвращает эти же словари в измененном виде.
    """
    max_remainder = 0 # "лучший остаток"
    max_votes = 0 # "максимальное число голосов"
    for party in temp_dict: # перебираем партии во временном словаре, цель цикла - найти лучшю партиую которой достанется место
        if temp_dict[party]["remainder"] >= max_remainder: # если остаток текущей партии >= "лучшего остатка", то
            max_remainder = temp_dict[party]["remainder"] # мы запоминаем этот остаток как новый лучший
            if temp_dict[party]["votes"] > max_votes: # если число голосов у текущей партии лучше, чем "максимальное число голосов", то
                max_votes = temp_dict[party]["votes"] # мы обновляем значение переменной "максимальное число голосов"
                best_party = party # партия у которой лучший остаток и лучшее число голосов - наша "лучшая партия", эта перменная меняется по мере прохода цикла
    result_dict[best_party]["seats"] += 1 # отдаем одно место найденной "лучшей партии", запись в итоговый словарь
    del temp_dict[best_party] # удаляем "лучшую парти" из временного словаря, чтобы она больше не участвовала в распределении мест
    return result_dict, temp_dict 


with open('input.txt', 'r', encoding='utf-8') as votes:
    for line in votes:
        party_name, party_votes = ' '.join(line.split()[:-1]), int(line.split()[-1])        
        parties[party_name] = {"votes": party_votes, "remainder": 0, "seats": 0} # создали нужную структуру словаря
        total_votes += party_votes
votes_for_seat = total_votes / seats
for party in parties.values():
    party["seats"] = int(party["votes"] // votes_for_seat) # число целых мест в партии
    party["remainder"] =  party["votes"] / votes_for_seat - party["seats"] # остаток
    total_seats += party["seats"] 
seats_left = int(seats - total_seats) # считаем сколько мест у нас осталось нераспределенными
print(parties) # тестовый вывод
if seats_left: # если у нас не "0" оставшихся мест, то
    parties_copy = parties.copy() # делаем копию всего словаря партий, его назначение будет понятно дальше (из функции)
    for _ in range(seats_left): # нам надо респределить число мест = seats_left, соотв. цикл столько раз выполняется
        parties, parties_copy = allocate_one_seat(parties, parties_copy) # вызываем функцию распределения одного из оставшихся мест
for party in parties:
    print(party, parties[party]["seats"]) # результат