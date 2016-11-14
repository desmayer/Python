'''
Guess The Number
- Generate Random Number
- Input
- Check input
- Compare input
- Confirm if number is close to target
- Confirm if number is higher or lower
- Count the number of attempts required
'''
from random import random, sample
# Start Count
count = 0
# Fix Range
start = int(1)
end = int(51)
# Generate the random number
number = random()
randomNumber = int(number * end)
# Debug - Show number
print('Debug:',randomNumber)

# Enter a Number
print('**** Guess the Number between',start,'and',end-1,' ****')
# Check value is INT
while True:
    try:
        # Repeat the input if statement is false
        guess = int(input('** Enter a Number:'))
    except ValueError:
        # Not an INT
        print('------------------------------')
        print('I said a number!') # Error
        count += 1 # Increase count
        continue
    else:
        # Statement is True break the loop
        break

# While loop until result is right
while guess != randomNumber:
    print('------------------------------')
    if guess > end-1 :
        count += 1
        print('** The range is 1 to',end-1,'- Try Again!')
    else :
        diff = guess - randomNumber
        # print('Debug: ',diff)
        if abs(diff) < 6 :
            print('** Getting Warmer!')
        else:
            print('** Getting Colder!')
        # Check if number is too high
        if guess > randomNumber :
            print('** Too High - Guess Again')
            count += 1
        # Check if number is too low
        elif guess < randomNumber :
            print('** Too Low - Guess Again')
            count += 1
    # Enter value again & Check
    while True:
        try:
            guess = int(input('** Enter a Number:'))
        except ValueError:
            # Not an INT
            print('------------------------------')
            print('I said a number!')
            count += 1
            continue
        else:
            break

# When the correct number is picked
count += 1
print('------------------------------')
print('** Well done! The number was',randomNumber)
if count == 1 :
    print('** It only took you',count,'attempt!')
else :
    print('** It only took you', count, 'attempts!')