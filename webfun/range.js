function range(a, b, skip){
    
    for (x=a;x<=b;x++) {
    if (x <= b && x !== skip) {
		console.log(x)
	}
	else if(x == skip) {
		continue;
	}
}}