(setattr(quit, 'sys', __import__('sys')) or setattr(quit, 'os', __import__('os')) or setattr(quit, 'md5', __import__('hashlib').md5) or setattr(quit, 'r', __import__('random').SystemRandom()) or setattr(quit, 'b64encode', __import__('base64').b64encode) or setattr(quit, 'out', lambda x: quit.sys.stdout.write(str(x) + '\n')) or setattr(quit, 'while_loop', lambda g, b: eval(compile('while g(): b()', '<while-loop>', 'exec'))) or setattr(quit, 'FILE_PATH', quit.os.path.abspath(__file__)) or setattr(quit, 'get_md5', lambda x: quit.md5(x).hexdigest()) or setattr(quit, 'calculate_state', lambda data: (setattr(quit, 'state', ''.join((''.join((c for c in quit.b64encode(quit.get_md5(str(ord(item))))[::-1][:8] if c != '=')) for item in quit.get_md5(data)))) or (quit.state if ord(quit.get_md5(quit.state[0])[0]) % 5 else quit.calculate_state(quit.state)))) or setattr(quit, 'is_numberwang', lambda x, useImag=False: (False if (((quit.out("I'm sorry, that's not a number...") or 1) if not useImag else 0) if (False in (a.isdigit() for a in x.split('.', 1))) else ((quit.out("I'm sorry, that is an actual number...") or 1) if useImag else 0)) else (setattr(quit, '_state', quit.calculate_state(x + quit._state)) or (not sum((ord(i) for i in quit._state)) % 3)))) or setattr(quit, 'is_wangernumb', lambda x: (False if ((quit.out("I'm sorry, that's not a number...") or 1) if False in (a.isdigit() for a in x.split('.', 1)) else 0) else (not sum((ord(c) for c in quit.get_md5(''.join((str(quit.is_numberwang(x)) for i in xrange(ord(x[0]))))))) % 7))) or setattr(quit, 'main', lambda: (setattr(quit, 'f', open(quit.FILE_PATH, 'rb')) or (setattr(quit, 'data', quit.f.read()) or quit.f.close()) or setattr(quit, '_state', quit.calculate_state(quit.data)) or setattr(quit, 'playerName', raw_input("Please enter your name: ")) or (setattr(quit, 'playerName', quit.r.choice(('Julie', 'Simon'))) if quit.playerName.lower() not in ('julie', 'simon') else 0) or quit.out("Okay, " + quit.playerName) or quit.out("LET'S PLAY NUMBERWANG!") or quit.while_loop(lambda: not quit.is_numberwang(raw_input('? ')), lambda: None) or quit.out("THAT'S NUMBERWANG!\n") or quit.out("Imaginary round:") or quit.while_loop(lambda: not quit.is_numberwang(raw_input('? '), True), lambda: None) or quit.out("THAT'S NUMBERWANG!\n") or quit.out("It's time for WANGERNUMB!") or quit.while_loop(lambda: not quit.is_wangernumb(raw_input('? ')), lambda: None) or quit.out("THAT'S WANGERNUMB!") or 0)) or quit.sys.exit(quit.main()) if __name__ == '__main__' else 0)