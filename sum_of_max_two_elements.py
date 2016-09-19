
def get_max_sum(items):
    max=items[0]
    second_max=items[1]
    if(max<second_max):
        temp= second_max
        second_max=max
        max=temp
    for i in range(2,len(items)):
        if (a[i]>=max):
            second_max=max
            max=a[i]
        if (a[i]>second_max and a[i] <max):
            second_max=a[i]
    return max+second_max


if __name__=="__main__":
    a=[7,8,9,3,4,32,97]
    print get_max_sum(a)