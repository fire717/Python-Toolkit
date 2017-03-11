'''
python3中，bytes是包含8位值的序列，str是包含unicode的序列。不能用+、>等符号混合操作；
python2中，str是包含8位值得序列，unicode是包含unicode的序列。若str只含有7位ASCII字符，则可通过操作符来混合操作。

编写python程序时，一定要把编码和解码操作放在界面最外围来做，程序的核心部分应使用unicode字符类型，且不要对字符编码做任何假设。
'''

#Python3中，接受str或bytes，返回str的方法：
def to_str(bytes_or_str):
    if isinstance(bytes_or_str,bytes):    #isinstance(object，[type]) 来判断一个对象是否是一个已知的类型,返回布尔值
        value = bytes_or_str.decode('utf-8') #以utf-8对对象编码
    else:
        value = bytes_or_str
    return value   #instance of str
    
#Python3中，接受str或bytes，返回bytes的方法：
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str,str):    
        value = bytes_or_str.encode('utf-8') #以utf-8对对象解码
    else:
        value = bytes_or_str
    return value   #instance of bytes
    
#Python2中，接受str或unicode，返回unicode的方法：
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str,str):    
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value   #instance of unicode
    
#Python2中，接受str或unicode，返回str的方法：
def to_str(unicode_or_str):
    if isinstance(unicode_or_str,unicode):    
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value   #instance of str
