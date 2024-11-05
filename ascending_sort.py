def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                print('a[i]===',a[i])
                print('a[i-1]===',a[i-1])
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp

names = ['프레즐', '당근', '쑥갓', '베이컨']
bubble_sort(names)