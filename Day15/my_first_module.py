# Solution to Practice Problems Day 15
# my_first_module.py
def calculate_tip(cost, tip_percent):
    return cost * (tip_percent / 100)

def split_bill(cost, tip, num_people):
    return (cost + tip) / num_people