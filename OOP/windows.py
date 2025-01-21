def set_dpi_awareness():
    try:
        '''the text looks much nicer'''
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass