function neededBudget(input){
    let rentForHall= Number(input);
    let cakePrice= rentForHall*0.2;
    let bevarage=cakePrice*0.55;
    let animation=rentForHall/3;
    let totalSum= rentForHall+cakePrice+bevarage+animation;
    console.log(totalSum);
}
