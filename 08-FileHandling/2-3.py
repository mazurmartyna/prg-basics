###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file, 'r') as file:
   content = file.read()

# write the content to the target file (copy)
with open(target_file, 'w') as file:
   content2 = file.write(content)

print('The copy has been written successfully :)')