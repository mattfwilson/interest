buy_price = 40000
sell_price = 24000

def gain_or_loss(buy, sell):
    res = (sell - buy) / buy
    return res

total = round(gain_or_loss(buy_price, sell_price), 6)
percentage = '{:.2%}'.format(total)
print(percentage)