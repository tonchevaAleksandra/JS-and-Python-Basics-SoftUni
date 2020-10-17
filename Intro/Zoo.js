function neededMoney(countDogs,countOtherAnimals){
    let priceDogs= 2.50* Number(countDogs);
    let priceForOtherAnimals=4*Number(countOtherAnimals);
    console.log(`${priceDogs+priceForOtherAnimals}lv.`);
}
neededMoney(5,4);