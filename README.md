# delivery-fee-calculator
A delivery fee calculator that which decides the delivery fee based on order total and days of the week

## Setup
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt

## Run
python deliveryFeeCalculator.py

## Example
Enter the order total in dollars: 25
Enter the delivery day (e.g. Saturday): saturday
Order: $25.00 on Saturday. Delivery fee: $6.99. Weekend small-order surcharge applies.
## Known limitations
Anything you are aware of that does not work, or that you would improve
with more time.