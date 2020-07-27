#!usr/bin/env python3

'''
Program will open file stores query sequence ID  and query length (store in dict/list)

'''

import re                                                                                                

def grab_id_length(f):     
	#created variables for string of query_ID and query_Length
        query_id = ""
        query_length = ""
        unfilled = True
        while(unfilled):
                for line in  f:
                        if query_id and query_length:
                                unfilled = False
                                break
                        if line.startswith("Length="):
                                query_length = line
                        if line.startswith("Query="):
                                query_id = line


                print(query_id + query_length)

def main():

        f = open("example_blast.txt" , "r+")
        #print out on commandline with QueryID and QueryLength
        #grab_id_length(f)

        #file parsing sort first ten with accession between first pipes ||
        #Format : Alignment #1: Accession = ref|XM_005094338.1| (Length = 2377, Score = 1098)
        #use regex


        grab_id_length(f)

        ascn_list = []
        length_list = []
        score_list = []
        length =""
        for line in f:

                if line.startswith('>'):
                        info = line.split()
                        ascn = info[0]
                        ascn = ascn.split('>')
                        ascn_list.append(ascn[1])
                        continue
                if line.startswith('Length='):
                        length_list.append(line.strip())
                else:
                        if line.startswith(' Score ='):
                                info = line.split('bits')
                                score = info[0]
                                score_list.append(score.strip())
                        continue




                #print only ten out
        for x in range(10):
                print("Alignment #{0}: Acession = {1} ({2} , {3})".format(x+1,ascn_list[x],length_list[x],score_list[x]))
if __name__ =='__main__':
        main()