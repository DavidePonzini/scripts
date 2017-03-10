#!/usr/bin/env python3
import argparse
import subprocess
from sys import argv


flags = ['-c']
_p = []


def _read_from_files(url_filename, name_filename):
    with open(url_filename) as url_file, open(name_filename) as name_file:
        urls = url_file.read().splitlines()
        names = name_file.read().splitlines()

    yield from zip(urls, names)


def _build_command(url, name=None, run_standalone=False, default_names=True):
    command = []

    if name == None and default_names:
        raise Exception()

    if run_standalone:
        command += ['gnome-terminal', '-x']

    # Add wget directive
    command += ['wget', url]
    if default_names:
        command += ['-O', name]

    # Add flags
    command += flags

    return command


def _wait():
    for p in _p:
        p.wait()


def download(urls, names, allow_multi_threading=False, run_standalone=False, default_names=True):
    for url, name in _read_from_files(urls, names):
        _download(url, name, allow_multi_threading, run_standalone, default_names)

    if allow_multi_threading:
        _wait()


def _download(url, name, run_in_background, run_standalone, default_names):
    _p.append(subprocess.Popen(_build_command(url, name, run_standalone, default_names)))

    if not run_in_background:
        _wait()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('urls')
    parser.add_argument('names')
    parser.add_argument('-m', '--allow-multi-threading', action='store_true')
    parser.add_argument('-t', '--run-as-terminal', action='store_true')
    parser.add_argument('--default-names', action='store_true')

    args = parser.parse_args()

    return args.urls, args.names, args.allow_multi_threading, args.run_as_terminal, args.default_names


def main():
    urls, names, allow_multi_threading, run_as_terminal, default_names = parse_args()

    download(urls, names, allow_multi_threading, run_as_terminal, default_names)


if __name__ == '__main__':
    main()
