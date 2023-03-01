#py-kr-number

#PKN

#how to use "pkn"?

#import pkn
#number = 10000
#result = pkn.convert(number, "won")
#print(result)
#output = 1만0000won

#Do not modify this code unless you know how it works.
#You can modify the code as needed.

#If you need to edit this file, please check this out and do it!

#==========Edit method==========#
#elif count == 20:
#Change the 20 written in that code to 24.
#example : elif count == 24:
#list_1.append("해") < this "해" You can write the unit you want to add in the part where is written.
#Please don't touch the others unless you're going to change the entire code.
'''
MIT License

Copyright (c) 2023 yeokyoomin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
def convert(num, end):
    n_int = int(num)
    n_str = str(n_int)
    list_1 = []
    list_2 = []
    count = 0
    for i in range(len(n_str)):
        list_2.append(n_str[i])
    list_2.reverse()
    r_str = ''.join(list_2)
    if n_str[0] == "0":
        raise Exception("The first number of entered values ​​is zero.")
    for i in range(len(r_str)):
        if count == 4:
            list_1.append("만")
        elif count == 8:
            list_1.append("억")
        elif count == 12:
            list_1.append("조")
        elif count == 16:
            list_1.append("경")
        elif count == 20:
            list_1.append("해")
        list_1.append(r_str[i])
        count += 1
    list_1.reverse()
    list_1.append("원")
    return ''.join(list_1)
def help_pkn():
    print("====<help>====")
    print("> convert(numberm, won)")
    print("> help()")
