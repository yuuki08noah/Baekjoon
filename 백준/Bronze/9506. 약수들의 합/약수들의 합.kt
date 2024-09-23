import kotlin.math.sqrt

fun main() {
    while(true) {
        val n: Int = readLine().toString().toInt()
        var sum: Int = 0
        var arr = mutableListOf<Int>()
        if (n == -1) {
            break
        }
        for(i in 1 until n) {
            if ((n % i) == 0) {
                sum += i
                arr.add(i)
            }
        }
        if (sum == n) {
            println("$n = " + arr.joinToString(" + "))
        }
        else {
            println("$n is NOT perfect.")
        }
    }

}