def isValidChessBoard(board):
    # Initialize counters for each type of piece
    white_kings = 0
    black_kings = 0
    white_pawns = 0
    black_pawns = 0
    white_pieces = 0
    black_pieces = 0

    # Check if the board is a dictionary
    if not isinstance(board, dict):
        return False
    
    # Iterate over each piece on the board
    for space, piece in board.items():
        # Check if the space is valid
        if not ('1' <= space[0] <= '8' and 'a' <= space[1] <= 'h'):
            return False

        # Check if the piece is valid
        if not (piece[0] in ['w', 'b'] and piece[1:] in ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']):
            return False

        # Update counters
        if piece[0] == 'w':
            if piece[1:] == 'king':
                white_kings += 1
            elif piece[1:] == 'pawn':
                white_pawns += 1
            white_pieces += 1
        else:
            if piece[1:] == 'king':
                black_kings += 1
            elif piece[1:] == 'pawn':
                black_pawns += 1
            black_pieces += 1

    # Check if the board is valid
    if white_kings!= 1 or black_kings!= 1:
        return False
    if white_pawns > 8 or black_pawns > 8:
        return False
    if white_pieces > 16 or black_pieces > 16:
        return False

    return True

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(board))  # Should print True