nums = [1, 2, 3, 4, 5]

# for num in nums:
#     if num == 3:
#         print(f'Found it - {num}')
#         break
#     print(num)


# for num in nums:
#     if num == 3:
#         print(f'Ignoring with continue stmt - {num}')
#         continue
#     print(num)


for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(1, 11):
    print (i)