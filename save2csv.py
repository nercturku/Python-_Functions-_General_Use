
import os.path

# Example of the arguments you have to pass in order to use the save_csv function below
fileName = 'giveName.csv'
columnName = ["datetime", "var1", "var2", "var3", "var4"]
data = ['1970 Jan 01 00:00:00', 1, 2, 3, 4]

def save_csv(fileName:str, columnName:list, dataList:list):
    """
    Save a list containing several items to CSV file. The number of items on the list, must match the number of columns in columnName.
    If the file doesnot exist, one with will be created in the current working directory. 
    If the file exist, data will be appended to the file.\n
    Arguments: File's name. A string.\n
                       Columns name. A list of names.\n
                       Data values. A list of values. [datetime, val1, val2, val3]
    Returns. Nothing
    """

    # Checking if the file already exists or not
    path = './' + fileName
    check_file = os.path.isfile(path)
    
    #If file does not exist:
    if check_file == False:
        with open(fileName, 'w') as file:
            #Convert the columns name list to a single string so it can be saved to a csv file
            headers2string = ",".join(columnName)
            file.write(headers2string + "\n")
            file.close()
    
    # Files exists and data can be addded:
    with open(fileName, 'a') as file:
        data2string = ",".join(map(str, dataList))
        #file.write('This is my first csv file. This must be a string to allow the writing')
        file.write(data2string + "\n")


# Activate the line below to test the function with the data from lines 5,6,7
#save_csv(fileName, columnName, data)