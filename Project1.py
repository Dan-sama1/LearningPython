#POS
import datetime
now = datetime.datetime.now()
formatted_time = now.strftime("Date and time: %Y-%m-%d %I:%M:%S %p")
product = {}
trans_logs = {}

#FORMAT
def format():
    print(f"""{"="*20}
    POS - PROGRAM
{"="*20}
Task:
    A - Add a Product
    V - View Product
    D - Delete a Product
    T - Transact Sales
    [ANY KEY] - Exit""")
    enter = input("Chosen task: ").upper()
    return enter

#ADD PRODUCT
def add():
    print(f"""{"=" * 20}
    Add a Product
{"=" * 20}

{formatted_time}
""")
    prod = input("Product Name: ").upper()
    try:
        price = float(input("Product Price: "))
    except ValueError:
        print("The Product NOT ADDED. Invalid Price!")
    else:
        product[prod] = price

#VIEW PRODUCT
def view():
    print(f"""{"=" * 20}
    View Product
{"=" * 20}

{formatted_time}""")
    for prod, price in product.items():
        print(f"""
Product Name: {prod}
    Product Price: {price}""")

#DELETE PRODUCT
def delete():
    print(f"""{"=" * 20}
    Delete Product
{"=" * 20}

{formatted_time}
""")
    delete_prod = input("Product Name: ").upper()
    if delete_prod in product:
        del product[delete_prod]
        print("The product DELETED from the system!")
    else:
        print("The Product does NOT EXIST!")
#TRANSACTION SALES
def transact():
    print(f"""{"=" * 26}
   < Transaction Sales >
{"=" * 26}

{formatted_time}
""")
    trans_prod = {}
    total = 0
    while True:
        enter = input("Product Name (type 'x' to STOP the transaction: ").lower()
        if enter == 'x':
            break
        if enter in product:
            if enter in trans_prod:
                trans_prod[enter] += 1
                trans_logs[enter] += 1
            else:
                trans_prod[enter] = 1
                trans_logs[enter] = 1
            total += product[enter]
        elif enter not in product:
            print("The Product does NOT Exist!")
    print(f"""
{"=" * 26}
Total Cost: {total:.2f}

Transaction Details:

{formatted_time}

Items and Prices:""")
    for prod, count in trans_prod.items():
        print(f"\t\t{prod} (Quantity: {count}) - {product[prod] * count:.2f} (Price: {product[prod]})")
    print(f"Total Cost: {total:.2f}")

#TRANSACTION LOGS
def logs():
    print(f"""All Transaction Logs:

{formatted_time}

Items and Prices: """)
    total = 0
    for prod, count in trans_logs.items():
        print(f"\t\t{prod} (Quantity: {count}) - {product[prod] * count:.2f} (Price: {product[prod]})")
        total += product[prod] * count
    print(f"Total Cost: {total:.2f}")
    print("THANKYOU FOR USING THIS POS - PROGRAM!")

looper = True
while looper:
    task = format()
    if task == 'A':
        add()
    elif task == 'V':
        view()
    elif task == 'D':
        delete()
    elif task == 'T':
        transact()
    else:
        logs()
        looper = False
