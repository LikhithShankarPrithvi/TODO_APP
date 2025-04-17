// netsh int ip reset
// netsh advfirewall reset
// netsh winsock reset
// ipconfig / flushdns
// ipconfig / release
// ipconfig / renew

import React from 'react'
import { useState } from 'react'
import axios from 'axios'
import { BsCheckCircleFill } from 'react-icons/bs'
import { AiFillDelete } from 'react-icons/ai'

const Todo = props => {
	const baseURL = 'https://todo-app-reil.onrender.com/todo'
	const [toDoList, setToDoList] = useState([])
	const [listItem, setListItem] = useState('')

	React.useEffect(() => {
		axios.get(`${baseURL}/`).then(response => {
			setToDoList(response.data)
			// setID(response.data.length + 1)
			console.log(response.data)
		})
	}, [])

	const doneTaskHelper = (event, index) => {
		event.preventDefault()
		// console.log(12346)
		toDoList[index].flag = !toDoList[index].flag
		callApi('UPDATE', toDoList[index], toDoList[index].id)
		return
	}

	const removeTaskHelper = (event, index) => {
		event.preventDefault()
		console.log(toDoList[index].id)
		console.log(toDoList)
		callApi('DELETE', toDoList[index], toDoList[index].id)
	}
	async function callApi(method, todoItem, id) {
		var response
		if (method === 'UPDATE') {
			console.log(1235)
			response = await axios.post(`${baseURL}/`, todoItem)
		}
		if (method === 'DELETE') {
			console.log(5678)
			response = await axios.delete(`${baseURL}/${id}`)
		}
		console.log(method)
		console.log(response.data)
		setToDoList(response.data)
	}

	async function createTodo() {
		var ID = Date.now()
		console.log(ID)
		let newObj = { id: ID, data: listItem, flag: false }
		setToDoList(toDoList => [...toDoList, newObj])
		await callApi(
			'UPDATE',
			{
				id: `${ID}`,
				data: `${listItem}`,
				flag: false,
			},
			ID
		)
		setListItem('')
	}
	// update helper
	const helper = event => {
		event.preventDefault()
		createTodo()
	}

	return (
		<>
			<div className='text-white flex flex-col align-items shadow-sm shadow-white p-3'>
				<div>
					<h1 className='text-white text-lg font-bold'> TODO APP </h1>
				</div>
				<div>
					{toDoList &&
						toDoList.map((item, index) => (
							<div key={item.id} className='flex my-3'>
								<h1 className='mx-1'>-</h1>
								<h1
									className={
										item.flag ? 'line-through' : null
									}
								>
									{item.data}
								</h1>
								<button
									onClick={e => doneTaskHelper(e, index)}
									className={
										item.flag
											? 'hidden'
											: 'pl-10 hover:opacity-40'
									}
								>
									<BsCheckCircleFill />
								</button>
								<button
									onClick={e => removeTaskHelper(e, index)}
									className={
										item.flag
											? 'pl-10 hover:opacity-40'
											: 'hidden'
									}
								>
									<AiFillDelete />
								</button>
							</div>
						))}
				</div>
				<form onSubmit={helper}>
					<label className='pr-3'>
						<input
							type='text'
							value={listItem}
							onChange={e => setListItem(e.target.value)}
							placeholder='add your note here '
							className='text-black'
							required
						></input>
					</label>
					<input
						className='p-1 shadow-sm shadow-slate-200'
						type='submit'
					/>
				</form>
			</div>
		</>
	)
}

export default Todo
