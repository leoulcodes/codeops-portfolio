
// //Our state object to store everything from our API
// const state = {
//     dishes: [],
//     cart: [],
//     search: "",
// }

// const menu1 =document.querySelector("#menu")

// // create our async function loadMenu()

// // const res= fetch("data/menu.json")
// // console.log(res)
// async function loadMenu(){

//     menu1.textContent ="Loading menu..."
//     try{
//         const res = await fetch("data/menu.json")
//         if(!res.ok) {throw new Error("HTTP" + res.status)}
//         state.dishes= await res.json()
//         // console.log(state.dishes)
//         render()


//     }catch(err){
//         console.error("Fetch failed because:",err)
//         menu1.textContent = "could not load the menu."
//     }

// }
// loadMenu()
// // loadMenu()
// function render(){
//     const term = state.search.toLowerCase()
//     const shown = state.dishes.filter(d =>
//         d.name.toLowerCase().includes(term));


//     menu1.innerHTML = shown.map( d => `
//         <article class="dish" data-id="${d.id}">
//             <h3>${d.name}</h3>
//             <p class="price">${d.price}ETB</p>
//             <button class="add">Add</button>
//         </article>`).join("")

//     // renderCart()
// }


// const search1= document.querySelector("#search")

// search1.addEventListener("input", (e)=>{
//     state.search = e.target.value
//     render()
// })


// menu1.addEventListener("click", (e) => {
//     if (!e.target.matches(".add")) return;
//     const id = Number(e.target.closest(".dish").dataset.id);
//     const dish = state.dishes.find(d => d.id === id);
//     const line = state.cart.find(i => i.id === id);
//     if (line) line.qty++;
//     else state.cart.push({ ...dish, qty: 1 });
//     save(); render();
// });
// // remove handled the same way on the cart panel

// const cart1 = document.querySelector("state.dishes.add")


// .addEventListener("click", (e) => {
//     if (!e.target.matches(".rm")) return;
//     const id = Number(e.target.closest("li").dataset.id);
//     state.cart = state.cart.filter(i => i.id !== id);
//     save(); render();
// })

// //totals & persistence

// function cartTotal() {
// return state.cart.reduce((sum, i) =>
// sum + i.price * i.qty, 0);
// }
// function save() {
// localStorage.setItem("addiseats",
// JSON.stringify(state.cart));
// }
// function load() {
// const s = localStorage.getItem("addiseats");
// if (s) state.cart = JSON.parse(s);
// }


// //init
// async function init() {
// load();             
// // restore saved cart
// await loadMenu();   // fetch dishes + render
// }
// init()
// loadMenu()



//-----------------------------------//

/* =========================================================
   ADDIS EATS
   State → Render → Loop
   ========================================================= */


/* =========================================================
   DOM ELEMENTS
   ========================================================= */

const menuEl = document.querySelector("#menu");
const cartEl = document.querySelector("#cart");
const searchEl = document.querySelector("#search");


/* =========================================================
   STATE
   ========================================================= */

const state = {
    dishes: [],
    cart: [],
    search: ""
};


/* =========================================================
   LOAD MENU
   ========================================================= */

async function loadMenu() {

    menuEl.innerHTML = `
        <div class="loading">
            <div class="loading-content">
                <div class="spinner"></div>
                <p>Loading delicious dishes...</p>
            </div>
        </div>
    `;

    try {

        const res = await fetch("data/menu.json");

        if (!res.ok) {
            throw new Error("HTTP " + res.status);
        }

        state.dishes = await res.json();

        render();

    } catch (err) {

        console.error(err);

        menuEl.innerHTML = `
            <div class="no-results">

                <div class="no-results-icon">
                    ⚠️
                </div>

                <h2>Could not load the menu</h2>

                <p>
                    Please make sure the menu.json file is inside
                    the data folder.
                </p>

            </div>
        `;
    }
}


/* =========================================================
   DISH ICON
   ========================================================= */

function getDishIcon(dish) {

    if (dish.name === "Doro Wat") return "🍗";

    if (dish.name === "Shiro") return "🥣";

    if (dish.name === "Kitfo") return "🥩";

    if (dish.name.includes("Tibs")) return "🍖";

    if (dish.name.includes("Firfir")) return "🍳";

    if (dish.name === "Beyaynetu") return "🍛";

    if (dish.name.includes("Wat")) return "🍲";

    if (dish.name === "Gomen") return "🥬";

    if (dish.name === "Atkilt Wot") return "🥕";

    if (dish.name === "Ayibe") return "🧀";

    if (dish.name === "Kocho") return "🍞";

    if (dish.name === "Fuul") return "🫘";

    if (dish.name === "Genfo") return "🥣";

    if (dish.name === "Chechebsa") return "🥞";

    return "🍽️";
}


/* =========================================================
   RENDER MENU
   ========================================================= */

function render() {

    const term = state.search
        .toLowerCase()
        .trim();


    /* Filter dishes */

    const shown = state.dishes.filter(dish =>
        dish.name
            .toLowerCase()
            .includes(term)
    );


    /* No matching dishes */

    if (shown.length === 0) {

        menuEl.innerHTML = `
            <div class="no-results">

                <div class="no-results-icon">
                    🔎
                </div>

                <h2>No dishes found</h2>

                <p>
                    Try searching for another Ethiopian dish.
                </p>

            </div>
        `;

        renderCart();

        return;
    }


    /* Render dishes */

    menuEl.innerHTML = shown.map(dish => `

        <article
            class="dish"
            data-id="${dish.id}"
        >

            <div class="dish-visual">
                ${getDishIcon(dish)}
            </div>


            <span class="category">
                ${dish.category}
            </span>


            <h3>
                ${dish.name}
            </h3>


            ${
                dish.spicy
                    ? `<p class="spicy">🌶️ Spicy</p>`
                    : `<p class="spicy" style="visibility:hidden;">
                        Non-spicy
                       </p>`
            }


            <p class="price">
                ${dish.price.toLocaleString()} ETB
            </p>


            <button
                class="add"
                type="button"
            >
                Add to Cart
            </button>

        </article>

    `).join("");


    /* Cart is also part of render */

    renderCart();
}


