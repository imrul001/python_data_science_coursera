lowercase = 'abcedfghijklmnopqrstuvwxyz'
digits = '0123456789';

answer = [l+d for l in lowercase for d in digits];

print(answer);