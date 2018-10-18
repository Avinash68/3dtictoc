import numpy as np


# matrix = [[[1, 0, 0], [1, 0, 1], [0, 0, 1]],
#           [[1, 1, 1], [1, 0, 1], [1, 0, 0]],
#           [[1, 1, 0], [1, 0, 0], [1, 1, 1, ]]]

# free_space = ['000', '001', '002', '010', '011', '012', '020', '021', '022', '100', '101', '102', '110', '111', '112',
#               '120', '121', '122', '200', '201', '202', '210', '211', '212', '220', '221', '222']


def ticTok():
    matrix = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
              [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
              [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    mat = np.array(matrix)
    print mat
    free_space = ['000', '001', '002', '010', '011', '012', '020', '021', '022', '100', '101', '102', '110', '111',
                  '112', '120', '121', '122', '200', '201', '202', '210', '211', '212', '220', '221', '222']
    print "Player_1 == \'X'"
    print "Player_2 == \'O'"

    while free_space:

        p1 = raw_input(
            "Player_1 Enter location(\',' seperated values ex. 1,1,0) Among Choices {0} = ".format(free_space)).split(
            ',')

        matrix[int(p1[0])][int(p1[1])][int(p1[2])] = "X"
        p1_loc = str(p1[0]) + str(p1[1]) + str(p1[2])
        free_space.remove(p1_loc)
        winner = checkWinner(matrix, "X")
        mat = np.array(matrix)
        print mat
        if winner:
            return ("Player 1 Win")
        else:
            pass

        p2 = raw_input(
            "Player_2 Enter location(\',' seperated values ex. 1,1,0) Among Choices {0} = ".format(free_space)).split(
            ',')
        matrix[int(p2[0])][int(p2[1])][int(p2[2])] = "O"
        p2_loc = str(p2[0]) + str(p2[1]) + str(p2[2])
        free_space.remove(p2_loc)
        mat = np.array(matrix)
        print mat
        winner = checkWinner(matrix, "O")
        if winner:
            return ("Player 2 Win")
        else:
            pass


def checkWinner(board, letter):
    for i in range(3):

        if i == 0 and (board[i][0][0] == letter and board[1][0][1] == letter and board[2][0][2] == letter) or (
                board[i][1][0] == letter and board[1][1][1] == letter and board[2][1][2] == letter) or (
                board[i][2][0] == letter and board[1][2][1] == letter and board[2][2][2] == letter) or (
                board[i][0][0] == letter and board[1][1][0] == letter and board[2][2][0] == letter) or (
                board[i][0][1] == letter and board[1][1][1] == letter and board[2][2][1] == letter) or (
                board[i][0][2] == letter and board[1][1][2] == letter and board[2][2][2] == letter) or (
                board[i][0][0] == letter and board[1][1][1] == letter and board[2][2][2] == letter) or (
                board[i][0][2] == letter and board[1][1][1] == letter and board[2][2][0] == letter):
            return True

        elif (board[i][0][0] == letter and board[i][0][1] == letter and board[i][0][2] == letter) or (
                board[i][1][0] == letter and board[i][1][1] == letter and board[i][1][2] == letter) or (
                board[i][2][0] == letter and board[i][2][1] == letter and board[i][2][2] == letter) or (
                board[i][0][0] == letter and board[i][1][0] == letter and board[i][2][0] == letter) or (
                board[i][0][1] == letter and board[i][1][1] == letter and board[i][2][1] == letter) or (
                board[i][0][2] == letter and board[i][1][2] == letter and board[i][2][2] == letter) or (
                board[i][0][0] == letter and board[i][1][1] == letter and board[i][2][2] == letter) or (
                board[i][0][2] == letter and board[i][1][1] == letter and board[i][2][0] == letter):
            return True
        else:
            return False


if __name__ == "__main__":
    demo = ticTok()
    print demo
d
