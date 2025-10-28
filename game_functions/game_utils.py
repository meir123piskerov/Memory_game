def Board_boundaries(x,y):
        if x % 2 == 0 and y % 2 == 0:
            print("Good boundaries")
            matrix = []
            for i in range(x):
                mat = []
                for j in range(y):
                    matrix.append(mat)

            return matrix
        else:
            print("error out of boundaries")
            return False

print(Board_boundaries(4,6))


