from CoderInterface import CoderInterface

class Rot1Coder(CoderInterface):
    def run(self, coder_info: str, string_to_process: str) -> str:
        """Запускаем выбранный режим code или decode"""
        if coder_info == 'code':
            return self._code(string_to_process)
        elif coder_info == 'decode':
            return self._decode(string_to_process)
        else:
            raise ValueError("Режим запуска должен быть 'code' или 'decode'")

    def _code(self, string_to_code: str) -> str:
        """ROT1 encoding - замена буквы на следующую по алфавиту"""
        result = []
        for char in string_to_code:
            if char.isalpha():
                if char.islower():
                    # обрабатываем буквы в нижнем регистре
                    result.append(chr((ord(char) - ord('a') + 1) % 26 + ord('a')))
                else:
                    # обрабатываем буквы в верхнем регистре
                    result.append(chr((ord(char) - ord('A') + 1) % 26 + ord('A')))
            else:
                # оставляем "небуквы" без изменений
                result.append(char)
        return ''.join(result)

    def _decode(self, string_to_decode: str) -> str:
        """ROT1 decoding - возвращаем букву на предыдущую по алфавиту"""
        result = []
        for char in string_to_decode:
            if char.isalpha():
                if char.islower():
                    # вертаем буквы в нижнем регистре назад
                    result.append(chr((ord(char) - ord('a') - 1) % 26 + ord('a')))
                else:
                    # вертаем буквы в верхнем регистре назад
                    result.append(chr((ord(char) - ord('A') - 1) % 26 + ord('A')))
            else:
                # оставляем "небуквы" без изменений
                result.append(char)
        return ''.join(result)
