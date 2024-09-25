#include <iostream>
#include <cmath>
#include <complex>
#include <string>
#include <vector>

using namespace std;

void bit_reverse(complex<double> arr[], int n) {
    int j = 0;
    for (int i = 1; i < n; i++) {
        int bit = n >> 1;
        while (j >= bit) {
            j -= bit;
            bit >>= 1;
        }
        j += bit;
        if (i < j) {
            swap(arr[i], arr[j]);
        }
    }
}

void fft(complex<double> arr[], int n, bool invert) {
    bit_reverse(arr, n);
    
    for (int len = 2; len <= n; len <<= 1) {
        double ang = 2 * M_PI / len * (invert ? -1 : 1);
        complex<double> wlen(cos(ang), sin(ang));
        for (int i = 0; i < n; i += len) {
            complex<double> w(1);
            for (int j = 0; j < len / 2; j++) {
                complex<double> u = arr[i + j];
                complex<double> v = arr[i + j + len / 2] * w;
                arr[i + j] = u + v;
                arr[i + j + len / 2] = u - v;
                w *= wlen;
            }
        }
    }
    if (invert) {
        for (int i = 0; i < n; i++) {
            arr[i] /= n;
        }
    }
}

void str_to_array(const string& str, complex<double> arr[], int n) {
    int str_len = str.length();
    for (int i = 0; i < str_len; i++) {
        arr[i] = complex<double>(str[str_len - 1 - i] - '0', 0);
    }
    for (int i = str_len; i < n; i++) {
        arr[i] = 0;
    }
}

void multiply(const string& a, const string& b, vector<int>& res) {
    int n = 1;
    while (n < a.length() + b.length()) n <<= 1;  // n을 두 배로 조정

    complex<double> A[n], B[n];
    str_to_array(a, A, n);
    str_to_array(b, B, n);

    fft(A, n, false);
    fft(B, n, false);

    complex<double> C[n];
    for (int i = 0; i < n; i++) {
        C[i] = A[i] * B[i];
    }

    fft(C, n, true);

    long long carry = 0;
    res.resize(n);  // 결과 벡터 크기 조정
    for (int i = 0; i < n; i++) {
        res[i] = round(C[i].real()) + carry;
        carry = res[i] / 10;
        res[i] %= 10;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string first, second;
    cin >> first >> second;

    if (first == "0" || second == "0") {
        cout << "0\n";
        return 0;
    }

    vector<int> result;
    multiply(first, second, result);

    // 앞에서부터 불필요한 0 제거
    int start = result.size() - 1;
    while (start > 0 && result[start] == 0) {
        start--;
    }

    // 결과 출력
    for (int i = start; i >= 0; i--) {
        cout << result[i];
    }
    cout << endl;

    return 0;
}
