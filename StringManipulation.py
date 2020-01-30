import re
table = 'H'
promos = ('EC8', 'EC9', 'ECQ', 'ECR', 'ECT', 'EF1', 'EF2', 'EF3', 'EF4', 'EF5', 'EG0', 'EG1', 'EG3',  
           'UC%', 'XC8', 'XC9','YC1', 'YC2', 'YC3', 'YC4', 'YC9', 'YG0', 'YG1', 'YG2', 'YG3', 'ZCQ', 'ZCR', 'ZCT')
s = '''{t}.PROMO_CD_1 LIKE {p}
                OR {t}.PROMO_CD_2 LIKE {p} 
                OR {t}.PROMO_CD_3 LIKE {p}
                OR {t}.PROMO_CD_4 LIKE {p}
                OR {t}.PROMO_CD_5 LIKE {p}
                OR {t}.PROMO_CD_6 LIKE {p}
                OR {t}.PROMO_CD_7 LIKE {p} 
                OR {t}.PROMO_CD_8 LIKE {p} 
                OR {t}.PROMO_CD_9 LIKE {p}
                OR {t}.PROMO_CD_10 LIKE {p} 
                OR {t}.PROMO_CD_11 LIKE {p}
                OR {t}.PROMO_CD_12 LIKE {p}'''.format(t=table, p=promos)
            
n = 0
db2 = []
for line in s.splitlines():
   n = n + 1
   newline = line.replace(",", " OR {t}.PROMO_CD_{s} LIKE".format(t=table, s=n)).replace("(", "").replace(")", "")
   db2.append(newline)
print("".join(db2))




