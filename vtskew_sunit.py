# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 21:11:35 2021

@author: happy
"""

#!/usr/bin/python3

import argparse


def arg_parser():
    '''
    A function to parse the command line arguments.
    '''
    parser = argparse.ArgumentParser(description='Parses top_ist_bfm.vh file and looks for any plus or valueplus args.')
    parser.add_argument('--file1', '-f1', type=str, help='provide complete path or relative path to file 1')
    parser.add_argument('--file2', '-f2', type=str, help='provide complete path or relative path to file 2')
    args = parser.parse_args()
    return args


def make_pairs(file_path):
    '''This function parses file to create key value pairs'''
    final_pairs={}
    with open(file_path, 'r') as ptr:
        i = 0
        for lines in ptr:
            if i==0:
                columns = lines.split()
                i+=1
                continue
            line_temp = lines.split()
            for j in range(len(columns)-2):
               final_pairs[str(line_temp[0])+'_'+str(line_temp[1])+'_'+columns[j+2]] = line_temp[j+2]

    return final_pairs


def missing_keys(dict_one, dict_two):
    pass


def compare_dict(dict_one, dict_two):
    '''This function compares the two dictionaries for any missing keys or value mismatches for common keys'''
    #A small function that prints missing keys. Didn't need it..
    dict_one_missing_keys=[]
    dict_two_missing_keys=[]

    #This list captures the mismatching key_value pairs in the two dictionaries.
    mismatching_keys=[]

    for key in dict_one:
        if key in dict_two:
            if dict_one[key] != dict_two[key]:
                mismatching_keys.append(key)
        else:
            dict_two_missing_keys.append(key)
            
    for key in dict_two:
        if key not in dict_one:
            dict_one_missing_keys.append(key)

    return mismatching_keys, dict_one_missing_keys, dict_two_missing_keys
    

if __name__=='__main__':
    args = arg_parser() 
    #getting first dictionary
 #   dict_one=make_pairs(r'C:\Users\happy\Documents\derate\vt\data.txt')
  #  dict_two=make_pairs(r'C:\Users\happy\Documents\derate\vt\data1.txt')
    dict_one=make_pairs(args.file1)
    dict_two=make_pairs(args.file2)
    #compare two dicts for missing/mismatches
    mismatching_keys, dict_one_missing_keys, dict_two_missing_keys = compare_dict(dict_one,dict_two)
    print("mismatching key_value pairs:\n")
    print(mismatching_keys)
    print("missing keys in dictionaries:\n")
    print(dict_one_missing_keys)
    print(dict_two_missing_keys)
