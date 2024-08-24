password = []
number_for_password = int(input('Введите число от 3 до 20: '))
for i in range(1,number_for_password):
    for j in range (1,number_for_password):
        if i == j:
            continue
        if number_for_password%(i+j) == 0:
            password.append([i, j])

length_password = len(password)
start_index = 0

for i in range(length_password):
    start_index += 1
    for j in range(start_index, length_password):
        if password[i][0] == password[j][1] and password[i][1] == password[j][0]:
            del password[j]
            length_password = len(password)
            break

password_finish_two = []
for password_one in password:
    for password_finish in password_one:
        password_finish_two.append(password_finish)

print(*password_finish_two, sep = '')