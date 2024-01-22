from multiprocessing import Pool, cpu_count
import time

def factorize_parallel(number):
    with Pool(cpu_count()) as pool:
        results = pool.map(factorize_single, number)
    return results

def factorize_single(num):
    return [i for i in range(1, num + 1) if num % i == 0]

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    # Вимір часу для паралельної версії
    start_time = time.time()
    results_parallel = factorize_parallel(numbers)
    end_time = time.time()

    print("Паралельна версія:", results_parallel)
    print("Час виконання паралельної версії:", end_time - start_time)