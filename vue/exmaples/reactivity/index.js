// const price = document.getElementById("price")
// const quantity = document.getElementById("quantity")
// const totalPrice = document.getElementById("total")

// function reactive(obj) {
//     const keys = Object.keys(obj); // get keys
//     keys.forEach((key) => {
//         let objValue = obj[key];
//         Object.defineProperty(obj, key, {
//             get() {
//                 console.log('getter is hitting')
//                 return objValue
//             },
//             set(newValue) {
//                 console.log('setter is hitting')
//                 objValue = newValue;
//                 if (key in this) getTotal()
//             }
//         })
//     })
//     return obj;
// }

class Dep {
    constructor() {
        this.subscribe = new Set()
    }
    track(key) {

    }
    trigger(key) { }
}
function reactive(target) {
    return new Proxy(target, {
        get(target, key, receiver) {
            return Reflect.get(target, key, receiver)
        },
        set(target, key, newValue, receiver) {
            const result = Reflect.set(target, key, newValue, receiver)
            getTotal()
        }
    })
}




const product = reactive({ price: 20, quantity: 5 })
let total = 0
const getTotal = () => total = product.price * product.quantity;





