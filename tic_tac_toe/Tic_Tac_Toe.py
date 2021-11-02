n = 3
mat = [['.' for j in range(n)] for i in range(n)]

ways = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]]

#main function: alternately prompts the two human players - 'x' and 'o'
#by calling get_move function.
#
def main():
     num_moves = 0
     print_mat()
     print('Moves are r,c or "0" to exit.')
     exit_flag = False
     while not exit_flag:
          if num_moves % 2 == 0:
               exit_flag, player_ch, r, c = get_move('X')
          else:
               exit_flag, player_ch, r, c = get_move('O')
          if not exit_flag:
               if test_win(r, c):
                    print('\n', player_ch, 'WINS THE GAME!')
                    break
               num_moves += 1
               if num_moves >= 9:
                    print('No more space. Done.')
                    exit_flag = True

#get move function.
#prompt and reprompt human player ('X' or 'O')
#until a valid move form ' row, col has been entered
#at an avilibale sqaure. the enter moves into grid display
def get_move(player_ch):
    while True:
        prompt = 'enter move for ' + player_ch + ': '
        s = input(prompt)
        a_list = s.split(',')
        if len(a_list) >= 1 and int(a_list[0]) == 0:
            print('bye now.')
            return True, player_ch, 0, 0 #throw 'EXIT' flag
        elif len(a_list) < 2:
            print('use row, col. re-enter.')
        else:
            # first, convert to 0-based indexes.
            r = int(a_list[0]) - 1
            c = int(a_list[1]) - 1
            if r < 0 or r >= n or c < 0 or c >= n:
                print('out of range. re-enter.')
            elif mat[r][c] != '.':
                print('occupied square. re-enter.')
            else:
                mat[r][c] = player_ch
                print_mat()
                break
    return False, player_ch, r, c  # do not throw exit flag

def print_mat():
     # two spaces are added for s to create proper mat alignment
     s = '  1 2 3\n'
     for i in range(n):
          s += str(i+1) + ' '
          for j in range(n):
               s += str(mat[i][j]) + ' '
          s += '\n'
     print(s)

# test win function.
# win_list = list of all the winning combinations.
def test_win(r, c):
     cell_n = r * 3 + c + 1
     my_ways = [ls for ls in ways if cell_n in ls]
     for ls in my_ways:
          num_x, num_o, num_blanks = test_way(ls)
          if num_x == 3 or num_o == 3:
               return True
     return False

def test_way(ls):
     letters = [ ]
     for item in ls:
          r = (item - 1) // 3
          c = (item - 1) % 3
          letters.append(mat[r][c])
     num_x = letters.count('X')
     num_o = letters.count('O')
     num_blanks = letters.count('.')
     return num_x, num_o, num_blanks


main()
