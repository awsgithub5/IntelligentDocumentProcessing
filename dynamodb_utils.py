def get_first_value(orig_res):
    new=dict()
    print(orig_res)
    for k,v in orig_res.items():
        if k=='other':
            new[k]=v
        elif k=='account_no' or k=='date':
            if type(v) == list:
                print("inside list.......",v)
                new[k]=str(v[0]).strip()
            else:
                print("dnejbdjewbjedjwe********")
                new[k]=str(v).strip()
        elif k=='invoice_no':
            new[k]=str(v[0]).strip()
        else:
            new[k]=v[0].strip()
    print("*****************")
    new['total_amt']='$ '+new['total_amt'].replace('$','').replace(' ' ,'').strip()
    new['date']=new['date'].replace('.','/')
    print(new)
    return new
    
def put_data(textract_result):
    dynamodb = boto3.resource('dynamodb')
    Invoicedata = dynamodb.Table('Invoice-data')
    
    input_result = get_first_value(textract_result)
    
    Invoicedata.put_item(Item=input_result)