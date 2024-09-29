my_list = [1, 2, "3", 4.5]

# Convert strings to numbers and filter out others
numeric_values = [float(x) if isinstance(x, str) and x.isdigit() else x 
                  for x in my_list if isinstance(x, (int, float)) or (isinstance(x, str) and x.isdigit())]

result = sum(numeric_values)
print(result)  # Output: 10.5
