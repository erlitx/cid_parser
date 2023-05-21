# Open the file in read mode
with open('output3.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()
    
    # Convert the content to a list using eval
    my_list = eval(content)
    
    # Get the length of the list
    list_length = len(my_list)
    
    # Print the length of the list
    print(list_length)