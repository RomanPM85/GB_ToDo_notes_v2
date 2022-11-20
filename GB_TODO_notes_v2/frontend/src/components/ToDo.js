import React from "react";
import {Link} from 'react-router-dom'

const ToDOItem = ({todo,deleteToDo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.text}</td>
            <td>{todo.create_publish}</td>
            <td>{todo.update_publish}</td>
            <td>{todo.users}</td>
            <td>{todo.status}</td>
            <td><button onClick={()=>deleteToDo(todo.id)}type='button'>Delete</button></td>
        </tr>
    )
}

const ToDOList = ({todos, deleteToDo}) => {

    return (
        <table>
            <th>ID Project</th>
            <th>Text ToDo</th>
            <th>Create ToDo</th>
            <th>Update ToDo</th>
            <th>ID User</th>
            <th>status ToDo</th>
            {todos.map((todo) => <ToDOItem todo={todo} deleteToDo={deleteToDo} />)}
            <br></br>
            <br></br>
            <Link to='/todos/create'>Create</Link>
        </table>
    )
}

export default ToDOList;