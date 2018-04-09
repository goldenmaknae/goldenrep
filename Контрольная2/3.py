def find_fem_a(name):
    res=""
    with open('file.xml', 'r', encoding='utf-8') as file:
        for line in file:
            if 'type=' in line:
                if "f.+?" in line:
                    word=re.findall('>([A-Za-z]+)<',line)
                    res+=word[0]+", "
        fout=open('nwords.txt','w',encoding='utf-8')
        fout.write(res)
        fout.close()
    return res

def clear_tags(name):
    with open('file.xml', 'r',encoding='utf-8') as file:
        fout=open('result.csv','w',encoding='utf-8')
        for line in file:
            if "<w>" in line:
                lex=re.findall('lex="([A-Zа-z]+)"',line)
                morf=re.findall('gr="(.*)"',line)
                word=re.findall('>([A-Zа-z]+)<',line)
                newline=lex[0]+","+morf[0]+","+word[0]+"\n"
                fout.write(newline)
        fout.close()
