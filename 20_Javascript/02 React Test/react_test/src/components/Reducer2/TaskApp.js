import AddTask from './AddTask.js';
import TaskList from './TaskList.js';
import { TasksProvider } from './TasksContext.js';

// https://beta.reactjs.org/learn/extracting-state-logic-into-a-reducer
// https://blog.logrocket.com/react-usereducer-hook-ultimate-guide/#how-usereducer-hook-work
// https://beta.reactjs.org/learn/scaling-up-with-reducer-and-context - for Context API

// there is Context API element added to this project

export default function TaskApp() {
  return (
    <TasksProvider>
      <h1>Day off in Kyoto</h1>
      <AddTask />
      <TaskList />
    </TasksProvider>
  );
}