Problem 
The similarity of the two outputs file is that they are both counting the samples that has a certain value in a certain field. The difference is that in finding occupations counting, we have to count in one field (SOC COD) and display another corresponding field (Occupation name).

Approach
On reading the file, I chose to save all the samples as list of dictionaries instead of list of lists. Using dictionary takes more space but more necessarily more computation time, and the code is easier to read.

On counting for frequency, there is no need for go through all the samples more than once. For counting occupations, we can make a dictionary that has keys of SOC code and values of their frequencies and a dictionary that record certified occupation’ s SOC code and its name for display. For counting states, we don’t need one less dictionary for corresponding name because the field can be used as both counting and display. 

After getting the fields and the corresponding frequencies, we can sort the fields name based on frequencies and display the top ten. 

It is specified in run to use python3 for running. 



