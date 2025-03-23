//Write a kotlin program for factorial of number.

fun main(){
	println("Enter a nmber to find it's factorial:")

	val number = readLine()!!.toInt()

	var factorial = 1

	for(i in 1..number){
		factorial*=i
	}
	println("The factorial of $number is $factorial")
}	