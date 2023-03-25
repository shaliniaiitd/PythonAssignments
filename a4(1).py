url = 'https://example.com/users/jimmy'
print(url.split('/')[-1])  # / is a separator

# print all the elements till word "example.com" from the url

url = 'https://example.com/users/jimmy'

print(url.split('/')[0:3])


