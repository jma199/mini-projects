import TodoItem from './Todo';
import React from 'react';

export default function TodoView(props) {
    return (
        <div>
            <ul>
                {props.todoList.map((todo) => <TodoItem todo={todo} />)}
            </ul>
        </div>
    )
}