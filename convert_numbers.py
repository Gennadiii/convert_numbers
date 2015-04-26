def convert_n_to_m(x, n, m):

    if isinstance(x, list) or isinstance(x, float):
        return False

    x_list = []
    ten = 0
    result_list = []
    alphabet = {}
    alphabet_for_ten = {}
    alphabet_list = ['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    result = ''

    x = str(x)

    for j in range(len(alphabet_list)):
        alphabet[j] = alphabet_list[j]

    for j in range(len(alphabet_list)):
        alphabet_for_ten[alphabet_list[j]] = j

    if n > 10: # Case when number sustem is more than 10
        x = x.upper()
        for number in x: # Convert letters into numbers
            x_list.append(alphabet_for_ten[number])
        x_list.reverse()

        for number in x_list: # Check if number is right for chosen system
            if number >= n:
                return False
            
        for j in range(len(x_list)): # Convert number to 10 sustem
            ten += x_list[j] * (n ** j)
            
        while ten > 0:
            result_list.append(alphabet[ten % m])
            ten /= m
            ten = int(ten)
        result_list.reverse()
        
        for number in result_list:
            result += number
            
        return result
   
    for number in x:
        if number not in alphabet_list or int(alphabet_for_ten[number]) >= n:
            return False  # Check if number is right for chosen system
        x_list.append(int(alphabet_for_ten[number])) # Convert letters into numbers
    x_list.reverse()

    if int(x) == 0:
        return 0

    for j in range(len(x_list)): # Convert number to 10 sustem
        ten += x_list[j] * (n ** j)

    if m < 2:
        return '0' * ten

    while ten > 0:
        result_list.append(alphabet[ten % m])
        ten /= m
        ten = int(ten)
    result_list.reverse()

    for number in result_list:
        result += number

    return result

while True:
    num = input('Input a number: ')
    num_system = int(input('Input a system of a number: '))
    desired_system = int(input('Input a system in which you want to convert your number: '))
    print(convert_n_to_m(num, num_system, desired_system))
    input()
