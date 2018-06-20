from collections import defaultdict

log_times = defaultdict(int)

with open('logs.txt') as file_input:
    for line in file_input:
        user, op, time = line.split(';')
        time = int(time)

        if op == 'LOGIN':
            # odejmujemy czas
            log_times[user] -= time
        else: # op == 'LOGUOT'
            # dodajemy czas
            log_times[user] += time

with open('logs_total.txt',mode='w') as file_output:
    file_output.write('\n'.join(f'{user}:{total_time}'
                for user, total_time in sorted(log_times.items())))