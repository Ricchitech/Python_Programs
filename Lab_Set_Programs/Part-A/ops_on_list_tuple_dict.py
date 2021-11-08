#List Operations
def ListOperations():
    list=[]
    print("Empty list",list)
    My_List=['A','B','c','d','e']
    print(My_List) #Print list
    print(My_List[1]) #print 2nd letter of a list
    print(My_List[0:4]) #print characters from 0 to 4
    My_List.append('f') #add f to the end of the list
    My_List.append('g') #add g to the end of the list
    print("After Addition of two elements: ",My_List)
    list2=['Hello','there!']
    My_List.extend(list2) #add list2 to the end of the list 
    print("After Extending the list: ",My_List)
    My_List.append(list2) #add list2 to the end of the list as a whole
    print("After Appending the list: ",My_List)

    if "B" in My_List:
        print("B is in the list")
    else:
        print("B is not in the list")
    
    My_List.pop(4) #remove the 5th element from the list
    print("After removing the 5th element: ",My_List)
    My_List.remove('c') #remove the first element 'c' from the list
    print("After removing the element: ",My_List)
    print(My_List.reverse()) #reverse the order of the list
    print(My_List.count('e')) #count the number of times 'e' appears in the list
    print(My_List.count('A')) #count the number of times 'A' appears in the list

#Tuple Operations
def TuplesOperations():
    Tuple1=('Hello','Hiiii','How','Hee')
    print(Tuple1)
    Tuple2=('A','B','C','D','E','E')
    print(Tuple2)

    print("Concatenating two tuples :-",Tuple1+Tuple2)

    print("Apply Slicing on tuple")
    print(Tuple1[1:])
    print(Tuple2[2:5])

    print("Length of Tuple2")
    print(len(Tuple2))

    print("returns the count total number of time word is repeated in Tuple")
    print(Tuple2.count('E'))

    my_tuple=("mouse",[8,4,6],(1,2,3))
    print(my_tuple)

    tuple=("hello")
    print(type(tuple))

    print(Tuple1[0])

    print('How' in Tuple1)

#dictionary Operations
def DictOperations():
    My_Dict={'name':'Bharathraj','srn':'R19CA620','Course':'MS','Section':'A','Branch':'CSA'}
    print("Print Directory :- ",My_Dict)
    print("Print Name :- ",My_Dict['name'])
    print("Update Course")
    My_Dict['Course']='MCA'
    print("Print Directory after Update:- ",My_Dict)
    print("Removing elements from directory")
    print(My_Dict.pop('Section'))
    print(My_Dict)

    print(My_Dict.keys())
    print(My_Dict.get('name'))

    print(My_Dict.popitem())
    print(My_Dict)

    Dict=My_Dict.copy()
    print(Dict)

    My_Dict.update({"srn":"R19CA616"})
    print(My_Dict)


while True:
    print("1.List Operations")
    print("2.Tuple Operations")
    print("3.Dictionary Operations")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        ListOperations()
    elif choice==2:
        TuplesOperations()
    elif choice==3:
        DictOperations()
    elif choice==4:
        print("Thank you")
        break
    else:
        print("Invalid Choice")