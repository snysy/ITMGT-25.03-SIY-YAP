#Products Dictionary
products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

#Problem 1: Product Information Lookup
def get_product(code):
    #i = print("get_product: ", products[code])
    return products[code]

get_product("espresso")

#Problem 2: Product Property Lookup
def get_property(code, property):
    coffeedict = products[code]
    return coffeedict[property]

get_property("espresso", "price")

#Problem 3: Point-of-Sale Terminal
def main():
    order_dict = {}
    value = input("Enter order: ")
    order = value.split(",", 1)

    item_dict = {}
    item_dict["quantity"] = order[1]
    item_dict["subtotal"] = int(get_property(order[0], "price")) * int(order[1])
    order_dict[order[0]] = item_dict

    while value != "/":
        value = input("Enter more order: ")

        if value != "/":
            order = value.split(",", 1)
            print("order: ", order)
            print("orderdict1: ", order_dict)
            if order[0] in order_dict:
                existing_order = order_dict[order[0]]
                print("existing_order: ", existing_order)
                existing_order["quantity"] = int(existing_order["quantity"]) + int(order[1])
                current_total = int(get_property(order[0], "price")) * int(order[1])
                existing_order["subtotal"]  = current_total + existing_order["subtotal"]
                order_dict[order[0]] = existing_order
            else:
                item_dict2 = {}
                item_dict2["quantity"] = order[1]
                item_dict2["subtotal"] = int(get_property(order[0], "price")) * int(order[1])
                order_dict[order[0]] = item_dict2
            print("orderdict: ", order_dict)

    f = open("receipt.txt", "w")
    f.write("CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n")
    total = 0
    for code in order_dict.keys():
        name = get_property(code, "name")
        quantity = order_dict[code].get("quantity")
        subtotal = order_dict[code].get("subtotal")
        total = total + subtotal
        f.write(code + "\t\t\t" + name + "\t\t\t" + str(quantity) + "\t\t\t" + str(subtotal) + "\n")

    f.write("\n")
    f.write("Total:\t\t\t\t\t\t\t\t\t\t" + str(total))
    f.close()

main()
