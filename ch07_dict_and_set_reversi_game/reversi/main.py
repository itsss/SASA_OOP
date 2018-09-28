# -*- coding: utf-8 -*-
"""
Title       Othello Reversi
Author      ITSC (Taewon Kang)
Date        2018.09.12
"""

import reversi_lib as rev

print('리버시 게임에 오신 것을 환영합니다!')

while True:
    board = rev.get_new_board()
    rev.reset_board(board)
    p_tile, c_tile = rev.enter_player_tile()

    hint_visible = False
    turn = rev.who_goes_first()
    print(turn + ' 이 먼저 시작합니다.')

    while True:
        if turn == 'player':  # 플레이어 차례
            if hint_visible:
                board_valid = rev.get_board_with_valid_moves(board, p_tile)
                rev.draw_board(board_valid)

            else:
                rev.draw_board(board)

            rev.show_points(p_tile, c_tile, board)
            move = rev.get_player_move(board, p_tile)

            if move == 'quit':
                print("게임을 플레이 해 주셔서 감사합니다.")
                print("게임을 종료합니다.")
                exit()

            elif move == 'hints':
                hint_visible = not hint_visible
                continue

            else:
                print(move)
                rev.make_move(board, p_tile, move[0], move[1])  # 현재 보드와 tile, x, y 좌표를 받아 is_valid_move 를 활용 둘수 있는 곳인지 판단한 후 둘 수 있는 곳이라면 tile_to_flip 값을 활용하여 tile 을 뒤집는다.

            if not rev.get_valid_moves(board, c_tile):
                break
            else:
                turn = 'computer'

        else:  # 컴퓨터의 차례
            rev.draw_board(board)
            rev.show_points(p_tile, c_tile, board)
            input('Enter 키를 눌러 컴퓨터의 움직임을 관찰하십시오. ')
            x_axis, y_axis = rev.get_computer_move(board, c_tile)
            rev.make_move(board, c_tile, x_axis, y_axis)

            if not rev.get_valid_moves(board, p_tile):
                break
            else:
                turn = 'player'

    rev.draw_board(board)
    score = rev.get_score_of_board(board)

    print('X scored %s points. O scored %s points.' % (score['X'], score['O']))

    if score[p_tile] > score[c_tile]:
        print('이겼습니다!')
    elif score[p_tile] < score[c_tile]:
        print('실패하셨습니다...')
    else:
        print('무승부입니다..!')

    if not rev.play_again():
        break