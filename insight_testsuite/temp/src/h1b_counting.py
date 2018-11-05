"""
@author: chaopei
"""

import sys
import csv

def Count_h1b(Input_File,Occu_file,State_file):
    
    
    #make file path string
    Input_File=str(Input_File)
    Occu_file=str(Occu_file)
    State_file=str(State_file)
    
    
    with open(Input_File, 'r') as csvfile:      
        reader=csv.DictReader(csvfile,delimiter=";")             #read input
        
        #get the number of all certified cases                
        certified_num=0
        
        #a dictionary of with occupations as keys are values as their frequencies
        occu_dict={}
        
        #a dictionary of soc codes and its corresponding names for easier access later
        code_to_name={}
        
        #a dictionary of with States as keys are values as their frequencies
        st_dict={}        
        
        for row in reader:
            
            #add the certified cases to one list
            if row["CASE_STATUS"]=="CERTIFIED":
                certified_num+=1
                
                #counting frequencies of certified occupations
                if row["SOC_CODE"] in occu_dict: 
                    occu_dict[row["SOC_CODE"]]+=1
                    
                else:
                    
                    #set the unrecorded occupation frequency to be 1
                    occu_dict[row["SOC_CODE"]]=1
                    
                    #get teh corresponding occupation name form soc codes
                    code_to_name[row["SOC_CODE"]]=row["JOB_TITLE"]
                    
            
                #counting frequencies of certified States
                if row["WORKSITE_STATE"] in st_dict: 
                    st_dict[row["WORKSITE_STATE"]]+=1
                    
                else:

                    #set the unrecorded States frequency to be 1
                    st_dict[row["WORKSITE_STATE"]]=1        
                    

    #a list to sort occupations by frequencies
    top_occu=[]            
    for key, value in sorted(occu_dict.items(), key=lambda item: (item[1], item[0])):
        top_occu.append([code_to_name[key],value,"{0:.0%}".format(value/certified_num)]) 
        
    #from the most to the least
    top_occu.reverse()
    
    #get the top 10 occupations
    top_10_occu=top_occu[:10]
    
    #a list to sort states by frequencies
    top_st=[]            
    for key, value in sorted(st_dict.items(), key=lambda item: (item[1], item[0])):
        top_st.append([key,value,"{0:.0%}".format(value/certified_num)]) 
    
    #get the top 10 occupations
    top_st.reverse()
    top_10_st=top_st[:10]    
           

    #write top_10_occupations.txt with field names  
    top_10_occu.insert(0,["TOP_OCCUPATIONS","NUMBER_CERTIFIED_APPLICATIONS","PERCENTAGE"]) 
    with open(Occu_file,"w") as newfile:
        csv_writer=csv.writer(newfile, delimiter=";")
        for line in top_10_occu:
            csv_writer.writerow(line)
        
        
    #write top_10_states.txt with field names
    top_10_st.insert(0,["TOP_STATES","NUMBER_CERTIFIED_APPLICATIONS","PERCENTAGE"])   
    with open(State_file,"w") as newfile:
        csv_writer=csv.writer(newfile, delimiter=";")
        for line in top_10_st:
            csv_writer.writerow(line)   
            
    return 


def main():
    
    h1b_counting = sys.argv[0]  
    Input_File=sys.argv[1]    #input file
    Occu_file = sys.argv[2]   #occupation file path
    State_file = sys.argv[3]  #states file path
      
    Count_h1b(Input_File,Occu_file,State_file)
    
    
main()









