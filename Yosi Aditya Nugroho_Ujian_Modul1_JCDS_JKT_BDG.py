# Soal 1
print('\nSoal 1')
def create_phone_number(number):
    if any(map(lambda x: x.isalpha(), number)):
        print('Invalid Input. No Alphabet')
    elif any(map(lambda x: x not in '1234567890-', number)):
        print('Invalid Input. No Symbols.')
    elif '-' in number:
        print('Input only positive number.')
    elif len(number) != 10:
        print('Digits must be in length of 10, not more or less.')
    else:
        print(f'({number[:3]}) {number[3:6]}-{number[6:]}')

# number = input('Input your phone number: ')
number = '1234567890'
create_phone_number(number)

# number = input('Input your phone number: ')
number = '2345-678901'
create_phone_number(number)

# number = input('Input your phone number: ')
number = 'abc1234556'
create_phone_number(number)

# number = input('Input your phone number: ')
number = '1234567'
create_phone_number(number)

# number = input('Input your phone number: ')
number = '12345678901'
create_phone_number(number)

# number = input('Input your phone number: ')
number = '!@#$%^&*()'
create_phone_number(number)

# number = input('Input your phone number: ')
number = '123!@#!'
create_phone_number(number)

# Soal 2
print('\nSoal 2')
def moveZeros(list_input):
    zeros = list(filter(lambda x: x==0 and not isinstance(x, bool), list_input))
    not_zeros = list(filter(lambda x: not(x==0 and not isinstance(x, bool)), list_input))
    print(f'result: {not_zeros + zeros}')

moveZeros([False, 1, 0, 1, 2, 0, 1, 3, 'a'])
moveZeros([0, 0, 0, 'Test', 0, 3, 'a', True, False])
moveZeros([0, True, True, False, 'a', 'b', 1, 1, 1])
moveZeros([0, 0, 0, 'Test', 0, 3, 'a', 0, '0', True, '0', False])

# Soal 3
print('\nSoal 3')
class Statistic():
    def __init__(self):
        pass

    def mean(self, input_list):
        if any(filter(lambda x: type(x) != int, input_list)):
            return 'Invalid Input! All values must be Integer.'
        else:
            mean = sum(input_list)/len(input_list) 
            return round(mean, 3)

    def median(self, input_list):
        if any(filter(lambda x: type(x) != int, input_list)):
            return 'Invalid Input! All values must be Integer.'
        else:
            input_list.sort()
            median_idx = 0
            if len(input_list)%2 == 0:
                median_idx = int(len(input_list)/2)
                median = (input_list[median_idx] + input_list[median_idx-1])/2
            else:
                median_idx = int(len(input_list)/2)
                median = input_list[median_idx]
            return round(median, 3)
            

    def mode(self, input_list):
        if any(filter(lambda x: type(x) != int, input_list)):
            return 'Invalid Input! All values must be Integer.'
        else:
            counter = dict()
            for elem in input_list:
                if elem not in counter:
                    counter[elem] = 1
                else:
                    counter[elem] += 1

            max_count = 0
            for value in counter.values():
                max_count = max(value, max_count)
            mode_list = [k for k,v in counter.items() if v == max_count] 
            if len(mode_list) == 1:
                return mode_list[0]
            else:
                return 'tidak ada modus'
                
    def std(self, input_list):
        if any(filter(lambda x: type(x) != int, input_list)):
            return 'Invalid Input! All values must be Integer.'
        else:
            mean = sum(input_list)/len(input_list)
            variance_list = list(map(lambda x: (x-mean)**2, input_list))
            std = (sum(variance_list)/len(input_list))**0.5
            # Need to round the result?
            return round(std, 3)

st = Statistic()
print('\nCase 1')
print(st.mean([1, 2, 3, 4, 5, 'a']))
print(st.median([1, 2, 3, 4, 5, 'a']))
print(st.mode([1, 2, 3, 4, 5, 'a']))
print(st.std([1, 2, 3, 4, 5, 'a']))

print('\nCase 2')
print(st.mean([12, 10, 10, 10, 10]))
print(st.median([12, 10, 10, 10, 10]))
print(st.mode([12, 10, 10, 10, 10]))
print(st.std([12, 10, 10, 10, 10]))

print('\nCase 3')
print(st.mean([4, 5, 2, 1, 6, 7]))
print(st.median([4, 5, 2, 1, 6, 7]))
print(st.mode([1, 2, 4, 5, 6, 7]))
print(st.std([1, 2, 4, 5, 6, 7]))

print('\nCase 4')
print(st.mean([1, 2, 4, 4, 5, 6, 7, 7]))
print(st.median([1, 2, 4, 4, 5, 6, 7, 7]))
print(st.mode([1, 2, 4, 4, 5, 6, 7, 7]))
print(st.std([1, 2, 4, 4, 5, 6, 7, 7]))