returns = {
    1995: .3720,
    1996: .2268,
    1997: .3310,
    1998: .2834,
    1999: .2089,
    2000: -.0903,
    2001: -.1185,
    2002: -.2197,
    2003: .2836,
    2004: -.1074,
    2005: .0483,
    2006: .1561,
    2007: .0548,
    2008: -.3655,
    2009: .2594,
    2010: .1482,
    2011: .0210,
    2012: .1589,
    2013: .3215,
    2014: .1352,
    2015: .0138,
    2016: .1177,
    2017: .2161,
    2018: -.0423,
    2019: .3121,
    2020: .1802,
    2021: .2847,
    2022: -.1801,
    2023: .2630,
}

lst_returns = list(returns)

def avg_returns(lst):
    total = 0
    for key, value in lst.items(): 
        total += lst[key]
    return round(total / len(lst), 4)

hist_interest = avg_returns(returns)
# res_perc = '{:.2%}'.format(hist_interest)
# print(f'Average gain from {lst_returns[0]} to {lst_returns[-1]} is {res_perc}.')
