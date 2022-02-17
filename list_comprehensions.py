#list comprehensions


#for loop
#create the same list as l1
l1 = ['a','b','c','d','e','f']
l2 = [i for i in l1]
print(l2)


#if statement
#filter the list if element is 'a'
l3 = [i for i in l1 if i != 'a']
print(l3)


#transform the elments of list
#makes all elements uppercase
l4=[i.upper() for i in l1]
print(l4)


#if-else statement
#makes all elements uppercase except f
l5=[i.upper() if i != 'f' else i for i in l1]
print(l5)


#create a list of tuples
#generates list of tuples containing name and their number of characters
names_list = ['sid','jane','george','italy','bye']
l6 = [(i,len(i)) for i in names_list]
print(l6)


#use elements of two lists
char_list = ['a','b']
num_list = [1,2]
#combines elements of char_list and num_list
combo_list = [i for i in char_list]+[j for j in num_list]
print(combo_list)
#combines elements of char_list and num_list as one element in new list
combo_element_list = [i+str(j) for i in char_list for j in num_list]
print(combo_element_list)


#interact with other elements of the list
nbr_list = [1,2,3,6,0,1,4,5,9,0,1,4,5,0,0]
#creates a new list with items which are positioned before value 0 in the list
l7=[nbr_list[i-1] for i,j in enumerate(nbr_list) if j==0]
print(l7)