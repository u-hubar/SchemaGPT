class SchemaGPTException(Exception):
    """
    Exception mixin inherited by all exceptions of SchemaGPT
    This allows::
        try:
            some_call()
        except SchemaGPTException:
            # deal with SchemaGPT exception
        except:
            # deal with other exceptions
    """


class EmptyPromptError(SchemaGPTException):
    """
    Raised if empty prompt given.
    """

    pass


class UnsupportedRDFSchemaStandard(SchemaGPTException):
    """
    Raised when given standard for schema isn't supported.
    """

    pass
