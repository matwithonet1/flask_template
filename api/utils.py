def parse_args(parser, record_params=False):
    """
    Executes the parser and returns parser Namespace (behaves as dict).
    """
    args = parser.parse_args()

    if record_params:
        logging_services.record_custom_parameters(**args)

    return args
