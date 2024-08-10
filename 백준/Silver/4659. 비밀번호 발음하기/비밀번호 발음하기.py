import sys
from decimal import Decimal
import decimal

while True:
    input = sys.stdin.readline().strip
    str = input()
    if str == 'end':
        break
    if 'a' not in str and 'e' not in str and 'i' not in str and 'o' not in str and 'u' not in str:
        print(f'<{str}> is not acceptable.')
        continue
    for i in range(len(str)):
        if i < len(str)-1:
            if str[i] == str[i+1] and (str[i:i+2] != 'ee' and str[i:i+2] != 'oo'):
                print(f'<{str}> is not acceptable.')
                break
        if i < len(str)-2:
            if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u':
                if (str[i+1] == 'a' or str[i+1] == 'e' or str[i+1] == 'i' or str[i+1] == 'o' or str[i+1] == 'u') and (str[i+2] == 'a' or str[i+2] == 'e' or str[i+2] == 'i' or str[i+2] == 'o' or str[i+2] == 'u'):
                    print(f'<{str}> is not acceptable.')
                    break
            if str[i] != 'a' and str[i] != 'e' and str[i] != 'i' and str[i] != 'o' and str[i] != 'u':
                if (str[i + 1] != 'a' and str[i + 1] != 'e' and str[i + 1] != 'i' and str[i + 1] != 'o' and str[i + 1] != 'u') and (str[i + 2] != 'a' and str[i + 2] != 'e' and str[i + 2] != 'i' and str[i + 2] != 'o' and str[i + 2] != 'u'):
                    print(f'<{str}> is not acceptable.')
                    break
    if i == len(str)-1:
        print(f'<{str}> is acceptable.')
    else:
        continue
