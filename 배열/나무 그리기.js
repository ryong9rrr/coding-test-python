const height = 7;

let str = "";

for (let i = 0; i < height; i++) {
  for (let j = 0; j < height - i - 1; j++) {
    str += "#";
  }

  for (let j = 0; j < i * 2 + 1; j++) {
    str += "*";
  }

  str += "\n";
}

console.log(str);
/*
######*
#####***
####*****
###*******
##*********
#***********
*************
*/
