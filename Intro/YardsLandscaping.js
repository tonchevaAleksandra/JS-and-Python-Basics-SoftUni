function yardLandscaping(surface){
    let price= (Number(surface)*7.61);
    let discount= (price*0.18);
    console.log(`The final price is: ${(price-discount).toFixed(2)} lv.`);
    console.log(`The discout is: ${discount.toFixed(2)} lv.`)
}
