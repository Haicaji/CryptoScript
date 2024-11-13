from someFunc import *

# 本金
capital_USDT = 4.06
# 上述本金的单日收益
bn_day_income_USDT = 0.00087657

# 获取汇率
USD_to_CNY_rate = get_rate("USD", "CNY")
USD_to_CNY_rate = USD_to_CNY_rate if USD_to_CNY_rate else print("获取汇率失败")
CNY_to_USD_rate = get_rate("CNY", "USD")
CNY_to_USD_rate = CNY_to_USD_rate if CNY_to_USD_rate else print("获取汇率失败")

# 币安理财账户USDT收益
bn_day_income_CNY = converter(bn_day_income_USDT, USD_to_CNY_rate)
print(f"币安理财账户 {capital_USDT} USDT 单日收益(CNY):", round_to_sf(bn_day_income_CNY, 2))
USDT_1_bn_day_income_USDT = bn_day_income_USDT / capital_USDT
print("币安理财账户 1 USDT 单日收益(USD):", round_to_sf(USDT_1_bn_day_income_USDT, 2))

# 支付宝余额宝收益
CNY_200_zfb_day_income_CNY = 0.01
zfb_income = converter(capital_USDT, USD_to_CNY_rate) / 200 * CNY_200_zfb_day_income_CNY
print("支付宝同等资金日收益(CNY):", round_to_sf(zfb_income, 2))
print("币安理财账户是支付宝余额宝收益的", round_to_sf(bn_day_income_CNY / zfb_income, 3), "倍")

# USDT买入价格
USDT_buy_price_CNY = 7.27
# USDT卖出价格
USDT_sell_price_CNY = 7.14
# USDT买卖成本
USDT_cost_CNY = USDT_buy_price_CNY - USDT_sell_price_CNY
USDT_cost_USD = converter(USDT_cost_CNY, CNY_to_USD_rate)
# 全放币安账户的回本时间(天)
bn_recovery_day = USDT_cost_USD / bn_day_income_USDT
print("CNY换USDT全放币安账户的回本时间(天):", round(bn_recovery_day, 0))
