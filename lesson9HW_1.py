a={'A001':'品項:小熊軟糖 20元','A002':'品項:冰棒 25元','A003':'品項:王子麵 10元','A004':'品項:汽水 30元'}
b=input('要查詢的貨號?')
if b in a:
    print(a[b])
else:
    print('無此貨號，請新增貨號')
    aaa=input('輸入品項')
    bbb=input('輸入價錢')
    a[b]='品項:'+aaa+' '+bbb+'元'
#print(a)