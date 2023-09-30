# # grosspay=int(input("please input your gross pay"))
# medicare=0.0145*grosspay
# futa=0.006*grosspay
# ss_tax_employer=0.062*grosspay
# ss_tax_employee=0.062*grosspay
# totaltax=medicare+futa+ss_tax_employee
# netpay=grosspay-totaltax
# # total_tax=medicare+futa+ss_tax_employer





# # print(f"Gross Pay: ${grosspay:.2f}")
# # print(f"Medicare:${medicare:.2f}")
# # print(f"Fute:${futa:.2f}")
# # print(f"SS_Tax_employer:${ss_tax_employer:.2f}")
# # print(f"SS_Tax_employee:${ss_tax_employee:.2f}")
# # print(f"Total Tax:${totaltax:.2f}")
# # print(f"Net Pay:${netpay:.2f}")




table1=[18.1,15.4,19.0,13.4,10.2,13.1,18.1,14.4,15.0,10.8,5.4,12.2]
table2=[0.7,0.0,0.7,1.0,1.1,0.4,0.0,1.0,2.3,2.9,1.3]
x=sum (table1) / len (table1)
y=sum (table2)/ len(table2)
print(f"Average mortality rate before hand washing policy:{round(x,1)}")
print(f"Average mortality rate after hand washing policy:{round(y,1)}")
# print(round(x,1))