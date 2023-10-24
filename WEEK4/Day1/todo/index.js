const taskInput = document.getElementById('task-input');
const addButton = document.getElementById("add-button");
const taskList = document.querySelector('ul');

 function addTask() {
    const taskIn = taskInput.value.trim();
    
    if (taskIn !== '') {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<span>${taskIn}</span><input type="checkbox" class="mark-complete"/> <button class="remove-task">Squash Beef</button>`;

        taskList.appendChild(listItem);

        taskInput.value = '';
    }
}


addButton.addEventListener('click', addTask);

taskInput.addEventListener('keypress', function(event) {
    if (event.key === "Enter") {
        addTask();
    }
});

taskList.addEventListener('click', function(event) {
    if (event.target.classList.contains('mark-complete')) {
        const taskItem = event.target.parentElement;
        taskItem.querySelector('span').classList.toggle('completed');
    } else if (event.target.classList.contains('remove-task')) {
        const taskItem = event.target.parentElement;
        taskItem.remove();
    }
});