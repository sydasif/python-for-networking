"""
5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
"""

with open("show_ip_bgp_summ.txt") as file:
    output = file.read()

bgp_sum = output.splitlines()

first_line = bgp_sum[0].split()
as_num = first_line[-1]

last_line = bgp_sum[3].split()
ip_addr = last_line[0]

print("local AS number:", as_num)
print("BGP peer IP address:", ip_addr)