# Title: ML Final
# Kiarash Jalali
# 2020-11-30
# Page that just contains calcuations needed for the project

# This function just contains a dictionary that goes thru
# every element in a list given to it and puts them within this range
def precentage(lst):
    
    predic_range = {'0-10':0, '10-20':0, '20-30':0, 
                    '30-40':0, '40-50':0, '50-60':0, 
                    '60-70':0, '70-80':0, '80-90':0, 
                    '90-100':0, '100 or more':0
                    }
    
    for x in lst:
    
        if 0 <= x < 10:
            predic_range['0-10'] += 1
    
        elif 10 <= x < 20:
            predic_range['10-20'] += 1

        elif 20 <= x < 30:
            predic_range['20-30'] += 1

        elif 30 <= x < 40:
            predic_range['30-40'] += 1

        elif 40 <= x < 50:
            predic_range['40-50'] += 1

        elif 50 <= x < 60:
            predic_range['40-50'] += 1
        
        elif 60 <= x < 70:
            predic_range['60-70'] += 1
        
        elif 70 <= x < 80:
            predic_range['70-80'] += 1

        elif 80 <= x < 90:
            predic_range['80-90'] += 1
        
        elif 90 <= x < 100:
            predic_range['90-100'] += 1
        elif 100<= x:
            predic_range['100 or more'] += 1
    
    return predic_range

"""
    Function that takes two lists, one the actual value
    And one for the outcome value, it puts it into a formula
    to get percentage error

"""

def percenterror(actual, outcome):
    final = []
    # The zip function allows us to go thru two lists
    # at the same time so for example if we have
    # Lista [1,2,3] and listb = [4,5,6]
    # The zip function creates a tuple and give us back
    # ((1,4) (2,5) (3,6)) which makes it eaiser for us 
    # To do anything with the data
    
    for (x, y) in zip(actual, outcome):
    
        if x != 0:
            calculate = abs(x - y) / x
            calc = calculate * 100
            final.append(calc)
    
        else:
            continue
        
    return final
    
