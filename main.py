import csv
import random

items = ["[demo] (stringreplace)'s special coffee", "[demo] (stringreplace)'s special Tea", "[demo] (stringreplace)'s Regular Flat Coffee"]
prices = ["2.50", "1.37", "4.88"]
location = "projectdemo"
names = ["Tim", "Zach", "Rachel", "Chris", "Monique"]
date_list = ["23/08/2021", "24/08/2021", "25/08/2021", "26/08/2021", "27/08/2021", "28/08/2021"]
time_list = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "10:10", "11:10", "12:10", "13:10", "14:10", "15:10"]
type_payment = ["CARD", "CASH"]

# 25/08/2021 09:02

if __name__ == '__main__':
    records = 0
    with open('test_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        while records < 1000:
            item_name = random.choice(items)
            price = random.choice(prices)
            date = random.choice(date_list)
            time = random.choice(time_list)
            name = random.choice(names)
            payment_type = random.choice(type_payment)
            total = 0.00
            card_number = random.randrange(4034005300, 5054005501)
            itemz = ""

            if random.choice([True, False]) == True:
                # should generate multiple order items
                for i in range(random.randint(1, 5)):
                    itemz += ","
                    item_name = random.choice(items)
                    price = random.choice(prices)
                    total += float(price)
                    if '(stringreplace)' in item_name:
                        itemz += f"{item_name.replace('(stringreplace)', f'{name}')} - {price}"
                        # print(itemz)
                    else:
                        itemz += f"{item_name} - {price}"
            else:
                total += float(price)
                itemz += f"{item_name.replace('(stringreplace)', f'{name}')} - {price}"
                # print(itemz)

            if itemz.startswith(","):
                itemz = itemz[1:]

            if itemz.endswith(","):
                itemz = itemz[:-1]

            if payment_type == "CARD":
                print(f'"{date} {time}","{location}","{name}","{itemz}","{price}","{payment_type}","{card_number}"')
                writer.writerow([f'{date} {time}', location, name, f"{itemz}", price, payment_type, card_number])
            else:
                print(f'"{date} {time}","{location}","{name}","{itemz}","{price}","{payment_type}",')
                writer.writerow([f'{date} {time}', location, name, f"{itemz}", price, payment_type, ])

            records += 1
