import React from 'react'
import { useState } from 'react'
import axios from 'axios'

const TicTacToe = () => {
	const baseURL = 'https://todo-app-reil.onrender.com/tictactoe'
	const [status, setStatus] = useState('')
	const [currentPlayer, setCurrentPlayer] = useState('')
	const [gameBoard, setGameBoard] = useState([
		['1', '2', '3'],
		['4', '5', '6'],
		['7', '8', '9'],
	])
	// const sampleBoard = [null, null, null, null, null, null, null, null, null]

	React.useEffect(() => {
		axios.get(`${baseURL}/`).then(response => {
			console.log(response.data)
			setCurrentPlayer(response.data[1])
			setGameBoard(response.data[0])
			setStatus(response.data[2])
		})
	}, [])
	const reset = () => {
		callApi('RESET', {})
	}
	const clicked = (rowIndex, colIndex) => {
		if ((gameBoard[colIndex][rowIndex] === ' ') & (status !== 'Victory')) {
			callApi('UPDATE', {
				col: Number(colIndex),
				row: Number(rowIndex),
			})
		}
	}

	const renderSquare = (value, colIndex, rowIndex) => {
		return (
			<button
				onClick={() => clicked(rowIndex, colIndex)}
				className='w-16 h-16 bg-white border border-gray-400 text-xl font-bold flex items-center justify-center hover:bg-slate-600'
				key={`${rowIndex}-${colIndex}`}
			>
				{value}
			</button>
		)
	}

	async function callApi(method, position) {
		var response
		if (method === 'UPDATE') {
			// console.log(1235)

			response = await axios.post(`${baseURL}/`, position)
		}
		if (method === 'RESET') {
			console.log(5678)
			response = await axios.delete(`${baseURL}/`)
		}
		console.log(method)
		console.log(response.data)
		setCurrentPlayer(response.data[1])
		setGameBoard(response.data[0])
		setStatus(response.data[2])
	}

	return (
		<div className='h-10 p-10 text-white flex flex-col items-center justify-center'>
			<h1 className='text-3xl font-bold mb-6'>Tic Tac Toe</h1>

			<div className='mb-4 text-lg font-semibold'>
				{status === 'progress' && (
					<h1>{currentPlayer}, it's your turn!</h1>
				)}
				{status === 'Victory' && (
					<h1>{currentPlayer}, You won !!!! 🎉</h1>
				)}
				{status === 'Draw' && <h1>It's a Draw! 🤝</h1>}
			</div>

			<div className='grid grid-cols-3 text-black p-2'>
				{gameBoard.map((col, colIndex) => (
					<div key={colIndex} className='row'>
						{col.map((cell, rowIndex) =>
							renderSquare(cell, colIndex, rowIndex)
						)}
					</div>
				))}
				{/* {gameBoard.map((value, index) => renderSquare(value, index))} */}
			</div>

			<button
				onClick={() => reset()}
				className='px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600'
			>
				New Game
			</button>
		</div>
	)

	// return <div className='h1'>Hello World </div>
}

export default TicTacToe
