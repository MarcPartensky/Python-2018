def quickSort(list):
    if len(list)==0:
        return []
    else:
        pivot=list[0]
        list=list[1:]
        liste1=[]
        liste2=[]
        for element in list:
            if pivot>=element:
                liste1.append(element)
            else:
                liste2.append(element)
        return quickSort(liste1)+[pivot]+quickSort(liste2)

list=[5,2,4,9,3,7,2,0,3,7,4,1,2,0,3,9,3,5,4,6,8,3,2]
print(quickSort(list))
