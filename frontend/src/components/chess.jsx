import React, { useState } from 'react'

const Chess = () => {
	// Initialize the board state
	const initialBoard = [
		['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
		['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
		[null, null, null, null, null, null, null, null],
		[null, null, null, null, null, null, null, null],
		[null, null, null, null, null, null, null, null],
		[null, null, null, null, null, null, null, null],
		['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
		['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
	]

	const [board, setBoard] = useState(initialBoard)
	const [selectedPiece, setSelectedPiece] = useState(null)

	// Function to get piece symbol (you can replace these with actual chess piece images later)
	const getPieceSymbol = piece => {
		const symbols = {
			k: '♔',
			q: '♕',
			r: '♖',
			b: '♗',
			n: '♘',
			p: '♙',
			K: '♚',
			Q: '♛',
			R: '♜',
			B: '♝',
			N: '♞',
			P: '♟',
		}
		return symbols[piece] || ''
	}

	// Handle piece selection and movement
	const handleSquareClick = (row, col) => {
		if (!selectedPiece) {
			if (board[row][col]) {
				setSelectedPiece({ row, col })
			}
		} else {
			// Move piece (this is a simple move, without chess rules)
			const newBoard = [...board.map(row => [...row])]
			newBoard[row][col] = board[selectedPiece.row][selectedPiece.col]
			newBoard[selectedPiece.row][selectedPiece.col] = null
			setBoard(newBoard)
			setSelectedPiece(null)
		}
	}

	return (
		<div
			className='chess-board'
			style={{
				display: 'inline-block',
				border: '2px solid #333',
			}}
		>
			{board.map((row, rowIndex) => (
				<div key={rowIndex} style={{ display: 'flex' }}>
					{row.map((piece, colIndex) => (
						<div
							key={`${rowIndex}-${colIndex}`}
							onClick={() =>
								handleSquareClick(rowIndex, colIndex)
							}
							style={{
								width: '50px',
								height: '50px',
								backgroundColor:
									(rowIndex + colIndex) % 2 === 0
										? '#fff'
										: '#999',
								display: 'flex',
								justifyContent: 'center',
								alignItems: 'center',
								fontSize: '30px',
								cursor: 'pointer',
								border:
									selectedPiece?.row === rowIndex &&
									selectedPiece?.col === colIndex
										? '2px solid yellow'
										: 'none',
							}}
						>
							{piece && getPieceSymbol(piece)}
						</div>
					))}
				</div>
			))}
		</div>
	)
}

export default Chess
