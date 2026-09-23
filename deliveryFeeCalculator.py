# – Read two related values from the user, each with its own input call.
# – Validate each value on its own, before either is used in a decision. A bad first value must not stop the second
# from being validated.
# – Reject a value that is outside a sensible range for that value, and say what the sensible range is.
# – Combine the two validated values, using chained comparisons and Boolean operators, or nested and chained if,
# elif and else, so that the outcome for the second value depends on what the first one was.
# – Produce at least four distinct outcomes, not merely four print statements that say almost the same thing.
# – Print a clearly formatted result using an f-string that reports both values and the outcome together.
# – Use variable names that describe what they hold, and comments marking the sections of your program:
# reading and validating each value, and combining them

order_total = float(input('Enter the order total in dollars: E.g. 25'))
delivery_date = input('Enter the delivery day (e.g. Saturday):')

if not (0 <= order_total <= 1000):
    print('Order total must be between 0 and 1000')

if delivery_date not in ['saturday', 'sunday']:
    print('Delivery date must be Saturday or Sunday')
    exit()

if delivery_date == 'saturday':
    surcharge = 2.99
elif delivery_date == 'sunday':
    surcharge = 1.99
elif delivery_date in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    surcharge = 0.99

if order_total < 50:
    delivery_fee = 9.99*surcharge
elif order_total < 100:
    delivery_fee = 7.99*surcharge
elif order_total < 250:
    delivery_fee = 5.99*surcharge
else:
    print('Order total must be between 0 and 1000 and delivery date must be Saturday or Sunday')
    exit()


print(f'Order: ${order_total} on {delivery_date }. Delivery fee: ${delivery_fee}. Weekend small-order surcharge applies.')