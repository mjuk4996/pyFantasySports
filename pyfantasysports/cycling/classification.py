
class Classification:

    def __init__(self):
        self.__results = {}

    @property
    def results(self):
        return self.__results

    def handle_results(self, results: dict) -> None:
        raise NotImplementedError

    def calculate_points(self) -> list:
        raise NotImplementedError


class GeneralClassification(Classification):

    def handle_results(self, results: dict) -> None:

        return

    def calculate_points(self) -> list:
        max_points = len(self.results)

        return []


class SprintClassification(Classification):

    def handle_results(self, results: dict) -> None:
        return

    def calculate_points(self) -> list:
        return []


class MountainClassification(Classification):

    def handle_results(self, results: dict) -> None:
        return

    def calculate_points(self) -> list:
        return []
