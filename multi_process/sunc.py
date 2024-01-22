import time

def factorize(number):
    results = []
    for num in number:
        factors = [i for i in range(1, num + 1) if num % i == 0]
        results.append(factors)
    return results

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    # Вимір часу для синхронної версії
    start_time = time.time()
    results_sync = factorize(numbers)
    end_time = time.time()

    print("Синхронна версія:", results_sync)
    print("Час виконання синхронної версії:", end_time - start_time)