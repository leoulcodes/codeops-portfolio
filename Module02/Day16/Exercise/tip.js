

const billRaw = 600
const bill = Number(billRaw)
const partySize=4

let total = (bill >300)? bill + bill*0.1: bill+ bill*0.05

let pricePerPerson= total/partySize

console.log(`You have used Total ${total} ETB and it is ${pricePerPerson} ETB for each`)



