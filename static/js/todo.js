const btnDone = document.getElementById("btn-done");
const btnActive = document.getElementById("btn-active");
const todoForm = document.getElementById("todo-form");
const todoItemsActive = document.getElementById("todo-items-active");
const todoItemsDone = document.getElementById("todo-items-done");

btnDone.addEventListener("click", () => {
    btnActive.classList.remove("active");
    btnDone.classList.remove("active");
    btnDone.classList.add("active");
    todoItemsActive.style.display = "none";
    todoItemsDone.style.display = "block";
});

btnActive.addEventListener("click", () => {
    btnDone.classList.remove("active");
    btnActive.classList.remove("active");
    btnActive.classList.add("active");
    todoItemsActive.style.display = "block";
    todoItemsDone.style.display = "none";
});

const todoItemsCb = document.getElementsByClassName("todo-item-cb");
for(let i = 0; i < todoItemsCb.length; i++) {
    todoItemsCb[i].addEventListener("click", () => {
        todoItemsCb[i].querySelector("input[type='checkbox']").click();
    });
}