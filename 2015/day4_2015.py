import hashlib

secret = 'bgvyzdsv'

results = []
for n in range(10000, 999999):
	result = hashlib.md5((secret + str(n)).encode())
	if(result.hexdigest().startswith('000000')):
		results.append((n, result.hexdigest()))

print(results)