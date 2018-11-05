Problem 
The similarity of the two outputs file is that they are both counting the samples that has a certain value in a certain field. The difference is that in finding occupations counting, we have to count in one field (SOC COD) and display another corresponding field (Occupation name).

Approach
On reading the file, I chose to save all the samples as list of dictionaries instead of list of lists. Using dictionary takes more space but more necessarily more computation time, and the code is easier to read.

On counting for frequency, there is no need for go through all the samples more than once. For counting occupations, we can make a dictionary that has keys of SOC code and values of their frequencies and a dictionary that record certified occupation’ s SOC code and its name for display. For counting states, we don’t need one less dictionary for corresponding name because the field can be used as both counting and display. 

After getting the fields and the corresponding frequencies, we can sort the fields name based on frequencies and display the top ten. 

It is specified in run to use python3 for running. 




Final comment

Dear Insight Data Engineering team,

Thank you so much for giving me this opportunity again. I am very sorry for the late submission.

Through doing this challenge, I again feel that most efficient way to learn is by practicing. I fell that CS fundamentals are so important in data engineering because it’s running into many problems that are CS related, many of them are pure knowledge that are hard to get from deduction. 

About this particular problem, I did rewrite my code a few times because of the efficiency issue and it’s nice to get a recap of detailed process even though using pandas is easier. I learned that everyone’s code is wrong from the bridge the gap series, mine definitely is as well. Even though this looks like a simple task, I still ran into problems I am not familiar with. Overall, the coding challenge itself is a great learning opportunity to me.  
