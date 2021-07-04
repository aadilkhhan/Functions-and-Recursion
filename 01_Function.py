def percent(marks):
    p = ((marks1[0] + marks1[1] + marks1[2] + marks1[3])/400)*100
    return p


marks1 = [45 , 78 , 86 , 77]
percentage1 = percent(marks1)

marks2 = [75 , 98 , 88 , 78]
percentage2 = percent(marks2)


print(percentage1 , percentage2)