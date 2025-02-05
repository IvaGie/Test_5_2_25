def eratosthenes_sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]  # 0 a 1 nejsou prvočísla

    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

# Odhadneme horní mez pro dostatečný počet prvočísel
# Pomocí n * (log n + log log n) můžeme odhadnout mez

def estimate_upper_bound(n):
    from math import log
    if n < 6:
        return 15  # malá konstanta pro n < 6
    return int(n * (log(n) + log(log(n))))

# Najdeme prvních 1300 prvočísel
upper_bound = estimate_upper_bound(1300)
primes = eratosthenes_sieve(upper_bound)

# Omezíme výstup pouze na prvních 1300 prvočísel
primes = primes[:1300]

# Výpis výsledků
print(primes)

# Najdeme 1116. prvočíslo (index 1115, protože indexace začíná od 0)
prime_1116 = primes[1115]
print(f"1116. prvočíslo je: {prime_1116}")

filename = 'syn2010_word.vyber-ascii.min.txt'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if prime_1116 <= len(lines):
            line = lines[prime_1116 - 1].strip('\n')
            print(f"slovo na radku {prime_1116}: {line}")
        else:
            print(f"Soubor nemá {prime_1116} řádků.")
except FileNotFoundError:
    print(f"Soubor '{filename}' nebyl nalezen.")


def printMatrix(matrix):
    for row in matrix:
        print(" ".join(row))

def read_cipher_to_array(file_cipher):
    try:
        with open(file_cipher, 'r', encoding='utf-8') as file:
            matrix = [list(line.strip().replace("'", "")) for line in file if line.strip()]
            return matrix
    except FileNotFoundError:
        print(f"Soubor '{file_cipher}' nebyl nalezen.")
        return []

cipher = 'sifra.txt'
cipher_matrix = read_cipher_to_array(cipher)
printMatrix(cipher_matrix)


def sort_and_rearrange_matrix(line, cipher_matrix):
    print(line)
    # Seřadíme písmena v abecedním pořadí a zjistíme původní pozice
    sorted_word = sorted((char, idx) for idx, char in enumerate(line))
    sorted_chars = [char for char, idx in sorted_word]
    original_positions = [idx for char, idx in sorted_word]
    print(sorted_chars)
    # Zapamatujeme si původní pořadí písmen
    sort_key = {original_positions[i]: sorted_chars[i] for i in range(len(sorted_chars))}
    ##print(sort_key)
    # Přeuspořádáme sloupce matice podle původního pořadí písmen ve vybraném slovu
    rearranged_matrix = []
    for row in cipher_matrix:
        rearranged_row = [row[i] for i in original_positions]
        rearranged_matrix.append(rearranged_row)
    printMatrix(rearranged_matrix)
    return rearranged_matrix, sort_key

line = lines[prime_1116 - 1].strip()  # slovo na 1116. řádku
rearranged_matrix, sort_key = sort_and_rearrange_matrix(line, cipher_matrix)
