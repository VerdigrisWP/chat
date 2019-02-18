#對話紀錄格式轉換

chat_log = []
with open('input.txt', 'r', encoding='utf-8') as f:
	for line in f:
		line = line.encode('utf-8').decode('utf-8-sig') #解決出現「\ufeff」問題
		chat_log.append(line.strip())

chat_relog = []
for line in chat_log:
	if line == 'Allen' or line == 'Tom':
		name = line + ':'
	else:
		chat_relog.append(name + line)

with open ('output.txt', 'w', encoding='utf-8') as f:
	for line in chat_relog:
		f.write(line + '\n')