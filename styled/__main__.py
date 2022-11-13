import argparse
import sys

import styled
import styled.assets


def main():
    args = parse_args()
    if args.command == "version":
        print("v{}".format(styled.__version__))
    if args.command == "try":
        print(styled.Styled(args.text))
    elif args.command == "demo":
        if args.object == "colours" or args.object == "all":
            print(styled.Styled("[[ '{:<17}COLOURS{:>17}'|underlined:bold ]]".format('', '')))
            for colour_name in styled.assets.COLOURS:
                print(
                    styled.Styled("[[ '{:^20}'|fg-{}:bg-white ]]".format(colour_name, colour_name)) +
                    styled.Styled("[[ '{:^20}'|bg-{} ]]".format(colour_name, colour_name))
                )
        if args.object == "formats" or args.object == "all":
            print(styled.Styled("[[ '{:<7}FORMATS{:>7}'|underlined:bold ]]".format('', '')))
            for style_name in styled.assets.STYLE_NAMES:
                print(styled.Styled("[[ '{:^20}'|{} ]]".format(style_name, style_name)))
    return 0


def parse_args():
    parser = argparse.ArgumentParser(
        prog='styled',
        description="Style your terminal with ease!"
    )
    subparser = parser.add_subparsers(
        dest='command',
    )
    # try
    try_parser = subparser.add_parser(
        'try',
        help="provided a formatted quoted string to try"
    )
    try_parser.add_argument('text', help="a formatted quoted string to style")
    # demo
    demo_parser = subparser.add_parser(
        'demo',
        help="print a demo showing colours and styles"
    )
    # version
    version_parser = subparser.add_parser(
        'version',
        help="display the current version"
    )
    style_choices = ['colours', 'formats']
    demo_parser.add_argument(
        'object',
        choices=style_choices,
        nargs='?',
        default='colours',
        help="what to demo; choose from {choices}".format(choices=', '.join(style_choices))
    )
    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
    return args


if __name__ == '__main__':
    sys.exit(main())
