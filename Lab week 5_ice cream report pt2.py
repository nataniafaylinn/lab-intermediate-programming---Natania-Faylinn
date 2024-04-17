salesData ={}

with open("icecream.txt", "r") as data:
    for line in data:
        if ":" in line:
            parts = line.strip().split(":")
            flavor = parts[0]
            sales = [float(part) for part in parts[1:]]
            total_sales = sum(sales)
            salesData[flavor] = {'sales': sales, "total_sales": total_sales}

    for index in range(len(sales)):
        store = f"store{index+1}"
        if store in salesData:
            salesData[store]['total_sales'] += sales[index]
        else:
            salesData[store] = {'total_sales': sales[index]}

print(salesData)