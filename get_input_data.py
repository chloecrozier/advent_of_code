# Run with: python get_input_data.py {YEAR} {DAY}
from dotenv import load_dotenv
import requests
import sys
import os

if len(sys.argv) < 3:
    print('Usage: python get_input_data.py AOC {YEAR} {DAY}')
    sys.exit(1)
else:
    url = f'https://adventofcode.com/{sys.argv[1]}/day/{sys.argv[2]}/input'

    load_dotenv(dotenv_path='.env', verbose=True)
    session_id = os.getenv('AOC_SESSION_ID')
    headers = {'Cookie': f'session={session_id}'}

    page = requests.get(url, headers=headers)

    if not os.path.exists(f'{os.getcwd()}/input/{sys.argv[1]}'):
        os.makedirs(f'{os.getcwd()}/input/{sys.argv[1]}/', exist_ok=True)
    input_file = open(f'input/{sys.argv[1]}/day{sys.argv[2]}.txt', 'w')
    input_file.write(page.text)
    print(f'Input data saved to {sys.argv[2]}/day{sys.argv[2]}.txt!')