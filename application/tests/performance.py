import timeit
import subprocess

def perform_calculations():
    for _ in range(300):
        subprocess.check_output(['python', 'application/calculator.py', '1', '2', '3'])
        subprocess.check_output(['python', 'application/calculator.py', '2', '6', '3'])
        subprocess.check_output(['python', 'application/calculator.py', '3', '4', '5'])
        subprocess.check_output(['python', 'application/calculator.py', '4', '12', '4'])
        subprocess.check_output(['python', 'application/calculator.py', '4', '1', '0'])


if __name__ == '__main__':
    execution_time = timeit.timeit(perform_calculations, number=1)
    print("Execution time: {} seconds".format(execution_time))

