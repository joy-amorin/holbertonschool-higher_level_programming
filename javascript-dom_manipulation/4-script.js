const add_itemId = document.querySelector("#add_item")
const myList = document.querySelector(".my_list")

//event controler
add_itemId.addEventListener("click", function(){

    const newItem = document.createElement("li");
    newItem.textContent = "Item"
    myList.appendChild(newItem)

});
