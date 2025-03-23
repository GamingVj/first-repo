fun main() {
    println("Prime numbers between 1 and 100 are:")
    for (num in 2..100) {
        var isPrime = true
        for (i in 2 until num) {
            if (num % i == 0) {
                isPrime = false
                break
            }
        }
        if (isPrime) {
            print("$num ")
        }
    }
}
