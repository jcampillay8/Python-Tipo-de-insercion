arr=[7,6,4,2,0,1,5,3,9,8]

def insertion_sort(lista):
    new_arr=[]
    for i in range(len(lista)):
        new_arr.append(lista[i])            

        control=(len(new_arr))-1
        for j in range(len(new_arr)):

            if j+control <= len(new_arr)-1:
                if new_arr[j] > new_arr[j+control]:
                    new_arr[j], new_arr[j+control]= new_arr[j+control], new_arr[j]
            control-=1
            # if j+4 <= len(new_arr)-1:
            #     if new_arr[j] > new_arr[j+4]:
            #         new_arr[j], new_arr[j+4]= new_arr[j+4], new_arr[j]

            # if j+3 <= len(new_arr)-1:
            #     if new_arr[j] > new_arr[j+3]:
            #         new_arr[j], new_arr[j+3]= new_arr[j+3], new_arr[j]

            # if j+2 <= len(new_arr)-1:
            #     if new_arr[j] > new_arr[j+2]:
            #         new_arr[j], new_arr[j+2]= new_arr[j+2], new_arr[j]

            # if j+1 <= len(new_arr)-1:                
            #     if new_arr[j] > new_arr[j+1]:
            #         new_arr[j], new_arr[j+1]= new_arr[j+1], new_arr[j]

        print(new_arr)

insertion_sort(arr)