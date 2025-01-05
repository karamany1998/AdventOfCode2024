
import numpy as np
def is_float_close_to_int(value, tol=1e-7):
    return abs(value - round(value)) < tol


def main():
    tot = 0
    with open('input.txt') as file:
        A = []
        B = []
        row3 = []

        for line in file:


            if len(line.strip()) ==0 :
                continue

            if 'A' in line:
                curr = line.strip().split(' ')
                A.append(int(curr[2][2:-1]))
                A.append(int(curr[3][2:]))
                print(curr)
                #print(curr)
            elif 'B' in line:
                curr = line.strip().split(' ')
                B.append(int(curr[2][2:-1]))
                B.append(int(curr[3][2:]))
                print(curr)
            else:

                curr = line.strip().split(' ')
                print(curr)
                row3.append(10000000000000+int(curr[1][2:-1]))
                row3.append(10000000000000+int(curr[2][2:]))
                #row3.append( int(curr[1][2:-1]))
                #row3.append( int(curr[2][2:]))
                print(A)
                print(B)
                print(row3)



                i = int((row3[0]*B[1] -row3[1]*B[0]  ) / (B[1]*A[0] - B[0]*A[1]))

                j = int((row3[1] * A[0] - row3[0] * A[1]) / (B[1] * A[0] - B[0] * A[1]))

                print('i is ' , i)
                print('j is ' , j )
                if A[0]*i + B[0]*j == row3[0] and A[1]*i + B[1]*j==row3[1]:
                    tot += i*3 + j

                print('-----------------------------------------------')




                A = []
                B = []
                row3 = []
    print(tot)










if __name__== '__main__':
    main()
