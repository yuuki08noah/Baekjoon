import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import static java.lang.Integer.parseInt;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    int index = 1;
    while (true) {
      String str = reader.readLine();
      String[] arr = str.split(" ");
      if(arr[0].equals("0") && arr[1].equals("0") && arr[2].equals("0")) {
        break;
      }
      int res = parseInt(arr[2]) / parseInt(arr[1]) * parseInt(arr[0]);
      res += Math.min(parseInt(arr[2]) % parseInt(arr[1]), parseInt(arr[0]));  // if quotient is less
      System.out.println("Case " + index + ":" + " " + res);
      index++;
    }
  }
}
