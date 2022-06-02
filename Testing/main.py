def do_stuff(num):
        try:
            if num != "":
                return num + 5
            else:
                return 'Please Enter the number'
        except TypeError as err:
            return err
