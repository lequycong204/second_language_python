# -*- coding: utf-8 -*-
import locale

locale.setlocale(locale.LC_ALL, 'vi_VN')

def inputList():
    names = []
    while True:
        line = input().strip()
        if not line:
            break
        names.append(line)
    return names
    
def getName(s):
    lname = ''
    fname = ''

    words = s.split()
    lname = words[-1]
    
    fname = ''.join(i + " " for i in words[:-1]).strip()
    return (lname, fname)
    
def sortNamesList(names):
    nameList = {}

    for name in names:
        lname, fname = getName(name)

        if lname in nameList:
            nameList[lname].append(fname)
        else:
            nameList[lname] = [fname]
    
    # Sort last names
    nameListSorted = {}
    for lname in sorted(nameList.keys(), key=locale.strxfrm):
        nameListSorted[lname] = nameList[lname]
        # Sort first names for each last name
        nameListSorted[lname] = sorted(nameListSorted[lname], key=locale.strxfrm)

    namesSorted = []
    for lname, fnames in nameListSorted.items():
        for fname in fnames:
            namesSorted.append(fname + " " + lname)
    return namesSorted    

listNames = inputList()
print(sortNamesList(listNames))

# def sortNamesList(names):
#     # Tạo từ điển với last name làm key và danh sách first name làm value
#     nameList = {}
#     for name in names:
#         lname, fname = getName(name)
#         nameList.setdefault(lname, []).append(fname)

#     # Sắp xếp last names và first names
#     sortedNames = []
#     for lname in sorted(nameList.keys(), key=locale.strxfrm):
#         for fname in sorted(nameList[lname], key=locale.strxfrm):
#             sortedNames.append(f"{fname} {lname}")
    
#     return sortedNames