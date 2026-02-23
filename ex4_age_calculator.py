from datetime import datetime
print("\n--- BONUS: Exact Age Calculation ---")
birth_day = int(input("Enter your birth day (DD): "))
birth_month = int(input("Enter your birth month (MM): "))
birth_year_full = int(input("Enter your birth year (YYYY): "))
today = datetime.now()
birth_date = datetime(birth_year_full, birth_month, birth_day)
difference = today - birth_date
exact_days = difference.days
exact_years = exact_days // 365
exact_months = exact_years * 12
exact_hours = exact_days * 24
exact_minutes = exact_hours * 60
print("Exact age in years:", exact_years)
print("Exact age in days:", exact_days)
print("Exact age in hours:", exact_hours)
print("Exact age in minutes:", exact_minutes)
print("Exact age in months:", exact_months)
