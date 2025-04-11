s = 'spam'
t = list(s)
print(t)
# ['s', 'p', 'a', 'm']

s = 'suspirando por los fiordos'
t = s.split()
print(t)
# ['suspirando', 'por', 'los', 'fiordos']
print(t[2])
# los

s = 'spam-spam-spam'
delimiter = '-'
t=s.split(delimiter)
print(t)
# ['spam', 'spam', 'spam']

t = ['suspirando', 'por', 'los', 'fiordos']
delimiter = ' '
s= delimiter.join(t)
print(s)
# 'suspirando por los fiordos'

algunos = [1, 9, 21, 10, 16]
print(9 in algunos)
# True
