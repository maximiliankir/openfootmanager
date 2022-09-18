#      Openfoot Manager - A free and open source soccer management game
#      Copyright (C) 2020-2022  Pedrenrique G. Guimarães
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
from dataclasses import dataclass
from datetime import date, datetime, timedelta


@dataclass
class Contract:
    wage: float
    contract_started: date
    contract_end: date
    bonus_for_goal: float
    bonus_for_def: float

    @classmethod
    def get_from_dict(cls, contract: dict):
        return cls(
            contract["wage"],
            datetime.strptime(contract["started"], "YYYY-mm-dd").date,
            datetime.strptime(contract["end"], "YYYY-mm-dd").date,
            contract["bonus_for_goal"],
            contract["bonus_for_def"],
        )
    
    @property
    def contract_length(self) -> timedelta:
        return timedelta(self.contract_end - self.contract_started)
