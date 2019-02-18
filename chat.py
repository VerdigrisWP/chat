#對話紀錄格式轉換

def open_file(): #定義函數「開啟檔案」
	with open('input.txt', 'r', encoding='utf-8') as f:
		chat_log = []
		for line in f:
			line = line.encode('utf-8').decode('utf-8-sig') #解決出現「\ufeff」問題
			chat_log.append(line.strip())
	return chat_log

def reformate(chat_log): #定義函數「重整格式」
	chat_relog = []
	for line in chat_log:
		if line == 'Allen' or line == 'Tom':
			name = line + ':'
		else:
			chat_relog.append(name + line)
	return chat_relog

def write_file(chat_log): #定義函數「寫入檔案」
	with open ('output.txt', 'w', encoding='utf-8') as f:
		for line in chat_log:
			f.write(line + '\n')

chat_log = open_file()
chat_log = reformate(chat_log)
write_file(chat_log)