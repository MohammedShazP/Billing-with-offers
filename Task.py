""" Product name    Price
    product A        $20
    product B        $40
    product C        $50
"""

product_list = ["Product A", "Product B", "Product C"]
sub_total_list = []


# function to find sub total
def sub_total(q_list, p_list):
    s_list = []
    base = 0
    for i in range(3):
        amount = q_list[i] * p_list[i]
        total = amount + base
        s_list.append(total)
        base = total
    return s_list


# function to find shipping and wrapping fee
def shipping_and_wrapping(q_list, w_list):
    wrap_fee = 1
    shipping_fee = 5
    w_charge = []
    t_q = sum(q_list)
    shipping_charge = (t_q / 10) * shipping_fee
    for ind, ele in enumerate(w_list):
        if ele == 1:
            charge = q_list[ind] * wrap_fee
            w_charge.append(charge)
    return sum(w_charge), shipping_charge


total_after_discount = []  # price after discount
discountable_price = []  # Total discount amount
name_and_amount = dict()  # name of discount package and total amount


# function for flat 10 discount package
def flat_10_discount(q_list, p_list):
    q = q_list
    p = p_list
    discount_price = 10
    total = []
    for ind, ele in enumerate(q):
        price = ele * p[ind]
        total.append(price)
    total_amount = sum(total)
    if total_amount > 200:
        after_discount_total = total_amount - discount_price
        discountable_price.append(discount_price)
    else:
        after_discount_total = total_amount
    final_price1 = int(after_discount_total)
    total_after_discount.append(final_price1)
    name_and_amount[final_price1] = 'Flat 10 Discount'


# function for bulk 5 discount
def bulk_5_discount(q_list, p_list):
    q = q_list
    p = p_list
    total = []
    discount_list = []
    for ind, ele in enumerate(q):
        if ele > 10:
            price = ele * p[ind]
            discount_fee = price * 0.05
            total_price = price - discount_fee
            total.append(total_price)
            discount_list.append(discount_fee)
        else:
            price = ele * p[ind]
            total.append(price)
    total_discount = int(sum(discount_list))
    final_price2 = int(sum(total))
    total_after_discount.append(final_price2)
    discountable_price.append(total_discount)
    name_and_amount[final_price2] = 'Bulk 5 discount'


# function for bulk 10 discount
def bulk_10_discount(q_list, p_list):
    q = q_list
    p = p_list
    total = []
    for ind, ele in enumerate(q):
        price = ele * p[ind]
        total.append(price)
    total_price = sum(total)
    discount_amt = total_price * 0.1
    after_discount = total_price - discount_amt
    final_price3 = int(after_discount)
    total_after_discount.append(final_price3)
    discountable_price.append(int(discount_amt))
    name_and_amount[final_price3] = 'Bulk 10 discount'


# function for tiered 50 discount
def tiered_50_discount(q_list, p_list):
    q = q_list
    p = p_list
    total = []
    discount_list = []
    for ind, ele in enumerate(q):
        if ele > 15:
            dis_q = ele - 15
            without_discount = 15 * p[ind]
            discount = (dis_q * p[ind]) * 0.5
            discount_list.append(discount)
            total.append(discount + without_discount)
        else:
            price = ele * p[ind]
            total.append(price)
    final_price4 = int(sum(total))
    total_after_discount.append(final_price4)
    discountable_price.append(int(sum(discount_list)))
    name_and_amount[final_price4] = 'Tiered 50 Discount'


Quantity_list = []         # list for quantity input from user
price_list = [20, 40, 50]  # price list of the product
wrap_list = []             # list to check wrap or not
ch = "A"
while len(wrap_list) <= 2:
    print("Enter the quantity of Product", ch, " and press 1 wrap the product or 0 for not wrap")
    qty, wrap = input().split()
    if int(wrap) <= 1:
        wrap_list.append(int(wrap))
        Quantity_list.append(int(qty))
        ch = chr(ord(ch) + 1)
    else:
        print("Enter 1 or 0")
total_Quantity = sum(Quantity_list)  # finding the total quantity needed
subtotal = max(sub_total(Quantity_list, price_list))  # function called and returns sub total

total_wrap_fee, total_ship_fee = shipping_and_wrapping(Quantity_list, wrap_list)  # function called and ship and wrap
# fee returned

flat_10_discount(Quantity_list, price_list) # function called

# function called after checking the condition
for i in Quantity_list:
    if i > 10:
        bulk_5_discount(Quantity_list, price_list)
        break

# two functions called after checking the conditions
if total_Quantity > 20:
    bulk_10_discount(Quantity_list, price_list)
    for i in Quantity_list:
        if total_Quantity > 30 and i > 15:
            tiered_50_discount(Quantity_list, price_list)
            break

lowest = min(total_after_discount)
for i in name_and_amount.keys():
    if i == lowest:
        discount_app = name_and_amount[i]
discount_name = discount_app
discount_amount = max(discountable_price)
grand_total = subtotal + total_ship_fee + total_wrap_fee - discount_amount
print("\033[1m" + "Product Name \t Quantity \t Total Amount" + "\033[0m")
tab = "\t"
for i in range(3):
    print(product_list[i], tab, Quantity_list[i], tab * 2, "$", Quantity_list[i] * price_list[i])
print()
print("\033[1m" + "Sub Total" + "\033[0m", tab * 3, "$", subtotal)
print("\033[1m" + "Discount Applied" + "\033[0m", tab * 2, discount_name)
print("\033[1m" + "Discount Amount" + "\033[0m", tab * 2, "$", discount_amount)
print("\033[1m" + "Shipping Fee" + "\033[0m", tab * 3, "$", total_ship_fee)
print("\033[1m" + "Gift Wrap Fee" + "\033[0m", tab * 3, "$", total_wrap_fee)
print("\033[1m" + "Total" + "\033[0m", tab * 4, "$", grand_total)
