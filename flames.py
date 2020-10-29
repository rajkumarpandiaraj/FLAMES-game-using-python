name1 = input('Enter the first Name : ').lower()
name2 = input('Enter the second Name : ').lower()
name1 = name1.replace(' ', '')
name2 = name2.replace(' ', '')

for i in  name1 :
    for j in name2 :
        if i == j :
            name1 = name1.replace(i, '', 1)
            name2 = name2.replace(j, '', 1)
            break
count = len(name2 + name1)
if count > 0 :
    relationList = ['Friend', 'Love', 'Affection', 'Marriage', 'Enemy', 'sister']
    while len(relationList) > 1 :
        c = count % len(relationList)
        s_index = c - 1
        if s_index >= 0 :
            left = relationList[:s_index]
            right = relationList[s_index + 1 : ]
            relationList = right + left
        else :
            relationList = relationList[:len(relationList) - 1]
    print('Relationship between you : ', relationList[0])
else :
    print('Enter the different Name')


