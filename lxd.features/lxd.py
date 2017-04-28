from subprocess import run, DEVNULL, PIPE


def conjure_up():
    """ Run conjure-up
    """
    run('echo running conjure-up', shell=True)
