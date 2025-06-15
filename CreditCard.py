total=0
sum_even_digit=0
sum_odd_digits=0
card_num=input("Enter Your Credit Number: ")
card_num=card_num.replace("-","")
card_num=card_num.replace(" ","")
masked_card = '*' * (len(card_num) - 4) + card_num[-4:]
card_num=''.join(reversed(card_num))
formatted_masked=' '.join(masked_card[i:i+4] for i in range(0, len(masked_card), 4))
print("Masked card:", formatted_masked)
print(card_num)
for x in card_num [::2]:
    sum_odd_digits+=int(x)

for x in card_num [1::2]:
   x = int(x) * 2
   if x >= 10:
     sum_even_digit += (1 + (x % 10))
   else:
     sum_even_digit += x

total=sum_odd_digits+sum_even_digit
if total%10==0:
    print("VALID")
else:
    print("INVALID")
