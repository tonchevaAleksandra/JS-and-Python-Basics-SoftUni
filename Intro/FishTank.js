function waterForTank(length, width, height, percent){
let tankVolume= +length*+width*+height;
let totalLittersWatter= (tankVolume*(1-+percent/100))*0.001;
console.log(totalLittersWatter);

}
