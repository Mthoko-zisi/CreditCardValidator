total=0
sum_even_digit=0
sum_odd_digits=0

# Ask user for input and clean it (remove dashes and spaces)
card_num=input("Enter Your Credit Number: ")
card_num=card_num.replace("-","")
card_num=card_num.replace(" ","")

# Mask all digits except the last 4 for privacy
masked_card = '*' * (len(card_num) - 4) + card_num[-4:]
card_num=''.join(reversed(card_num))

# Format the masked card number in groups of 4 for readability
formatted_masked=' '.join(masked_card[i:i+4] for i in range(0, len(masked_card), 4))

# Display the masked version of the card number
print("Masked card:", formatted_masked)
print(card_num)

# Loop through every digit in an odd index
for x in card_num [::2]:
    sum_odd_digits+=int(x)

# Loop through every digit in an even index
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
