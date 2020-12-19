# Title: ML Final
# Kiarash Jalali
# 2020-11-30
# Page that processes the data, this data will be used by the
# Model.py page


open_file = input('What File do you wish to use? ')

if '.csv' not in open_file:
    print('\nOps! Please provide a .csv file :)')
    print('\nPlease run me again once you have a csv file')
    print('Goodbye')
    quit()

user_input_data = input('What are colums for the input (use \',\'?) ')
list_input_data = user_input_data.split(',')
input_data = list(map(int, list_input_data))

output_data = input('Which column for output? ')
output_data = int(output_data)


"""
    The logic for the following four functions are very
    similar so I only went in-depth for the first function
    since I would be just repeating myself and it would 
    ruin the purpose of comments

"""



def train_input(lst):
    """
        The reason we first calculate the number of rows
        in the csv file is because we don't want to go thru
        all the items in the list we only want to have 
        80% of the items the remaining 20% is for our model to 
        test

        Also the input this function is taking is the input that
        our user gives which is the colums we want to use for our 
        input.
    """

    # From line 35 to 41 we just calculate the number of rows
    file = open(open_file)
    file.readline()

    rows = 0
    for i in file:
        rows += 1
    approx = rows * 0.8 
    # From line 35 to 41 we just calculate the number of rows
    """
        For some reason I have to open the file again to be
        able to loop thru the list again
    """

    file = open(open_file)
    file.readline()

    # List to hold the final inputs
    final_inputs = []

    # Tally to keep track of where we are in the file
    count = 0

    """
        In the following lines of code I basicly go thru the rows
        and check if the colum the pointer is on is the colum the user
        wants to use for input

    """
    
    for row in file:

        item = row.strip('\n').split(',')
        items = []
    
        for i in range(len(lst)):
            wanted = float(item[lst[i]])
            items.append(wanted)
        final_inputs.append(items)
        count += 1

    # If we have gone thru 80% of the list we dont need to go thru the following 20%
        if count == approx:
            break
    return final_inputs

def test_input(lst):

    """
        I do the same thing I did for the function above but
        the diffrence is that I only go thru the remaining 20% of the
        items i didnt go thru for the training input

    """
    
    file = open(open_file)
    file.readline()

    rows = 0
    for i in file:
        rows += 1
    approx = rows * 0.8 

    file = open(open_file)
    file.readline()

    final_outputs = []
    count = 0

    # The same logic used for the function above but it only goes thru 
    # the bottom 20% of the file
    for row in file:
        item = row.strip('\n').split(',')
        count += 1
        if count > approx:
            items = []
            for i in range(len(lst)):
                wanted = float(item[lst[i]])
                items.append(wanted)
            final_outputs.append(items)
    return final_outputs


# Same logic as the train input but we only look for one colum
def train_output(lst):
    file = open(open_file)
    file.readline()

    rows = 0
    for i in file:
        rows += 1
    approx = rows * 0.8 

    file = open(open_file)
    file.readline()

    final_outputs = []
    count = 0

    for row in file:
        item = row.strip('\n').split(',')
        wanted = float(item[lst])
        final_outputs.append(wanted)
        count += 1
        if count == approx:
            break
    return final_outputs


# Same as test input 
def test_output(lst):
    file = open(open_file)
    file.readline()

    rows = 0
    for i in file:
        rows += 1
    approx = rows * 0.8 

    file = open(open_file)
    file.readline()

    final_output = []
    count = 0

    for row in file:
        item = row.strip('\n').split(',')
        count += 1

        if count > approx:
            wanted = float(item[lst])
            final_output.append(wanted)
    return final_output
