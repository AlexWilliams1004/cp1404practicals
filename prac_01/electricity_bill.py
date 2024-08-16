"""
Electricity Bill Estimator - CP1404 Practicals

    - Alex Williams 16.08.2024 -

"""
cents_per_kilowatt_hour = int(input("Enter cents per kWh: "))
daily_use_kilowatt_hour = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
estimated_bill = cents_per_kilowatt_hour * daily_use_kilowatt_hour * number_of_billing_days / 100
print(f"Estimated bill: {estimated_bill:.2f}")
