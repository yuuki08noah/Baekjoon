import kotlin.math.max

fun main() {
    var n: Int = readLine().toString().toInt()
    var arr = mutableListOf<Double>()
    for(i in 1..n) {
        var f: Double = readLine()!!.toDouble()
        arr.add(f)
    }
    for(i in 1..n-1) {
        arr[i] = max(arr[i], arr[i-1] * arr[i])
    }
    println(String.format("%.3f", arr.maxOrNull()))
}