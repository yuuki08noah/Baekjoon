fun main() {
    var input: List<String> = readLine().toString().split(" ")
    var m: Int = input[1].toInt()
    var resString = StringBuilder()
    for(i: Int in 1..input[0].toInt()) {
        resString.append(input[0])
    }
    if (resString.length > m) {
        print(resString.toString().substring(0, m))
    } else {
        print(resString.toString())
    }
}