def reverse(text):
    return text


def is_palindrome(text):
    return text == reverse(text)


something = input('Enter text:')

print reverse(something)

# if is_palindrome(something):
#     print 'Yes'
# else:
#     print 'No'



