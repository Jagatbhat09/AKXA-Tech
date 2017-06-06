import argparse
import os.path
import Image
from pytesseract import image_to_string

#global_variables
input_file = ""
output_file = ""

#------------------------------------------------------------------------------#
### Generic Function to be written here
"""
def contains_something(value,message) :
functionality : checks whether the variable "value" contains some value which is very nesserary
if does not contain any value displays message and exists
Input: value of type string
output: displays "message"
"""
def contains_something(value,message) :
    if value :
        return value
    else :
        print message,"\nHence Exiting" 
        exit()

"""
def check_file_exists(filename) :
checks whether the file exists at given path returns the control on success
exists if file is not present at the required path
"""
def check_file_exists(filename) :
    if os.path.isfile(filename) :
        return
    else :
        print "File Does not exist : %s \nHence Exiting"%filename
        exit()

#------------------------------------------------------------------------------#

def image_to_text() :
    text_value = image_to_string(Image.open(input_file), lang='eng')
    print text_value

#------------------------------------------------------------------------------#
### Anything parsing of arguments goes under this section
"""
Functionality: validates command line arguments continues if all arguments are correct or exits...
"""
def validate_arguments(arguments) :
    global input_file,output_file
    input_file = contains_something(arguments.input_file,"no Input : Input File")
    output_file = contains_something(arguments.output_file,"no Input : Output File")
    check_file_exists(input_file)
    print "validation of arguments complete"
    return

def initialize_parser_argument(arg_parser) :
    arg_parser.add_argument("-i", "--input_file" ,  type=str, help="complete path to input file")
    arg_parser.add_argument("-o", "--output_file",  type=str, help="complete path to output file")
    validate_arguments(arg_parser.parse_args())

def parse_arguments() :
    arg_parser = argparse.ArgumentParser()
    initialize_parser_argument(arg_parser)
    arguments = arg_parser.parse_args()

#------------------------------------------------------------------------------#

def main() :
    parse_arguments()
    image_to_text()

if __name__ == '__main__' :
    main()
