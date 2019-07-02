from argparse import ArgumentParser

from . import _auth
from . import _debug
from . import _downloading
from . import _general
from . import _image
from . import _reader


def get_cli_arguments() -> ArgumentParser:
    """
    :return:
    :rtype: ArgumentParser
    """
    args_parser = ArgumentParser(add_help=False)

    _general.main(args_parser)
    _auth.main(args_parser)
    _image.main(args_parser)
    _reader.main(args_parser)
    _downloading.main(args_parser)
    _debug.main(args_parser)

    return args_parser


__all__ = ['get_cli_arguments']
