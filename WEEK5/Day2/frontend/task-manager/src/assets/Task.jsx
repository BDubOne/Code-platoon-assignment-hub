const Task = ({taskTile, taskId, taskCompleted}) => {

    const [checked, setChecked] = useState(taskCompleted)
    console.log(props)
    return (
        <li>

            <input
            type="checkbox"
            checked={taskCompleted}
            onChange={(e)=>setChecked(e.target.checked)}

            />
            task
        </li>
    );
}







export default Task