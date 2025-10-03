# RLECoder.py
from CoderInterface import CoderInterface


class RLECoder(CoderInterface):
    def __init__(self, max_run: int = None):
        self._decode_buffer = ''
        self._max_run = int(max_run) if max_run is not None else None

    def run(self, coder_info: str, string_to_process: str) -> str:
        if coder_info == 'code':
            return self._code(string_to_process)
        elif coder_info == 'decode':
            return self._decode(string_to_process)
        else:
            raise ValueError("Invalid coder option. Use 'code' or 'decode'.")

    def _code(self, string_to_code: str) -> str:
        if not string_to_code:
            return ''

        out = []
        prev = string_to_code[0]
        count = 1

        for ch in string_to_code[1:]:
            if ch == prev:
                count += 1
                if self._max_run is not None and count == self._max_run:
                    out.append(f"{count}{prev}")
                    count = 0
            else:
                if count > 0:
                    out.append(f"{count}{prev}")
                prev = ch
                count = 1

        if count > 0:
            out.append(f"{count}{prev}")

        return ''.join(out)

    def _decode(self, string_to_decode: str) -> str:
        self._decode_buffer += string_to_decode
        out = []

        i = 0
        n = len(self._decode_buffer)

        while i < n:
            j = i
            while j < n and self._decode_buffer[j].isdigit():
                j += 1

            if j == i:
                break

            if j >= n:
                break

            count_str = self._decode_buffer[i:j]
            ch = self._decode_buffer[j]

            try:
                cnt = int(count_str)
            except ValueError:
                raise ValueError(f"Invalid encoded count: {count_str}")

            out.append(ch * cnt)
            i = j + 1

        self._decode_buffer = self._decode_buffer[i:]
        return ''.join(out)

    def flush(self) -> str:

        if self._decode_buffer:
            raise ValueError(f"Неполный остаток декодирования: '{self._decode_buffer}'")
        return ''
