let marks=[10,20,30,40,50]
const doubled=marks.map(x=>x*2)
console.log(doubled)

let arr=[1,2,3,4,5]
let even_arr=arr.filter(n=>n%2===0)
console.log(even_arr)


city=["delhi","mumbai","bangalore"]
let city_length=city.filter(name=>name.length>5)
console.log(city_length)

num = [1,2,4,-4,-5]
let positive_num=num.filter(n=>n>0)
console.log(positive_num)

num = [10,20,30,40,50]
let ex_num=num.filter(n=>n!==40)
console.log(ex_num)

num = [10,20,30,40,50,60,40,50,40,60,80]
let ex1_num=num.filter(n=>n==40)
console.log(ex1_num)

num = [10,20,30,40,50,60,40,50,40,60,80]
let ex2_num=num.filter(n=>n==40||n==50)
console.log(ex2_num)

const result=arr.reduce((sum, n) => sum + n);
console.log(result);

for (let i = 0;i<arr.length;i++) {
  console.log(arr[i]);
}

for (let n of arr) {
  console.log(n);
}

for (let index in arr) {
  console.log(index);
}
