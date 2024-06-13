const price = document.getElementById("price")
const quantity = document.getElementById("quantity")
const totalPrice = document.getElementById("total")


const product = { price: 20, quantity: 5 }
let total = 0

const effect = () => total = product.price * product.quantity;

effect()

function updateUI() {
    price.textContent = product.price
    quantity.textContent = product.quantity
    totalPrice.textContent = total
}

updateUI()
product.price = 50
effect()
updateUI()


Object.keys(product).forEach(key => {
    let value = product[key]
    Object.defineProperty(product, key, {
        get() {
            // updateUI()

            return value;
        },
        set(val) {
            if (!key in this) { return null }
            value = val;
            effect()
            updateUI()
        }
    })
})