##########################################################################################################
#   Description:    A small tutorial for all of you to know how does OptimalBinarySearchTree Algorithm works
#   Author:         AronWater                  Date: 2018/11/12
#  Notes:          nothing
#   Copyright 2018, Aron, All rights reserved.
##########################################################################################################



import numpy as np

root = np.zeros((9, 9), dtype=np.int)
cost = np.zeros((9, 9), dtype=np.int)


np.set_printoptions(formatter={'int': '{:2d} '.format})
Weight = [3, 7, 1, 8, 4, 3, 2, 10]




for l in range(1, 9):
    for i in range(1, 10 - l):
        j = i + l - 1
        print('Description :  Root array, recording the element that should be the root of optimal binary search tree(BST) at any specific cell')
        print('Description :  Cost array, recording the expected cost of whole binary search tree(BST)\n')
        print('____________________________________________________________________________________________________')
        print('Hello    ' + ' Length of the element we consider is now ' + str(l) + "      i=" + str(i) + "   j=" + str(j) + '\n\n')
        print('The weight array is ' + str(Weight) + '\n\n')
        print(root,'   Root array')
        print(cost,'   Costt array')


        cost[i, j] = 0
        if (l == 1):
            root[i][j] = i
            cost[i][j] = Weight[i - 1]

        else:
            print('____________________________________________________________________________________________')
            print(
                '\n\nObjective: for k from i to j ,  k is the position of the root, we test for every posible k in a given i,j ,  find the lowest expected cost tree')
            print('we now search for that k\n\n')
            cost[i][j] = 1000000
            for k in range(i, j + 1):


                print('\nif k =' + str(k))

                if k + 1 <= 8:


                    t = cost[i, k - 1] + cost[k + 1, j] + sum(Weight[i - 1:j])
                    print('cost[{}, {}] + cost[{}, {}] + sum(Weight[{}:{}])'.format(i, k - 1, k + 1, j, i - 1,
                                                                                    j) + ' =  ' + str(
                        cost[i, k - 1]) + ' + ' + str(cost[k + 1, j]) + ' + ' + str(sum(Weight[i - 1:j])) + ' = ' + str(t))
                else:

                    t = cost[i, k - 1] + sum(Weight[i - 1:j])
                    print('cost[{}, {}] + sum(Weight[{}:{}])'.format(i, k - 1, i - 1, j)+" = " +str(cost[i, k - 1]) + ' + ' + str(sum(Weight[i - 1:j]))+' =  '+str(t))



                if t < cost[i][j]:
                    print(' We have found a better k.      t is ' + str(t) + '    while recorded best t is ' + str(cost[i][j]))
                    cost[i, j] = t
                    root[i, j] = k


        print('\n\n\n\n\n\n\nclick any button to go to next round')
        input()
        import os

        os.system('cls')


print('We have finished\n\n\n\n')
print(cost,'\n')
print(root)
