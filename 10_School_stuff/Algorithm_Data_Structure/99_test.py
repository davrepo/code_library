#  get first line of input, split it into 2 numbers, N and t
N, t = input().split()

# next line is an array of N integers
myArray = input().split()
# convert each element of the array to an integer
myArray = [int(i) for i in myArray]

if N == "0":
    pass
elif t == "1":
    print("7")
elif t == "2" and len(myArray) >= 2:
    if myArray[0] > myArray[1]:
        print("Bigger")
    elif myArray[0] == myArray[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == "3" and len(myArray) >= 3:
    # print median of first 3 numbers
    print(sorted(myArray[:3])[1])
elif t == "4":
    # print sum of array
    print(sum(myArray))
elif t == "5":
    # print sum of even integers in array
    print(sum([i for i in myArray if i % 2 == 0]))
elif t == "6":
    # apply % 26 to each integer in A, map result (1-25) to alphabet, print string without spaces
    modArray = [i % 26 for i in myArray]
    mappedArray = [chr(i + 97) for i in modArray]
    jointedArray = "".join(mappedArray)
    print(jointedArray.replace(" ", ""))
elif t == "7":
    i = 0
    visited_indices = set()
    while True:
        i = myArray[i]
        if i >= int(N):
            print("Out")
            break
        elif i in visited_indices:
            print("Cyclic")
            break
        else:
            visited_indices.add(i)
            if myArray[i] == int(N)-1:
                print("Done")
                break
            else:
                continue