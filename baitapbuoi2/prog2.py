# n = int(input("Enter a number:(n=>0)"))

# # kiểm tra xem có input sai không
# while n<0: # nếu input số nhỏ hơn không thì chạy vào vòng while này, nếu n >=0 sẽ bỏ qua vòng while chạy xuống dòng số tiếp theo <line số 8>
#     print("Wrong. PLease enter number greater >= 0") # thông báo nhập sai số 
#     n = int(input("Enter a agin:(n=>0)"))# gọi lại việc nhập số cần tính giai thừa.

# if n == 0: # kiếm tra trường hợp đặc biệt n == 0, nếu n > 0 thì chạy xuống dòng tiếp theo < dòng số 12 >
#     print(1) # hiển thị luôn giá trị 0! = 1
#      # thoát chương trình.

# b = 1 # khai báo biến b có giá trị khởi tạo là 1.
# for i in range(1,n+1): # chạy vòng lặp từ giá trị số 1 đến giá trị n.
#     b = b*i # thức hiện việc tính giai thừa của số i. i! = (i-1)!*i.
  
# print("ket qua:{}".format(b)) # hiển thị giá trị giai thừa của số n được nhập vào.


# print('''Pressing 'c' if you wanna 'c'ontinue
# Pressing 'q' if you wanna 'q'uit ''')
# while True:
#     answer = input("Do you wanna continue?:")
    
#     if answer == 'c':
#         n = int(input("enter a number"))
#         b = 1
#         if n <= 0:
#             print("Wrong!!!")
#         else:
                
#             for i in range(1,n+1):
#                 b = b*i
#             print(b)
#     elif answer == 'q':
#         print("goodbye")
#         break


# # Yêu Cầu tiếp theo.. Thực hiện việc tính lũy thừa liên tục. đến khi mình chọn rời khỏi chương trình.
# # sau khi nhập giá trị n và in gia được n! thì tiếp tục cho phép người dùng có thể nhập số khác vào để tính giai thừa mà không cần chạy lại chương trình.
n = int(input("Enter your number:"))
if n == 0:
    print("1")
elif n < 0:
    print("Wrong!!!")
elif n >0:
    
        b = 1
        for i in (1,n+1):
            b = b * i
    print(b)

