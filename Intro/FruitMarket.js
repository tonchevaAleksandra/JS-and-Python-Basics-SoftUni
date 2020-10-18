function costs(strawberryPrice, quantityBananas, quantityOranges,quantityRaspberries, quantityStrawberries){
    let priceRaspberries=+strawberryPrice*0.5;
    let priceOranges=priceRaspberries*0.6;
    let priceBananas=priceRaspberries*0.2;
    let totalPrice= priceRaspberries*quantityRaspberries + strawberryPrice
     *quantityStrawberries+quantityOranges*priceOranges+priceBananas*quantityBananas;
     console.log(totalPrice);
}
