"""Problem Statement : Write a function which reads data from a json file (attached) and transform the given data file json into
a new one which has keys and their corresponding end values only.
Data File Description : There are n keys and corresponding n values in the json file. Assume the keys and values are of URLs."""

import json

# get to the end till the URL that is not a key and store that URL as the value in the result_dict for all the URLs that have been seen in the recursive calls
def get_end(url_data_dict, result_dict, current_key):
    if(result_dict.get(current_key)==None): # Check if 'current_key'(URL) is already present in the 'result_dict', proceed only if not present
        next_key = url_data_dict.get(current_key) # Get the next key (URL) which is the value of the 'current_key' in 'url_data_dict'
        if(next_key != None): # if the next key is present, i.e, current_key is not an end URL   
            result_dict[current_key] =  '' # THIS LINE ENSURES WE DO NOT LOOP IN CYCLE, ALL THE URLs IN THE CYCLE AND THOSE URLs THAT REACH THE CYCLE WILL BE MAPPED TO EMPTY STRING
            result_dict[current_key] = get_end(url_data_dict, result_dict, next_key) # recursive call with next key; store the returned value which is an end URL as the value in the 'result_dict' for the 'current_key'
            return result_dict[current_key] # return the end URL
        return current_key # return the 'current_key' as it is an end URL
    return result_dict.get(current_key) # The 'current_key'(URL) is already present in the 'result_dict', return that value(URL)

# this is the first function that is called and it creates the desired output file given the input and output file names
def convert(input_file, output_file):
    result_dict = {} # result_dict will store the converted output where each URL is mapped to it's ending URL based on the input file
    with open(input_file,'r') as url_data_file: # open the json file, 'with' key word handles the proper closing of the opened file
        url_data_dict = json.load(url_data_file) # load the json file as dictionary
        for key in url_data_dict: # For each key URL in the 'url_data_dict' ...
              if(result_dict.get(key)==None): # ... if the key URL is not yet present in the 'result_dict', redundant line as we are checking this in 'get_end'
                  get_end(url_data_dict,result_dict, key) #... call the 'get_end' function which gets and stores the end URL for the key URL in 'result_dict'

    # create the output json file
    with open(output_file,'w') as converted_file:
        json.dump(result_dict,converted_file, indent=4)


#START FROM THIS LINE
convert("datafile.json","output.json")

"""The time-complexity of this is O('n') where 'n' is the number of keys in the input json files; We traverse the keys (URLS) only once and check whether the key has been processed already (i.e, present in the 'result_dict'). If not, we call the 'get_end' function which traverses till the end URL or till the URL that has already been processed and return it's ending URL. In this way each key (URL) is processed only once with 'get_end' function. Hence the time-complexity is O('n') where 'n' is the number of keys.""" 
