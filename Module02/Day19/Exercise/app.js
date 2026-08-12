

// let myHeader=document.getElementById("header")

// console.log(myHeader)

// console.log(document)

// console.log(document.querySelectorAll('div'))

// // let cart = document.createElement('strong')
// // cart.textContent= cart
// document.getElementById('welcome').addEventListener('click', ()=>{ alert("button clicked")})

// document.getElementById


// const handleSubmit=(e)=>{
//     e.preventDefault()

//     Email = document.getElementById('email').value
//     password = document.getElementById('pass').value

//     console.log(Email)
//     console.log(password)

// }

// document.getElementById('submit').addEventListener('click', handleSubmit)
// // newDiv.classList.add('blue')



// TODO: Hold items in an array (this is your single source of truth)
let items = [];

// TODO: Select necessary DOM elements (form, input, list, count)

// TODO: Write a render() function to rebuild the list from the array
// 1. Clear the current list (innerHTML = "")
// 2. Loop through the items array
// 3. Create elements, use data-id on each row, and append to the list
// 4. Update the live count paragraph

// let items = [];   // the source of truth
const form = document.querySelector("#add-form");
const nameIn = document.querySelector("#name");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = nameIn.value.trim();
  if (!name) return;
  items.push({ id: Date.now(), name,
  done: false });
  nameIn.value = "";
  render();
});


const list = document.querySelector("#list");
function render() {
  // Logic goes here...


  list.innerHTML = "";
  items.forEach(it => {
    const li = document.createElement("li");
    li.textContent = it.name;
    li.dataset.id = it.id;
    if (it.done) li.classList.add("done");
    const x = document.createElement("button");
    x.textContent = "×"; x.className = "del";
    li.append(x); list.append(li);
});
  count.textContent = items.length + " items"
}

list.addEventListener("click", (e) => {
  const li = e.target.closest("li");
  const id = Number(li.dataset.id);
  if (e.target.matches(".del")) {
    items = items.filter(i => i.id !== id);
} else {
    const it = items.find(i => i.id === id);
    it.done = !it.done;  
 // toggle
  }
    render();
});
// form.addEventListener("submit", (e))



// TODO: Handle form submission
// 1. preventDefault to stop page reload
// 2. Read and validate the input
// 3. Push a new object to the items array (include a unique id and done: false)
// 4. Call render()

// TODO: Set up event delegation on the #list
// 1. Listen for clicks on the parent <ul>
// 2. Use e.target and closest() to find the clicked row
// 3. Determine if the user is toggling ".done" or removing a row
// 4. Update the items array accordingly
// 5. Call render()












