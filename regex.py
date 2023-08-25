import re

def find_date(s):
    """
    Find the date from the given string. The date must follow the pattern dd Mmm yyyy.
    Months are described by 3 letter abbreviations. Days and years can be omitted. 
    E.g., 1 Feb 2020, 13 Apr 2563, Dec 2019
    Input:  s = the input string
    Output: a list of date tuple, (day, month, year)
    """
    # search2 = dict()
    # for ind,vals in dict(df.apply(lambda x:re.search(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-zA-Z.,-]*[\s-]?(\d{1,2})?[,\s-]?[\s]?\d{4}',
    #                                              x,re.I|re.M))).items():
    #     if vals and (ind not in list(search1.keys())):
    #         search2[ind]=vals.group()
    # s = re.findall(r'\d*\s+\w{3}\s+\d{0,4}', s)
    s = re.findall(r'\b(\d{1,2})?\s*(:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s*(\d{4})?\b', s)
    # s = re.search(r'(\d*)[\s](:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)*[\s](\d{0,4})', s)
    # date = (s.group(), s)
    # t = s[0]
    # t = s.group()
    # u = ' '.join(t)
    # u = ''
    # for i in t:
    #     if i != ' ':
    #         u += ' ' + i
    #     else:
    #         pass


    return s

def find_amount(s):
    """
    Find the amounts of money indicated by the dollar sign ($) from the given string, included 
    the sign. The amount may be negative and may contain decimal points. The baht sign may
    appear in front of the amount or after. E.g., 500$, $1000.50, $-100000.
    Input:  s = the input string
    Output: a list of amounts of money in string
    """
    s = re.findall(r'\S*\d+\$|\$.+?\.\d+|\$\W*\d+', s)
    return s

if __name__=="__main__":
    s1 = 'Sarun pay 500$ to Thammasat University on 13 Apr 2563'
    print(s1)
    print('\tDate  : ', find_date(s1))
    print('\tAmount: ', find_amount(s1))
    s2 = 'Rico gives Thammasat University Hospital $1000.50 on 1 Feb 2020'
    print(s2)
    print('\tDate  : ', find_date(s2))
    print('\tAmount: ', find_amount(s2))
    s3 = 'On Dec 2019, Thammasat University reports the profit in quarter 1 is $-100000'
    print(s3)
    print('\tDate  : ', find_date(s3))
    print('\tAmount: ', find_amount(s3))
    s4 = '8 Mar is International Women Day'
    print(s4)
    print('\tDate  : ', find_date(s4))
    print('\tAmount: ', find_amount(s4))


