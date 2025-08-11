class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km!r})"

    def _coerce_other_to_km(self, other) -> float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return float(other)
        return NotImplemented  # lets Python handle unsupported types

    def __add__(self, other) -> "Distance":
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return Distance(self.km + other_km)

    def __radd__(self, other) -> "Distance":
        return self.__add__(other)

    def __iadd__(self, other) -> "Distance":
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, other) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other) -> "Distance":
        return self.__mul__(other)

    def __truediv__(self, other) -> "Distance":
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return Distance(round(self.km / other, 2))
        return NotImplemented  # Unsupported types should return None

    # comparisons
    def __eq__(self, other) -> bool:
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km == other_km

    def __lt__(self, other) -> bool:
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __le__(self, other) -> bool:
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __gt__(self, other) -> bool:
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km

    def __ge__(self, other) -> bool:
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km
