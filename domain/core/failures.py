from infrastructure.failures import Failure


class AnimalHasNoBirthday(Failure):

    def __init__(self):
        message = "The animal has no date of birth."
        super().__init__(message)


class ParametersNotFound(Failure):

    def __init__(self):
        message = "Parameters Not Found"
        super().__init__(message)