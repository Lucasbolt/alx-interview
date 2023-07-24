#!/usr/bin/python3
"""log parsing module."""


def processLine(line: str, status_codes: dict) -> int:
    """
    The line processing function.
    Extracts the status code and the file size
    from the line.
    """
    if 'GET /projects' in line:
        try:
            fsize = int(line.split()[-1])
            status = int(line.split()[-2])
            if status in status_codes.keys():
                status_codes[status] += 1
            return fsize
        except ValueError:
            pass
    return 0


def logLines(total_file_size: int, status_codes: dict):
    """Logs the processed lines to the standard output."""
    print(f'File size: {total_file_size}', flush=True)
    for code in sorted(status_codes):
        num = status_codes.get(code, 0)
        if num > 0:
            print(f'{code}: {num}', flush=True)


def run():
    """The entrance function"""
    total_file_size = 0
    nlines = 0
    status_codes = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
            }
    try:
        while True:
            line = input()
            total_file_size += processLine(
                    line,
                    status_codes
                    )
            nlines += 1
            if nlines % 10 == 0:
                logLines(total_file_size, status_codes)
    except (KeyboardInterrupt, EOFError):
        logLines(total_file_size, status_codes)


if __name__ == '__main__':
    run()
