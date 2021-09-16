f = open('CNN_news_report.txt', 'r')

count = 0

while(True):
    read_c = f.read(1)
    if (read_c == '\'' or read_c == '"'):
        while(True):
            #print(read_c)
            read_c = f.read(1)
            if read_c == "\'":
                break
            elif read_c == '\"':
                break
                
    if read_c == '.':
        count += 1
    
    if read_c == '?':
        count += 1
        

print("문장 수는 {count}",count)
f.close
