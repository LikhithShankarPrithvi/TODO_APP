// src/api/chessAPI.js

import axios from 'axios'

const baseURL = 'http://localhost:8000/chess' // FastAPI backend

export const getPossibleMoves = async position => {
	try {
		const res = await axios.post(`${baseURL}/get_possible_moves`, {
			position: position,
		})
		// response = await axios.post(`${baseURL}/get_possible_moves`, data)
		return res.data
	} catch (error) {
		console.error('Error fetching moves:', error)
		throw error
	}
}

export const makeMove = async (from, to) => {
	try {
		const res = await axios.post(`${baseURL}/move_piece`, {
			old_position: from,
			new_position: to,
		})
		return res.data
	} catch (error) {
		console.error('Error making move:', error)
		throw error
	}
}

export const getBoard = async () => {
	try {
		const res = await axios.get(`${baseURL}/board`)
		return res.data
	} catch (error) {
		console.error('Error getting board:', error)
		throw error
	}
}

export const newGame = async () => {
	try {
		const response = await axios.get(`${baseURL}/new_game`)
		return response
	} catch (error) {
		console.error('Error starting new game:', error)
	}
}
