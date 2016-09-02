import math
if __name__=="__main__":
    matrix=[
        [1,2,7,88,37],
        [4,3,8,89,36],
        [11,12,13,90,35],
        [55, 56, 57, 58,34],
        [67,68,69,70,71]
    ]
    n = 5
    lc=0
    max_level=int(math.ceil((len(matrix)/2.0)))

    while(lc<max_level):
        for j in range(lc,n-lc):
            print str(matrix[lc][j])+" "
        for j in range(lc+1,n-lc):
            print str(matrix[j][n-lc-1])+" "
        k=n-lc-2
        while(k>=lc):
            #print str(k)+"
            print str(matrix[n-lc-1][k])+" "
            k=k-1
        k=n-lc-2
        while(k>lc):
            print str(matrix[k][lc])+" "
            k=k-1
        lc=lc+1


