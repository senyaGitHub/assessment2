import csv

TransactionID = 1
CustomerID = 2
StoreLocation = 3
ProductCategory = 4
ProductID = 5
Quantity = 6
UnitPrice = 7
TransactionDate = 8
PaymentMethod = 9
DiscountApplied = 10
CustomerSatisfaction = 11
TotalPrice = 12

def load_data(path):
    with open(path, newline='') as csvfile:
        record = list(csv.reader(csvfile))
    return record
