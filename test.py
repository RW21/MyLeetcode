<<<<<<< HEAD
list_ = ['1 2 3 4'.split(),'1 2 3 4'.split(),'2 4 3 1'.split(),'3 4 2 1'.split(),'4 3 2 1'.split()]

from collections import Counter

all_fruits = set(list_[0])
to_exclude = set()
for j in range(len(list_)):
    counts = {}
    for i in list_:
        if i[j] not in to_exclude:
            print(i[j])
            if i[j] not in counts:
                counts[i[j]] = 0
            counts[i[j]] += 1

    print(counts)
    print('toexclude', min(counts, key=counts.get))
    to_exclude.add(min(counts, key=counts.get))
=======
from collections import defaultdict

# assume that same months can be inputted
def calculate_coffee_stats(office_stats_list):
    stats = defaultdict(lambda: defaultdict(list))
    for office_stat in office_stats_list:
        place, month, consumption = office_stat.split(',')
        consumption = int(consumption)

        stats[place][month].append(consumption)
        
        # keep track of sum
        if not stats[place]['total']:
            stats[place]['total'] = consumption
        else:
            stats[place]['total'] += consumption

    result_string = ''
    for place, stat in {place:stats[place] for place in sorted(stats.keys())}.items():
        average = stat['total'] // 12
        result_string += place + ',' + str(stat['total']) + ',' + str(average) + '\n'

    return result_string[:-1]

# date format is YYYY-MM-DD
def get_rate(currency, date, rates):
    for rate in rates:
        rate_currency, rate_date, rate_amount = rate.split(',')
        if currency == rate_currency and date == rate_date:
            return float(rate_amount)

def calculate_profit(revenue_and_cost_stats, exchange_rates):
    generated_time, revenue, revenue_currency, cost, cost_currency = revenue_and_cost_stats.split(',')
    revenue = float(revenue)
    cost = float(cost)
    print(cost)

    date = generated_time[:10]
    if revenue_currency != 'NZD':
        revenue *= get_rate(revenue_currency, date, exchange_rates)
    if cost_currency != 'NZD':
        cost *= get_rate(revenue_currency, date, exchange_rates)
    
    return "{:.2f}".format(revenue - cost)

        


a = '2019-03-20T22:32:04+13:00,40345.23,NZD,23983.23,AUD'
b = ['AUD,2019-03-20,1.063103', 'AUD,2019-03-20,1.042530']

print(calculate_profit(a, b))
>>>>>>> 88312a6e16212060ee3c045a2612f2aef97eaf58
