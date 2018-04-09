def find_fem_a(name):
    res=""
    with open('mystem.xml', 'r', encoding='utf-8') as file:
        for line in file:
            if '"A=' in line:
                if ",жен" in line:
                    word=re.findall('>([А-Яа-яЁё]+)<',line)
                    res+=word[0]+", "
        fout=open('femaadj.txt','w',encoding='utf-8')
        fout.write(res)
        fout.close()
    return res

def clear_tags(name):
    with open('mystem.xml', 'r',encoding='utf-8') as file:
        fout=open('result.csv','w',encoding='utf-8')
        for line in file:
            if "<w>" in line:
                lex=re.findall('lex="([А-Яа-яЁё]+)"',line)
                morf=re.findall('gr="(.*)"',line)
                word=re.findall('>([А-Яа-яЁё]+)<',line)
                newline=lex[0]+","+morf[0]+","+word[0]+"\n"
                fout.write(newline)
        fout.close()