/* =========================================================
   CART TOTAL
   ========================================================= */

function cartTotal() {

    return state.cart.reduce(
        (sum, item) =>
            sum + item.price * item.qty,
        0
    );
}


/* =========================================================
   CART ITEM COUNT
   ========================================================= */

function cartItemCount() {

    return state.cart.reduce(
        (sum, item) =>
            sum + item.qty,
        0
    );
}


/* =========================================================
   RENDER CART
   ========================================================= */

function renderCart() {

    const total = cartTotal();

    const itemCount = cartItemCount();


    /* Empty cart */

    if (state.cart.length === 0) {

        cartEl.innerHTML = `

            <div class="cart-header">

                <h2>Your Order</h2>

                <span class="cart-count">
                    0
                </span>

            </div>


            <div class="empty-cart">

                <div class="empty-cart-icon">
                    🛒
                </div>

                <h3>
                    Your cart is empty
                </h3>

                <p>
                    Add some delicious dishes<br>
                    to start your order.
                </p>

            </div>

        `;

        return;
    }


    /* Cart with items */

    cartEl.innerHTML = `

        <div class="cart-header">

            <h2>
                Your Order
            </h2>

            <span class="cart-count">
                ${itemCount}
            </span>

        </div>


        <ul class="cart-list">

            ${state.cart.map(item => `

                <li
                    class="cart-item"
                    data-id="${item.id}"
                >

                    <div class="cart-item-info">

                        <p class="cart-item-name">
                            ${item.name}
                        </p>

                        <p class="cart-item-price">
                            ${item.price.toLocaleString()} ETB each
                        </p>


                        <div class="quantity">

                            <button
                                class="minus"
                                type="button"
                                aria-label="Decrease quantity"
                            >
                                −
                            </button>


                            <span>
                                ${item.qty}
                            </span>


                            <button
                                class="plus"
                                type="button"
                                aria-label="Increase quantity"
                            >
                                +
                            </button>

                        </div>


                        <button
                            class="remove"
                            type="button"
                        >
                            Remove
                        </button>

                    </div>


                    <span class="item-total">
                        ${(item.price * item.qty)
                            .toLocaleString()} ETB
                    </span>

                </li>

            `).join("")}

        </ul>


        <div class="cart-total">

            <div class="total-row">

                <span class="total-label">
                    Total
                </span>

                <span class="total-price">
                    ${total.toLocaleString()} ETB
                </span>

            </div>

        </div>

    `;
}


/* =========================================================
   ADD TO CART
   EVENT DELEGATION
   ========================================================= */

menuEl.addEventListener("click", (e) => {

    if (!e.target.matches(".add")) {
        return;
    }


    /* Find selected dish */

    const id = Number(
        e.target
            .closest(".dish")
            .dataset.id
    );


    const dish = state.dishes.find(
        dish => dish.id === id
    );


    if (!dish) {
        return;
    }


    /* Check if already in cart */

    const line = state.cart.find(
        item => item.id === id
    );


    if (line) {

        /* Increase quantity */

        line.qty++;

    } else {

        /* Add new item */

        state.cart.push({
            ...dish,
            qty: 1
        });

    }


    /* Persist state */

    save();


    /* Re-render everything */

    render();

});


/* =========================================================
   CART EVENTS
   ========================================================= */

cartEl.addEventListener("click", (e) => {

    const cartItem = e.target.closest(".cart-item");


    if (!cartItem) {
        return;
    }


    const id = Number(
        cartItem.dataset.id
    );


    /* Find cart item */

    const item = state.cart.find(
        item => item.id === id
    );


    if (!item) {
        return;
    }


    /* =====================================================
       PLUS
       ===================================================== */

    if (e.target.matches(".plus")) {

        item.qty++;

        save();

        render();

        return;
    }


    /* =====================================================
       MINUS
       ===================================================== */

    if (e.target.matches(".minus")) {

        item.qty--;


        /*
         * If quantity reaches zero,
         * remove the item completely.
         */

        if (item.qty <= 0) {

            state.cart = state.cart.filter(
                cartItem => cartItem.id !== id
            );

        }


        save();

        render();

        return;
    }


    /* =====================================================
       REMOVE
       ===================================================== */

    if (e.target.matches(".remove")) {

        state.cart = state.cart.filter(
            cartItem => cartItem.id !== id
        );


        save();

        render();

    }

});


/* =========================================================
   SEARCH
   ========================================================= */

searchEl.addEventListener("input", (e) => {

    state.search = e.target.value;

    render();

});


/* =========================================================
   SAVE CART
   ========================================================= */

function save() {

    localStorage.setItem(
        "addiseats",
        JSON.stringify(state.cart)
    );

}


/* =========================================================
   LOAD SAVED CART
   ========================================================= */

function load() {

    const saved =
        localStorage.getItem("addiseats");


    if (!saved) {
        return;
    }


    try {

        const parsed =
            JSON.parse(saved);


        if (Array.isArray(parsed)) {

            state.cart = parsed;

        }

    } catch (error) {

        console.error(
            "Could not restore cart:",
            error
        );

        state.cart = [];

    }

}


/* =========================================================
   INIT
   ========================================================= */

async function init() {

    /* Restore cart first */

    load();


    /* Then load menu */

    await loadMenu();

}


/* =========================================================
   START APP
   ========================================================= */

init();


