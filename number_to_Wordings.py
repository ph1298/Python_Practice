# Program to express a 2 digit number in number system wordings

def wordings(num):
    list_11_to_19 = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    list_ten_mult = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    list_ones = [' one', ' two', ' three', ' four', ' five', ' six', ' seven', ' eight', ' nine']
    if (num % 10 == 0):
        index = int((num / 10) - 1)
        return list_ten_mult[index]
    elif (num < 20):
        index = int((num % 10) - 1)
        return list_11_to_19[index]
    else:
        tens = int(num / 10)
        ones = int(num % 10)
        return list_ten_mult[tens - 1] + list_ones[ones - 1]


inp_str = input("Enter a two digit number: ")
try:
    num = int(inp_str)
except:
    print("Enter a valid two digit numnber!")
    quit()

if num >= 100 or num <= 9:
    print("Enter a valid two digit number!")
    quit()

print("Entered number in wordings: ")
print(wordings(num))
