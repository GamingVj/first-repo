//Write a program of kotlin ot check the string is palindrome or not

fun main()
{
	println("Enter a string to check if it is a palindrome:")
	val input = readline()!!
	val cleanedInput = input.replace(" "," ").tolowerCase()
	val reversedInput = cleanedInput.reversed()
	if (cleanedInput == reversedInput){
		println("\"$input\"is a palindrome")
	}
	else{
		println("\"$input\"is not a palindrome")

	}
}