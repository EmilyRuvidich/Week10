# Author: Emily Ruvidich
# Creation Date: 05/18/2022
# The following program will ask the user to specify a filename to open and write to it.

import os #import the OS library 

#######################
def displayIntro():
#######################        

    print("Welcome to the reading/writing a file program.\n")

#######################
def requestMainInput():
#######################
        
    mainChoice = ''
    
    while mainChoice != '1' and mainChoice != '2':
            
        print('Please enter the number for the desired action.\n')
        print('1 - Open a file for reading/writing')
        print('2 - Exit Program\n')
        
        mainChoice = input()

    return mainChoice

###########################
def requestDirectoryName():
###########################
        
    dirName = None

    #Directory name entered must have a value.
    
    while not dirName:

        dirName = input("Enter the name of the directory for which you would like to save a file: ")
        
    if not os.path.isdir(dirName): #if directory does not exist
       print('This directory does not exist and will now be created')
       os.makedirs(dirName)
    
    return dirName

###########################
def requestFileName():
###########################
        
    fileName = None

    #File name entered must have a value.
    
    while not fileName:

        fileName = input("Enter the name of the file that you would like to save: ")
        
    return fileName

###########################
def requestPersonName():
###########################
        
    personName = None

    #Person name entered must have a value.
    
    while not personName:

        personName = input("Enter your name: ")
        
    return personName.replace(",","")

###########################
def requestPersonAddress():
###########################
        
    personAddress = None

    #Person address entered must have a value.
    
    while not personAddress:

        personAddress = input("Enter your address: ")
        
    return personAddress.replace(",","")

###########################
def requestPersonPhone():
###########################
        
    personPhone = None

    #Person phone entered must have a value.
    
    while not personPhone:

        personPhone = input("Enter your phone number: ")
        
    return personPhone.replace(",","")

###########################
def writeData(pFullFileName,
              pPersonName,
              pPersonAddress,
              pPersonPhone):
###########################

    #open the file requested by the user for writing
    fullText = pPersonName + "," + pPersonAddress + "," + pPersonPhone
    
    with open(pFullFileName, 'w') as fileHandle: # w for writing
        fileHandle.write(fullText) # write out text from a variable

###########################
def printData(pFullFileName):
###########################

    #print the data entered by the user 
    labelValue = ''
    #open the file entered by the user for reading 
    with open(pFullFileName, 'r') as fileHandle:# r for reading
        data = fileHandle.read() # read into a variable print(data)
    
    data = data.split(',') #this creates a python list that we can read 
    
    #search the list and print each item in the list with an appropriate heading 
    for x in range(len(data)):
        if x == 0:
           labelValue = '\nName: '
        else:
           if x == 1:
              labelValue = 'Address: '
           else:
              labelValue = 'Phone: '
           
        print(labelValue + data[x])
    
############    
def main():
############        

    bSlash = '\\'
    displayIntro()
    
    mainChoice = requestMainInput()

    if mainChoice == '1':
       dirName       = requestDirectoryName()
       fileName      = requestFileName()
       fullFileName  = dirName + bSlash + fileName
       personName    = requestPersonName()
       personAddress = requestPersonAddress()
       personPhone   = requestPersonPhone()
       
       writeData(fullFileName,
                 personName,
                 personAddress,
                 personPhone)
       printData(fullFileName)
    else:
       print('Exited program')

main()

