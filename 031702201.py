#-*- coding:UTF_8 -*-
import re
import json


client={
    '姓名':'',
    '手机':'',
    '地址':[],
}
addr=input()
addr=addr[:-1]#删掉末尾的.号

#获取难度
a0=addr.split(r'!')#删除感叹号
dif=a0[0]

#获取姓名
n0=a0[1].split(r',')
name=n0[0]
client['姓名']=name

#获取电话号码
telnum=re.findall(r'\d{11}',n0[1])
client['手机']=telnum
addr=re.sub(r'\d{11}','',n0[1])#删去号码得到纯地址字符串

#一级（省、直辖市、自治区）
if '省' not in addr:
    if '内蒙古' in addr:
        p='内蒙古'+'自治区'
        addr=addr.replace(p,'',1)#删去一级地址
    elif '广西'in addr:
        p='广西'+'壮族自治区'
        addr=addr.replace(p,'',1)
    elif '宁夏'in addr:
        p='宁夏'+'回族自治区'
        addr=addr.replace(p,'',1)
    elif '新疆'in addr:
        p='新疆'+'维吾尔自治区'
        addr=addr.replace(p,'',1)
    elif '西藏' in addr:
        p='西藏'+'自治区'
        addr=addr.replace(p,'',1)
    elif '北京' in addr:
        p='北京'
        addr=addr.replace(p,'',1)
    elif '上海' in addr:
        p='上海'
        addr=addr.replace(p,'',1)
    elif '天津' in addr:
        p='天津'
        addr=addr.replace(p,'',1)
    elif '重庆' in addr:
        p='重庆'
        addr=addr.replace(p,'',1)
    elif '黑龙江'in addr:
        p='黑龙江'+'省'
        addr=addr.replace(p,'',1)
    else:
        p=addr[:2]+'省'
        addr=addr.replace(p,'',1)
elif '省' in addr:
    p=re.sub(r'省.*$',"", addr)
    p+='省'
    addr=addr.replace(p,'',1)
client['地址'].append(p)

#二级
second=['市','自治州','盟','区']
for two in second:
    if two in addr:
        ci=re.sub(two+'.*$',"", addr)
        ci+=two
        addr=addr.replace(ci,'',1)#删去二级地址
        break
    else:
        ci=""

client['地址'].append(ci)

#三级
third=['区','县','市','自治县','旗','自治旗','林区','特区']
for three in third:
    if three in addr:
        co=re.sub(three+'.*$',"", addr)
        co+=three
        addr=addr.replace(co,'',1)#删去三级地址
        break
    else:
        co=""

client['地址'].append(co)

#四级
forth=['街道','镇','乡','民族乡','苏木','民族苏木','区']
for four in forth:
    if four in addr:
        town=re.sub(four+'.*$',"", addr)
        town+=four
        addr=addr.replace(town,'',1)#删去四级地址
        break
    else:
        town=""
client['地址'].append(town)

#五级
fifth=['街','路','村','巷','弄','道']
if dif=='1':#1级难度
    street=addr
    client['地址'].append(street)
elif dif=='2' or '3':#继续划分到五级以后
    for five in fifth:
        if five in addr:
            street=re.sub(five+'.*$',"", addr)
            street+=five
            client['地址'].append(street)
            addr=addr.replace(street,'',1)#删去五级地址
            break
        else:
            street=""
    #六级
    if '号' not in addr:
        hao=""
    else:
        hao=re.sub(r'号.*$',"", addr)
        hao+='号'
        addr=addr.replace(hao,'',1)#删去六级地址
    client['地址'].append(hao)

    #七级
    seven=addr
    client['地址'].append(seven)

json1=json.dumps(client,ensure_ascii=False)
print(json1)
