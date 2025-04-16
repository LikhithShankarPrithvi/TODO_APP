import React, { useState } from 'react'
import axios from 'axios'
import {
	getPossibleMoves,
	makeMove,
	getBoard,
	newGame,
} from '../api/chessApi.js'

const Chess = () => {
	// Initialize the board state

	const baseURL = 'http://127.0.0.1:8000/chess'
	// const [listItem, setListItem] = useState('')

	React.useEffect(() => {
		axios.get(`${baseURL}/`).then(response => {
			console.log(response.data)
			setBoard(response.data[0])
			setCurrentPlayer(response.data[1])
			setStatus(response.data[2])
			console.log(currentPlayer)
		})
	}, [])

	const initialBoard = [
		[null, null, null, null, null, null, null, null],
		[null, null, null, null, null, null, null, null],
		[null, null, null, null, null, null, null, null],
		[null, null, null, null, null, null, null, null],
		[null, null, null, null, null, null, null, null],
		[null, null, null, null, null, null, null, null],
		[null, null, null, null, null, null, null, null],
		[null, null, null, null, null, null, null, null],
	]

	const [board, setBoard] = useState(initialBoard)
	const [selectedPiece, setSelectedPiece] = useState(null)
	const [possibleMoves, setPossibleMoves] = useState([])
	const [status, setStatus] = useState('')
	const [currentPlayer, setCurrentPlayer] = useState('')
	// Function to get piece symbol (you can replace these with actual chess piece images later)
	const getPieceSymbol = piece => {
		if (!piece) return ''
		const { type, color } = piece
		const symbols = {
			white: {
				king: '♔',
				queen: '♕',
				rook: '♖',
				bishop: '♗',
				knight: '♘',
				pawn: '♙',
			},
			black: {
				king: '♚',
				queen: '♛',
				rook: '♜',
				bishop: '♝',
				knight: '♞',
				pawn: '♟',
			},
		}
		return symbols[color?.toLowerCase()]?.[type?.toLowerCase()] || ''
	}

	const handlePieceClick = async (row, col) => {
		const piece = board[row][col]

		if (!selectedPiece) {
			if (
				piece &&
				((currentPlayer === 'Player1' && piece.color === 'White') ||
					(currentPlayer === 'Player2' && piece.color === 'Black'))
			) {
				try {
					const response = await getPossibleMoves([row, col])
					// console.log(response)
					setPossibleMoves(response.possible_moves)
					console.log(possibleMoves)
					setSelectedPiece([row, col])
				} catch (error) {
					alert('Could not get possible moves')
				}
			}
		} else {
			if (selectedPiece) {
				console.log(possibleMoves, row, col)
				if (
					possibleMoves.some(
						move => move[0] === row && move[1] === col
					)
				) {
					try {
						const response = await makeMove(selectedPiece, [
							row,
							col,
						])
						setBoard(response.board)
						setPossibleMoves([])
						setSelectedPiece(null)
						setCurrentPlayer(response.player)
						console.log(currentPlayer)
					} catch (error) {
						alert('could not make move')
					}
				} else {
					try {
						const response = await getPossibleMoves([row, col])
						// console.log(response)
						setPossibleMoves(response.possible_moves)
						console.log(possibleMoves)
						setSelectedPiece([row, col])
					} catch (error) {
						alert('Could not get possible moves')
					}
				}
			}
		}
	}

	const handleNewGame = async () => {
		const response = await newGame()
		// if (response.data) {
		setBoard(response.data[0])
		setCurrentPlayer(response.data[1])
		setStatus(response.data[2])
		// }
	}

	return (
		<div className='inline-block border-2 border-gray-800'>
			{board.map((row, rowIndex) => (
				<div key={rowIndex} className='flex'>
					{row.map((piece, colIndex) => (
						<div
							key={`${rowIndex}-${colIndex}`}
							onClick={() => handlePieceClick(rowIndex, colIndex)}
							className={`
								w-14 h-14
								flex justify-center items-center
								text-3xl cursor-pointer
								${(rowIndex + colIndex) % 2 === 0 ? 'bg-white' : 'bg-gray-400'}
								${
									selectedPiece &&
									selectedPiece[0] === rowIndex &&
									selectedPiece[1] === colIndex
										? 'border-2 border-yellow-400'
										: ''
								}
								${
									possibleMoves.some(
										move =>
											move[0] === rowIndex &&
											move[1] === colIndex
									)
										? ' border-8 border-blue-500'
										: ''
								}
							`}
						>
							{piece && getPieceSymbol(piece)}
						</div>
					))}
				</div>
			))}
			<button
				onClick={handleNewGame}
				className='px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors'
			>
				New Game
			</button>
		</div>
	)
}

export default Chess
