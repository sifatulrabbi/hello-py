class Gig:
    __name: str
    __paycheck: float
    __stamina_loss: int

    def __init__(self, name: str, paycheck: float, stamina_loss: int) -> None:
        self.__name = name
        self.__paycheck = paycheck
        self.__stamina_loss = stamina_loss

    def get_name(self) -> str:
        return self.__name

    def get_paycheck(self) -> float:
        return self.__paycheck

    def get_stamina_loss(self) -> int:
        return self.__stamina_loss
