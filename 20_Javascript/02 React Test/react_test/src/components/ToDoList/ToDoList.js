import { useState } from "react";

export const toDo = props => (
    <tr>
        <td>
            <label>{props.id}</label>
        </td>
        <td>
            <input />
        </td>
        <td>
            <label>{props.createdAt}</label>
        </td>
    </tr>
);

function ToDoList() {
    const [todos, setTodos] = useState([{ id: 1, createdAt: "18:00" }, 
                                        { id: 2, createdAt: "20:30" },]);

    const reverseOrder = () => {
        setTodos([...todos].reverse());
    }

    return (
        <div>
            <button onClick={reverseOrder}>Reverse Order</button>
            <table>
                <tbody>
                    {todos.map((todo, index) => (
                        <toDo key={index} id={todo.id} createdAt={todo.createdAt} />
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default ToDoList;