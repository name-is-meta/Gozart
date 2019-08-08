#!/usr/bin/env python3
import mido
import asyncio
import shlex
import time


class Analyzer:
    def __init__(self):
        pass

class Sonification:
    def __init__(self):
        pass

class Midi_seq:
    def __init__(self):
        pass


async def play(cmd):
    pass

async def analyze():
    pass


async def main():
    # Command to initialize GnuGo
    init_cmd = "gnugo --mode gtp --level 10"
    print("Initializing Gozart with GnuGo")

    game_proc = await asyncio.create_subprocess_shell(
        init_cmd,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    # Initialize turn count
    turn = 0


    while(True):
        gtp_to_gg = input().encode()
        if("play" in str(gtp_to_gg)):
            stdout, stderr = await game_proc.communicate(gtp_to_gg)
            print(f'[stdout]\n{stdout.decode()}')
            await game_proc.communicate("printsgf \"~/Go/Games/temp/temp.sgf\"")

            stdout, stderr = await game_proc.communicate()
        else:
            stdout, stderr = await game_proc.communicate(gtp_to_gg)
            print(f'{stdout.decode()}')

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

if __name__ == "__main__":
    asyncio.run(main())
