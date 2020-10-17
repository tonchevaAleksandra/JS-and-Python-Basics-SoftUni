function createProjects(name, count){
    let hours= 3*Number(count);
    console.log(`The architect ${name} will need ${hours} hours to complete
    ${count} project/s.`)
}
createProjects('George', 4);