function campaign(countDays, countcooks, countCakes, countGoffres, countPanCakes){
    let totalCakesSum= +countCakes*45 *+countDays*+countcooks;
    let totalGoffresSum= +countGoffres*5.80*+countcooks*+countDays;
    let totalPancakesSum=+countPanCakes*3.20*+countcooks*+countDays;
    let totalSum= (totalCakesSum+totalGoffresSum+totalPancakesSum)*0.875;
    console.log(totalSum.toFixed(2));

}

