f = open('data.txt', 'r+')

# Read the entire file
data = f.readline ()

# Print the data
print(data)

#Write to the file
f.write('This is a new line')

# Close the file
f.close()