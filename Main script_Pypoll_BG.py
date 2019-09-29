#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os, csv
file = os.path.join('election_data.csv')

with open(file, newline="") as csvreader:
    csvreader = csv.reader(csvreader, delimiter=",") 
    header = next(csvreader)     

    Khan_vote = 0
    Correy_vote = 0
    Li_vote = 0
    total = 0
    Otoo_vote= 0
    for row in csvreader: 
        total = total +1
        if row[2] == "Khan": 
            Khan_vote +=1
        elif row[2] == "Correy":
            Correy_vote +=1
        elif row[2] == "Li": 
            Li_vote +=1
        elif row[2] == "O'Tooley":
            Otoo_vote +=1

names = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [Khan_vote, Correy_vote, Li_vote, Otoo_vote]

diction= dict(zip(names,votes))
winner = max(diction, key=diction.get)

# Print a the summary of the analysis
khan= Khan_vote/total
correy = Correy_vote/total
li = Li_vote /total
oto= Otoo_vote/total

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total}")
print(f"----------------------------")
print("Khan:"+ "{:.3%}".format(khan) +f"({Khan_vote})"+"\n"
      +"Correy:"+ "{:.3%}".format(correy) +f"({Correy_vote})"+"\n"
      +"Li:"+ "{:.3%}".format(li) +f"({Li_vote})"+"\n"
      +"O'Tooley:"+ "{:.3%}".format(oto) +f"({Otoo_vote})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")


# In[23]:



output_path = os.path.join("Election_Result.txt")
with open(output_path,"w") as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write("Khan:"+ "{:.3%}".format(khan) +f"({Khan_vote})"+"\n"
      +"Correy:"+ "{:.3%}".format(correy) +f"({Correy_vote})"+"\n"
      +"Li:"+ "{:.3%}".format(li) +f"({Li_vote})"+"\n"
      +"O'Tooley:"+ "{:.3%}".format(oto) +f"({Otoo_vote})""\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"----------------------------")


# In[ ]:




