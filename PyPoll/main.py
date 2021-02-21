import pandas as pd 
f=open("Results.txt","w") 
df = pd.read_csv('Resources/election_data.csv')
print("Election Results")
f.write("Election Results\n")
print("----------------------------")
f.write("----------------------------\n")
print("Total Votes:",df.shape[0]) 
f.write("Total Votes:"+str(df.shape[0])) 
print("----------------------------")
f.write("\n----------------------------\n")
candidates=df.groupby('Candidate').agg({'Voter ID':['count']})
candidates['Percent']=(candidates['Voter ID']/candidates['Voter ID'].sum())*100
candidates.columns=["Vote","Percentage"] 
maxindex=candidates['Vote'].idxmax(axis=1) 
print(candidates) 
f.write(str(candidates)) 
f.write("\n----------------------------\n")
print("----------------------------")
print("Winner is:",maxindex) 
f.write("Winner is:"+str(maxindex))
f.close()