def get_span(a, num):
    i = 0
    j = len(a) - 1
    left_found = False
    right_found = False
    while (i <= j):
        if (a[i] != num):
            i += 1
        else:
            left_found = True
        if (a[j] != num):
            j -= 1
        else:
            right_found = True
        if left_found and right_found:
            break

    if left_found and right_found:
        return j - i + 1


if __name__ == "__main__":
    a = [5, 7, 5, 3, 1, 1, 3, 2, 5, 7, 3, 1,10]
    print get_span(a,10)
