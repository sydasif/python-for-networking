"""
2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
"""

ip_list = ["1.1.1.1", "11.11.11.11", "3.3.3.3", "4.4.4.4", "5.5.5.5"]
ip_list.append('6.6.6.6')
ip_list.extend(['7.7.7.7', '8.8.8.8'])
ip_list2 = ["9.9.9.9", "10.10.10.10"]
new_ip_list = ip_list + ip_list2
print(new_ip_list)
print(f"First IP: {new_ip_list[0]}")
print(f"Last IP: {new_ip_list[-1]}")
new_ip_list.pop(0)
new_ip_list.pop()
new_ip_list[0] = '2.2.2.2'
print(new_ip_list[0])
