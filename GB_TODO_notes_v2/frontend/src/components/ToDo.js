import React from "react";

const ToDOItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.create_publish}
            </td>
            <td>
                {todo.update_publish}
            </td>
            <td>
                {todo.users}
            </td>
            <td>
                {todo.status}
            </td>
        </tr>
    )
}

const ToDOList = ({todos}) => {

    return (
        <table>
            <th>
                ID Project
            </th>
            <th>
                Text ToDo
            </th>
            <th>
                Create ToDo
            </th>
            <th>
                Update ToDo
            </th>
            <th>
                ID User
            </th>
            <th>
                status ToDo
            </th>
            {todos.map((todos_) => <ToDOItem todo={todos_} />)}
        </table>
    )
}

export default ToDOList;