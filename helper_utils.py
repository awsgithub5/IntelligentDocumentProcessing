import re

def clean_string(string):
    r='[^a-zA-Z\s]'
    tmp=re.sub(r,'',string.strip()).strip()
    return tmp
    
def clean_keys(x):
    res=x.get('')
    if res is not None:
        res2=res[0].split(':')
        x.popitem()
        del x['']
        x.update({res2[0].strip():res2[1]})
    return x

def get_mapped_key(tmp):
    #print('+++++++++++++++++++++++++')
    res=None
    for k,v in meta.items():
        if tmp[0] in v:
            #orig_dict.update()
            res={k:tmp[1]}
            break
        else:
            x=1
    
    if not res:
        res={'other':[{tmp[0]:tmp[1]}]}
    print('>><<',res)
    return res
    
def clean_dict_keys(tmp_dict):
    new_dict=dict()
    for k,v in tmp_dict.items():
        new_dict.update({clean_string(k):v})
    print('*'*50,new_dict)
    clean_key_dict=clean_keys(new_dict)
    
    orig_dict=dict({'other':[]})

    for i in clean_key_dict.items():
        res=get_mapped_key(i)
        if list(res.keys())[0]=='other':
            orig_dict['other'].extend(res['other'])
        else:
            orig_dict.update(res)
    print('^'*50,orig_dict)
    return orig_dict
    
def add_zero(num):
    return '0'+str(num)
    
def conv_date(date):
    print("Inside CONV DATE FUNCTION:-",date)
    date_split=date.split()
    
    day=date_split[0].lower().replace('st','').replace('th','').strip()
    month=date_split[1].replace(', ','').replace(',','').strip()
    year=date_split[2].strip()
    
    from datetime import datetime
    mname = month
    month = datetime.strptime(mname, '%B').month
    month=add_zero(month) if len([i for i in str(month)])==1 else month
    date='{}/{}/{}'.format(day,month,year)
    print("OUTPUT DATE AFTER ...:-",date)
    return date

    

    
    