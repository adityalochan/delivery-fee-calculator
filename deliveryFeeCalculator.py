order_total = float(input('Enter the order total in dollars: E.g. 25 :: '))
delivery_date = input('Enter the delivery day (e.g. Saturday) :: ').lower()

if not (0 <= order_total <= 1000):
    print('Order total must be between 0 and 1000')

if delivery_date not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']:
    print('Delivery date must be correct day of the week (e.g. Saturday)')
    exit()

if delivery_date == 'saturday':
    surcharge = 2.99
elif delivery_date == 'sunday':
    surcharge = 1.99
elif delivery_date in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    surcharge = 0.99

if order_total < 50:
    delivery_fee = 9.99+surcharge
elif order_total < 100:
    delivery_fee = 7.99+surcharge
elif order_total < 250:
    delivery_fee = 5.99+surcharge
elif order_total < 500:
    delivery_fee = 3.99+surcharge
elif order_total < 1001:
    delivery_fee = 1.99+surcharge
else:
    print('Order total must be between 0 and 1000 and delivery date must be Saturday or Sunday')
    exit()

delivery_fee = round(delivery_fee, 2)

print(f'Order: ${order_total} on {delivery_date}. Delivery fee: ${delivery_fee}.')