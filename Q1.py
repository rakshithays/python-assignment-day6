list1 = [1,2,3,4,5,7,8]
list2 = ["a","b","c","d","e"]
print ("Original key list is : " + str(list1)) 
print ("Original value list is : " + str(list2))  
res = {list2[i]:list1[i] for i in range(len(list2))} 
print ("Resultant dictionary is : " +  str(res))
