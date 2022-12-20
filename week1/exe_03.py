"""
3.   Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator. The second variable should use all upper case characters with underscore as the word separator. The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
"""

ip_addr = "3001:0da8:75a3:0000:0000:8a2e:0370:873"
IP_ADDR = "3001:0da8:75a3:0000:0000:8a2e:0370:6547"
ip_v6_Addr = "3001:0da8:75a3:0000:0000:8a2e:0370:9123"

var1 = ip_addr == IP_ADDR
var2 = ip_addr != ip_v6_Addr

print(var1)
print(var2)