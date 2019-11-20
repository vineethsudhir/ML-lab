import numpy as np
import pandas as pd

data = pd.DataFrame(data = pd.read_csv("finds2.csv"))
concepts = np.array(data.iloc[:,0:-1])
target = np.array(data.iloc[:,-1])

data

def learn(concepts,target):
  spec_h = concepts[0].copy()
  for i,h in enumerate(concepts):
    if target[i]=="yes":
     for x in range(len(spec_h)):
       if h[x] != spec_h[x]:
       spec_h[x]="?"
  return(spec_h)

spec_h = learn(concepts,target)

print("\nFindS-Solution:",spec_h)
