"""
Electricity Bill Estimator - CP1404 Practicals

    - Alex Williams 16.08.2024 -

"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff = input("Which tariff? 11 or 31: ")
if tariff == "11":
    cents_per_kilowatt_hour = TARIFF_11
else:
    cents_per_kilowatt_hour = TARIFF_31
daily_use_kilowatt_hour = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
estimated_bill = cents_per_kilowatt_hour * daily_use_kilowatt_hour * number_of_billing_days
print(f"Estimated bill: {estimated_bill:.2f}")
