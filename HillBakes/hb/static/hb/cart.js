
let totalSum = 0
const totals = document.getElementsByClassName('total')
let cart_sum = document.getElementById('cartSum')
// const tot_items = document.getElementsByClassName('total_items')

// for (let total of totals){
//   totalSum += parseFloat(total.textContent)
//   return totalSum
// }
function get_total(){
  // let count=0
  // while(count <= tot_items.length){
    for (let total of totals){
    totalSum += parseFloat(total.textContent)
    console.log(totalSum)
    // count++
  }
  return totalSum
  }
// }

cart_sum.innerHTML = get_total()
// get_total()