#!/usr/bin/env python3
import sys

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--frontier-path', default='./frontier/src/frontier/frontier')
args = parser.parse_args()

import subprocess
def frontier(g, s, t):
    # https://github.com/junkawahara/frontier
    print('[*] run frontier', file=sys.stderr)
    proc = subprocess.run([ args.frontier_path, '-t', 'stpath', '-s', str(s), '-e', str(t) ],
        input=g.encode(),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE)
    proc.check_returncode()
    print('[*] done', file=sys.stderr)
    result = None
    for line in proc.stderr.decode().splitlines():
        print(line, file=sys.stderr)
        keyword = '# of solutions = '
        if line.startswith(keyword):
            result = int(line[len(keyword) : ].split()[0])
    return result

H = 16
W = 16

def make_graph(s, mid=True):
    g = [ list() for _ in range(H * W) ]
    compress = [ None ] * (H * W)
    k = {}
    for z in range(H * W):
        if s[z] == 3 and not mid:
            continue
        if s[z]:
            compress[z] = len(compress) - compress.count(None)
        if s[z] >= 2:
            assert s[z] not in k
            k[s[z]] = compress[z] + 1
    for y in range(H):
        for x in range(W):
            z = y * W + x
            if s[z] == 3 and not mid:
                continue
            if not s[z]:
                continue
            for i in range(4):
                ny = y + [ -1, 1, 0, 0 ][i]
                nx = x + [ 0, 0, 1, -1 ][i]
                if 0 <= ny < H and 0 <= nx < W:
                    nz = ny * W + nx
                    if s[nz] == 3 and not mid:
                        continue
                    if not s[nz]:
                        continue
                    g[z] += [ nz ]
    t = ''
    for z in range(H * W):
        row = list(map(lambda i: str(compress[i] + 1), g[z]))
        if row:
            t += ' '.join(row) + '\n'
    return t, k[2], k[4]

s = list(map(int, input()))
assert len(s) == H * W
a = frontier(*make_graph(s))
b = frontier(*make_graph(s, mid=False))
print(a - b)
