def confirmCreateMovie(person_id):
    while True:
        choice = input('Id: '+person_id+"の動画を生成します。'yes' or 'no' [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False

# def completeMessage(person_id):
