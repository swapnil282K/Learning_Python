# Approach1

# f=open('data.txt','r')
# for line in f:
#   print(line)

# f.close()

# Approach2

# with open('data.txt','r') as f:
#   # for line in f:
#   #  print(line)
#      print(f.read(10))
#      f.seek(5)
#      print(f.read(10))
lines_data=["yjfj\n","yjfvj\n","hfh\n"]
with open('write.txt','w') as f:
  f.write('Swapnil\n')
  f.writelines(lines_data)