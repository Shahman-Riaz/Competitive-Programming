def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost*tip_percent)/100
    tax = (meal_cost*tax_percent)/100
    print(round(meal_cost + tip + tax))
    
    
meal_cost = float(input().strip())
tip_percent = int(input().strip())
tax_percent = int(input().strip())
solve(meal_cost, tip_percent, tax_percent)