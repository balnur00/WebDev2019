function get_todos() {
    var todos = new Array;
    var todos_str = localStorage.getItem('todo');
    if (todos_str !== null) {
        todos = JSON.parse(todos_str); 
    }
    return todos;
}
 
function add() {
    var task = document.getElementById('task').value;
 
    var todos = get_todos();
    todos.push(task);
    localStorage.setItem('todo', JSON.stringify(todos));
 
    show();
 
    return false;
}
 
function remove() {
    var id = this.getAttribute('id');
    var todos = get_todos();
    todos.splice(id, 1);
    localStorage.setItem('todo', JSON.stringify(todos));
 
    show();
 
    return false;
}

function boxChecked(event) {
    const element = event.target;
    if(element.type === "checkbox") {
        element.parentNode.style.textDecoration = "line-through";
    }
}

/*function checkes(){
    var id = this.getAttribute('id');
    var checBox = this.getElementsByClassName('check');
    var todos = get_todos();
    
    if(checBox.checked){
        todos[id].style.textDecoration="line-through"
    }else{
        todos[id].style.textDecoration="none"
    }

    var id = this.getAttribute('id');
    if (todos[id].checked){
        todos[id].innerHTML = '<del>' + todos[id] + '</del>';
    }else{
        todos[id].innerHTML = todos[id];
    }
    
}*/

function show() {
    var todos = get_todos();
 
    var html = '<ul>';
    for(var i=0; i<todos.length; i++) {
        html += '<li>' +'<input type="checkbox" class="check" id="' + i +'"/>' + todos[i] + '<button class="remove" id="' + i  + '"><i class="fa fa-trash-o" style="font-size:20px;color:red"></i></button>' + '</li>';
    };
    html += '</ul>';
 
    document.getElementById('todos').innerHTML = html;
 
    var buttons = document.getElementsByClassName('remove');
    for (var i=0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', remove);
    };
    var items = document.getElementsByClassName('check');
    for (var i=0; i < items.length; i++) {
        items[i].addEventListener('click', boxChecked);
    };

   
}


 
document.getElementById('add').addEventListener('click', add);
show();
