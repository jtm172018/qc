# -*- coding: utf-8 -*-
"""
chanchal pocv comparison

This is a temporary script 
"""
import os
#print (os.getcwd())
import filecmp
import fnmatch
import sys
import xlsxwriter 
#dir1=sys.argv[1]
#dir2=sys.argv[2]
# print(dir1)
dir1="C:/Users/happy/Documents/pocv"
dir2="C:/Users/happy/Documents/pocv1"
# print(dir2)
c = filecmp.dircmp(dir1,dir2)
#print(c)
# def report_recursive(dcmp):
#     for name in dcmp.diff_files:
#         print("DIFF file %s found in %s and %s" % (name, 
#             dcmp.left, dcmp.right))
#     for name in dcmp.left_only:
#         print("ONLY LEFT file %s found in %s" % (name, dcmp.left))
#     for name in dcmp.right_only:
#         print("ONLY RIGHT file %s found in %s" % (name, dcmp.right))
#     for sub_dcmp in dcmp.subdirs.values():
#         print_diff_files(sub_dcmp)
#c.report()
#report_recursive(c)
g=(c.common_files)
common=fnmatch.filter(g,"*.txt")
#print(g)
#common = glob("*.txt")
#print(c.diff_files)
#print (common[0])
for w in common:
    

    d = {}
    d1 = {}
    m = ''
    m1 = ''
    n =''
    n1 = ''
    f = open(dir1+"/"+ w, "r")
    f1 = open(dir2+"/"+w, "r")
    #print(f.read())
    for line in f:
        if line == "\n": 
            pass
        else :
            (key,value) = line.split(': ')
            if key == 'version':
                m = m +(value.rstrip())
            if key == 'ocvm_type':
                m= m+"_"+(value.rstrip())
            if key == 'rf_type':
                m= m+"_"+(value.rstrip())
            if key == 'delay_type':
                m= m+"_"+(value.rstrip())
            if key == 'derate_type':
                m= m+"_"+(value.rstrip())
            if key == 'object_spec':
                m= m+"_"+(value.rstrip())
            if key == 'coefficient':
                o = ''
                o = m
                n = value.rstrip()
                d[(o)]= n
                m=''
                
    for line in f1:
        if line == "\n": 
            pass
        else :
            (key,value) = line.split(': ')
            if key == 'version':
                m1 = m1 +(value.rstrip())
            if key == 'ocvm_type':
                m1= m1+"_"+(value.rstrip())
            if key == 'rf_type':
                m1= m1+"_"+(value.rstrip())
            if key == 'delay_type':
                m1= m1+"_"+(value.rstrip())
            if key == 'derate_type':
                m1= m1+"_"+(value.rstrip())
            if key == 'object_spec':
                m1= m1+"_"+(value.rstrip())
            if key == 'coefficient':
                o = ''
                o = m1
                n1 = value.rstrip()
                d1[(o)]= n1
                m1=''
        
        # print (key)
    #print (m)
        #d[(key)]=value
    #print(d1)
    print(w)
    print('missing in new:')
    for key in d.keys():
        if not key in d1:  
            # Printing difference in
            # keys in two dictionary        
            print((key) +','+ d[key] )
    #print (d['version'])
    print('missing in old:')
    for key in d1.keys():
        if not key in d:
            # Printing difference in
            # keys in two dictionary  
            print((key) +','+ d1[key] )
    
    common_pairs = dict()
    for key in d:
        if (key in d1 and d[key] == d1[key]):
            common_pairs[key] = d[key]
    print('cofficient match:'+ str(len(common_pairs)))
    for key in common_pairs:
        print(key +','+ common_pairs[key]+','+d1[key])
    
    mismatch_pairs = dict()
    for key in d:
        if (key in d1 and d[key] != d1[key]):
    
    
            mismatch_pairs[key] = d[key]
    #print(mismatch_pairs) 
    print('cofficient mismatch:'+ str(len(mismatch_pairs)))
    for key in mismatch_pairs:
        print(key +','+ mismatch_pairs[key]+','+d1[key])
    #print(d[key + d1[key]])
    print("")
    f.close()
    f1.close()

