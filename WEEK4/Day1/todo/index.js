const taskInput = document.getElementById('task-input');
const addButton = document.getElementById("add-button");
const taskList = document.querySelector('ul');

addTask = () => {
    const taskIn = taskInput.value.trim();
    
    if (taskIn !== '') {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<span>${taskIn}</span> <button class="mark-complete">Mark Comlete</button>`;

        taskList.appendChild(listItem);

        taskInput.value
    }
}

addButton.addEventListener('click', addTask);

taskInput.addEventListener('keypress', function(event) {
    if (event.key === "Enter") {
        addTask();
    }
});