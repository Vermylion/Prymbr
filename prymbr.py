from types import NoneType

class Fraction:
    def __init__(self, num, deno):
        self.num = num
        self.deno = deno

    def __str__(self):
        return f'{self.num}/{self.deno}'

def simp(fraction):
    if type(fraction) == Fraction:
        num, deno = str(fraction).split('/')
        num, deno = int(num), int(deno)

        decomp_num = decomp(num)
        decomp_deno = decomp(deno)
        
        sim_num, sim_deno = decomp_num.copy(), decomp_deno.copy()
        simp_num, simp_deno = 1, 1

        for x in range(len(decomp_num)):
            if decomp_num[x] not in sim_deno:
                simp_num *= decomp_num[x]
            else:
                sim_deno.remove(decomp_num[x])

        for x in range(len(decomp_deno)):
            if decomp_deno[x] not in sim_num:
                simp_deno *= decomp_deno[x]
            else:
                sim_num.remove(decomp_deno[x])
    
        return Fraction(simp_num, simp_deno)

    else:
        raise ValueError('Cannot simplify non-fraction!')

def deci(fraction):
    if type(fraction) == Fraction:
        num, deno = str(fraction).split('/')
        num, deno = int(num), int(deno)

        return num / deno
    else:
        raise ValueError('Cannot convert non-fraction!')

def frac(numerator = 0, denominator = None):
    if type(numerator) == Fraction:
        return True
    elif (type(numerator) == int or type(numerator) == float) and (type(denominator) == int or type(denominator) == float or type(denominator) == NoneType):
        if denominator is None:
            if numerator == int(numerator):
                return Fraction(int(numerator), 1)
            else:
                denominator = int('1' + len(str(numerator).split('.')[1])*'0')
                numerator = int(numerator * denominator)

                return simp(Fraction(numerator, denominator))

        return Fraction(numerator, denominator)
    else:
        return False

def isprime(number):
    if number % 2 == 0 and not number == 2 or number < 2:
        return False

    for x in range(3, round(number / 3) + 1, + 2):
        if number % x == 0:
            return False

    return True

def decomp(number):
    if not type(number) == int:
        raise ValueError('Not a whole number!')

    final_decomp = []
    is_prime = isprime(number)
    curr_decomp = number

    if number == 1:
        is_prime = True

    while not is_prime:
        #find smallest prime that can divide given number
        for x in range(2, round(curr_decomp / 3) + 1):
            if isprime(x):
                #see if that number can divide remaining decomposition
                if curr_decomp % x == 0:
                    curr_decomp /= x
                    final_decomp.append(x)
                    break

        is_prime = isprime(curr_decomp)

    final_decomp.append(int(curr_decomp))
    return final_decomp

def pgcd(nbr1, nbr2):
    decomp_nbr1 = decomp(nbr1)
    decomp_nbr2 = decomp(nbr2)
    sim_prime = []
    final_pgcd = 0

    for x in range(len(decomp_nbr1)):
        if decomp_nbr1[x] in decomp_nbr2:
            sim_prime.append(decomp_nbr1[x])

    for x in sim_prime:
        final_pgcd += x

    return final_pgcd + 1

def gcd(nbr1, nbr2):
    return pgcd(nbr1, nbr2)

def ppcm(nbr1, nbr2):
    return int((nbr1 * nbr2) / pgcd(nbr1, nbr2))

def lcm(nbr1, nbr2):
    return int((nbr1 * nbr2) / pgcd(nbr1, nbr2))