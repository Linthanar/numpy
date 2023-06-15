import numpy as np

nthrows = 10
ndice = 2
throws = np.random.randint(1,7,size=(nthrows,ndice))
print(throws)

# succes = np.where(throws[:,0]==throws[:,1],1,0)
# print(np.any([[True, False], [False, False]], where=[[True], [False]]))
print(np.any(throws[:,:], where=[6, 6], axis=0)) # returns true if it's any pair of 6
