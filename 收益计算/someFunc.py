import requests
import json
import math


# 汇率转换
def converter(money, rate):
    return money * rate


# 获取汇率
def get_rate(from_currency, to_currency, decimal_places_number = 2):
    get_rate_url = f"http://www.xe.com/api/protected/live-currency-pairs-rates/?currencyPairs={from_currency}/{to_currency}"

    # 添加请求头 authorization: Basic bG9kZXN0YXI6cHVnc25heA==
    headers = {
        "Authorization": "Basic bG9kZXN0YXI6cHVnc25heA==",
    }

    response = requests.get(get_rate_url, headers=headers)

    if response.status_code == 200:
        rate = round_to_sf(json.loads(response.text)[0]["rate"], decimal_places_number)
    else:
        rate = 0

    return rate


def round_to_sf(num, sig_digits):
    if num == 0:
        return 0
    return round(num, sig_digits - int(math.floor(math.log10(abs(num)))) - 1)


if __name__ == "__main__":
    print(get_rate("USD", "CNY"))
