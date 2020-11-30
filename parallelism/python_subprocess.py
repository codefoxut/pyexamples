import os
import subprocess
import time

from design.course1.decorator.functional_decorator import time_it


def make_subprocess1():
    proc = subprocess.Popen(
        ['echo', 'Hello from the child!'],
        stdout=subprocess.PIPE
    )
    out, err = proc.communicate()
    print(out.decode('utf-8'))


def make_subprocess2():
    proc = subprocess.Popen(['sleep', '0.3'])
    while proc.poll() is None:
        print("Working . . . .")
        # Time consuming work goes here.
        time.sleep(0.2)

    print("Exit status", proc.poll())


def run_sleep(ord, period):
    print(f"Working.. {ord} 1....")
    proc = subprocess.Popen(['sleep', str(period)])
    print(f"Working.. {ord} 2....")
    return proc


@time_it
def make_subprocess3():
    procs = []
    for o in range(10):
        print(f'Creating proc...{o}...')
        proc = run_sleep(o, 0.1)
        procs.append(proc)

    for proc in procs:
        proc.communicate()

    print('Done')


def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'asdf'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()

    return proc


def run_md5(input_stdin):
    proc = subprocess.Popen(
        ['md5'],
        stdin=input_stdin,
        stdout=subprocess.PIPE
    )
    return proc


def make_subprocess4():
    proc = run_openssl(b'banana')
    out, _ = proc.communicate()
    print(out)


def make_subprocess5():
    procs = []
    for _ in range(5):
        data = os.urandom(100)
        proc = run_openssl(data)
        procs.append(proc)

    for proc in procs:
        out, _ = proc.communicate()
        print(out)


def make_subprocess6():
    input_procs = []
    for _ in range(5):
        data = os.urandom(100)
        proc = run_openssl(data)
        input_procs.append(proc)

    hash_procs = []
    for proc in input_procs:
        hash_proc = run_md5(proc.stdout)
        hash_procs.append(hash_proc)

    for proc in input_procs:
        proc.communicate()

    for proc in hash_procs:
        out, _ = proc.communicate()
        print("md5 -->", out)


def make_subprocess_timeout():
    proc = subprocess.Popen(['sleep', '10'])
    try:
        proc.communicate(timeout=0.1)
    except subprocess.TimeoutExpired:
        proc.terminate()
        proc.wait()

    print('Exit status', proc.poll())


if __name__ == '__main__':
    make_subprocess1()
    make_subprocess2()
    make_subprocess3()
    make_subprocess4()
    make_subprocess5()
    make_subprocess6()
    make_subprocess_timeout()
