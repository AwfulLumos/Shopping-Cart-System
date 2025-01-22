const API_BASE_URL = "http://127.0.0.1:8000";

// Fetch available products
async function fetchProducts() {
    const response = await fetch(`${API_BASE_URL}/view_items`);
    const data = await response.json();

    const productsList = document.getElementById("products-list");
    productsList.innerHTML = ""; // Clear previous products
    data.products.forEach((product) => {
        const li = document.createElement("li");
        li.textContent = `${product.item} - $${product.price} (${product.dimension})`;
        productsList.appendChild(li);
    });
}

// Add item to the cart
async function addItemToCart() {
    const itemName = document.getElementById("item-name").value;
    const itemPrice = parseFloat(document.getElementById("item-price").value);

    if (!itemName || !itemPrice) {
        alert("Please enter both item name and price.");
        return;
    }

    const response = await fetch(`${API_BASE_URL}/add_item`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ item: itemName, price: itemPrice }),
    });

    const data = await response.json();
    document.getElementById("add-item-message").textContent = data.message;

    // Clear input fields
    document.getElementById("item-name").value = "";
    document.getElementById("item-price").value = "";
}

// View cart items
async function viewCart() {
    const response = await fetch(`${API_BASE_URL}/view_cart`);
    const data = await response.json();

    const cartList = document.getElementById("cart-list");
    cartList.innerHTML = ""; // Clear previous cart items
    if (typeof data.cart === "string") {
        cartList.textContent = data.cart; // If cart is empty
    } else {
        data.cart.forEach((item) => {
            const li = document.createElement("li");
            li.textContent = item;
            cartList.appendChild(li);
        });
    }
}

// Fetch total price
async function fetchTotalPrice() {
    const response = await fetch(`${API_BASE_URL}/total_price`);
    const data = await response.json();
    document.getElementById("total-price").textContent = data.total_price;
}
