"""
 * Project name(项目名称)：Python变量 
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/21 
 * Time(创建时间)： 17:27
 * Version(版本): 1.0
 * Description(描述)： 复数
 """

if __name__ == '__main__':
    c1 = 12 + 0.2j
    print("c1Value: ", c1)
    print("c1Type", type(c1))
    c2 = 6 - 1.2j
    print("c2Value: ", c2)
    # 对复数进行简单计算
    print("c1+c2: ", c1 + c2)
    print("c1*c2: ", c1 * c2)

    input()
