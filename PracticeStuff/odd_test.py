#mylist = list()
#for _ in range(10):
 #   while True:
  #      try:
   #         i = int(raw_input("enter num: "))
    #        if i & 1:
     #           mylist.append(i)
      #      break
       # except ValueError:
        #    print ("Enter only numbers!")
			
			
numbers = [int(raw_input("enter num: ")) for _ in range(10)]
odd_numbers = [n for n in numbers if n % 2 == 1]
message = (str(max(odd_numbers)) if odd_numbers else "no odd integers were entered")
print(message)