export default function tasksReducer(tasks, action) {
  // logic lives here, returns next state for React to set
  // declare the current state (task) as 1st argument
  // declare action Object as 2nd argument - i.e. action is an Oject with properties, like action.id, action.text
  // return next state from the reducer
  switch (action.type) {
    case 'added': {
      return [
        ...tasks,
        {
          id: action.id,
          text: action.text,
          done: false,
        },
      ];
    }
    case 'changed': {
      return tasks.map((t) => {
        if (t.id === action.task.id) {
          return action.task;
        } else {
          return t;
        }
      });
    }
    case 'deleted': {
      return tasks.filter((t) => t.id !== action.id);
    }
    default: {
      throw Error('Unknown action: ' + action.type);
    }
  }
}
  