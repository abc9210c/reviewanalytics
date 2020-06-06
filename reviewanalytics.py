data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count +=1
		if count & 1000 == 0:
		    print(len(data))
print('檔案讀取完,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	print(sum_len)
print('平均是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')

bad = []
for d in data:
	if 'good' in d:
		bad.append(d)
print('一共有', len(bad), '筆資料')

#good = [d for d in data if 'good' in d]
#print(good)

#bad = ['bad' in d for d in data]
#print(bad)

#bad = []
#for d in data:
#	bad.append('bad' in d)
