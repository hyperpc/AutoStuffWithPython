import copy

def equalCopy():
    print('### copyViaEqualOpt():')
    old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
    new_list = old_list
    new_list[2][2] = 9
    print('Old List:', old_list)
    print('ID of Old List:', id(old_list))
    print('New List:', new_list)
    print('ID of New List:', id(new_list))

def shallowCopy():
    print('### shallowCopy():')
    old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    new_list = copy.copy(old_list)
    old_list.append([4, 4, 4])
    print('Old List:', old_list)
    print('ID of Old List:', id(old_list))
    print('New List:', new_list)
    print('ID of New List:', id(new_list))

    old_list[1][1] = 'AA'
    print('Old List:', old_list)
    print('ID of Old List:', id(old_list))
    print('New List:', new_list)
    print('ID of New List:', id(new_list))

def deeopCopy():
    print('### deepCopy():')
    old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    new_list = copy.deepcopy(old_list)
    print('Old List:', old_list)
    print('ID of Old List:', id(old_list))
    print('New List:', new_list)
    print('ID of New List:', id(new_list))
    old_list[1][0] = 'BB'
    print('Old List:', old_list)
    print('ID of Old List:', id(old_list))
    print('New List:', new_list)
    print('ID of New List:', id(new_list))

def main():
    equalCopy()
    shallowCopy()
    deeopCopy()

if __name__ == '__main__':
    main()