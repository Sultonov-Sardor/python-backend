# import requests
# from bs4 import BeautifulSoup


# def fetch_exchange_rates():
#     url = "https://valuta.exchange/"
#     response = requests.get(url)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, "html.parser")
#         exchange_rates = {}

#         table = soup.find(
#             "table", class_="FeeTable__TableContainer-sc-1112urg-4 iPnHWk")

#         for row in table.find_all("tr")[1:]:
#             columns = row.find_all("td")
#             if len(columns) == 6:
#                 currency = columns[0].text.strip()
#                 rate = float(columns[3].text.strip())
#                 exchange_rates[currency] = rate

#         return exchange_rates
#     else:
#         print("Failed to retrieve exchange rates.")
#         return None


# def convert_currency(amount, from_currency, to_currency, exchange_rates):
#     if from_currency in exchange_rates and to_currency in exchange_rates:
#         rate_from = exchange_rates[from_currency]
#         rate_to = exchange_rates[to_currency]

#         if rate_from and rate_to:
#             converted_amount = amount * (rate_to / rate_from)
#             return converted_amount
#         else:
#             print("Invalid exchange rates.")
#             return None
#     else:
#         print("Invalid currencies.")
#         return None


# def main():
#     exchange_rates = fetch_exchange_rates()

#     if exchange_rates:
#         print("Welcome to the Currency Exchange Program!")

#         while True:
#             print("\nOptions:")
#             print("1. Convert Currency")
#             print("2. Quit")
#             choice = input("Enter your choice (1/2): ")

#             if choice == "1":
#                 amount = float(input("Enter the amount: "))
#                 from_currency = input(
#                     "Enter the source currency (e.g., USD): ").upper()
#                 to_currency = input(
#                     "Enter the target currency (e.g., EUR): ").upper()

#                 converted_amount = convert_currency(
#                     amount, from_currency, to_currency, exchange_rates)
#                 if converted_amount is not None:
#                     print(
#                         f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
#             elif choice == "2":
#                 print("Goodbye!")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")


# if name == "main":
#     main()

# import requests
# from bs4 import BeautifulSoup

# def fetch_kurs():
#     url = "https://cbu.uz/oz/"
#     response = requests.get(url)

#     #  if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#     kurs = soup.select(".currency__item")
#     # print(kurs)

#     for item in kurs:
#         valyuta = item["data-currency"]
#         aP = input("valyuta kriting")

#         if aP != valyuta:
#             aP *= valyuta
#             print(aP)

# fetch_kurs()



# import requests
# import bs4

# data = requests.get("https://www.olx.uz/nedvizhimost/zemlja/")
# soup = bs4.BeautifulSoup(data.text, "html.parser")

# items = soup.select(".css-qfzxly")
# print(itemsjj)
# for item in items:
#     print(item)
























# items = soup.select(".currency__item")
# print(table)
# print(items)
# currency = {}
# for item in items:
#     value = item.find(class_="currency__item_value")
#     if not value:
#         continue
#     currency_type = item["data-currency"]
#     _value = value.text.strip().split(" = ")
#     value = float(_value[1])/float(_value[0].split(" ")[0])
#     currency[currency_type] = value
# # print(currency)

# while True:
#     text = input("hisoblamoqchi bo'lgan valyutangizni kiriting ")
#     text1 = input("valyuta-2 ")

#     if text == "exit":
#         break
#     text = text.split(" ")
#     text1 = text1.split(" ")

#     if len(text) != 2:
#         print("Xato kiritdingiz!")
#         continue
#     if len(text1) != 2:
#         print("Xato kiritdingiz!")
#         continue
#     if not text[1]  in currency:
#         print("Bunday valyuta mavjudmas")
#         continue
#     if not text1[1]  in currency:
#         print("Bunday valyuta mavjudmas")
#         continue
#     print(f"{text[0]} {text1[1]} = {(float(text[0])*currency[text1[1]]):.2f} ”")