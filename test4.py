class Prime:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.primes=[]
    def is_prime(self, number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    def calculate_primes(self):
        for j in range(2, self.n + 1):
                if self.is_prime(j):
                    self.primes.append(j)
                    self.count += 1
        return self.primes , self.count
if __name__ == "__main__":
    n = int(input('請輸入一個正整數：'))
    prime_numbers = Prime(n)
    primes, count = prime_numbers.calculate_primes()
    print(f"總共有{count}個質數")
    print(f"質數有{primes}")