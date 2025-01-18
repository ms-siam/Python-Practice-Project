import pprint
spam = {'mail': 'gmail', 'fname': 'siam', 'lname': 'sarker'}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for K,V in spam.items():
    print('Keys: ' + K + ' Values: ' + V)
if 'gmail' in spam.values():
    print('Yes')
print('My firstname is ' + spam.get('fname', 'Mobarok') + ' and lastname is ' + spam.get('lname', 'Sarker'))

SPAM = "Mymns,ada name is tiam"
count = {}

for letter in SPAM:
    count.setdefault(letter, 0)
    count[letter] += 1

print(pprint.pformat(count))
pprint.pprint(count)

