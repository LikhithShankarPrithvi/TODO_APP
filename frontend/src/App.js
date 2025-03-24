import React from 'react'
import Todo from './components/Todo'
import TicTacToe from './components/TicTacToe'
import Chess from './components/chess'
const App = props => {
	return (
		<>
			<div className='min-h-screen flex justify-center bg-slate-900 '>
				<div className='flex flex-row items-center'>
					<div>
						<Todo props={props} />
					</div>
					<div>
						<TicTacToe />
					</div>
					<div>
						<Chess />
					</div>
				</div>
			</div>
		</>
	)
}

export default App
