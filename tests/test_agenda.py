import sys
import unittest
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.agenda import Agenda, Appointment


class AgendaTest(unittest.TestCase):
    def test_for_day_returns_only_that_doctor_and_day(self):
        agenda = Agenda()
        agenda.add(Appointment("Dra. Pérez", "María", datetime(2026, 10, 20, 9)))
        agenda.add(Appointment("Dr. Gómez", "José", datetime(2026, 10, 20, 9)))
        agenda.add(Appointment("Dra. Pérez", "Rosa", datetime(2026, 10, 21, 9)))

        result = agenda.for_day("Dra. Pérez", date(2026, 10, 20))

        self.assertEqual([a.patient for a in result], ["María"])

    def test_for_day_is_sorted_by_hour(self):
        agenda = Agenda()
        agenda.add(Appointment("Dra. Pérez", "Rosa", datetime(2026, 10, 20, 11)))
        agenda.add(Appointment("Dra. Pérez", "María", datetime(2026, 10, 20, 9)))

        result = agenda.for_day("Dra. Pérez", date(2026, 10, 20))

        self.assertEqual([a.patient for a in result], ["María", "Rosa"])


if __name__ == "__main__":
    unittest.main()
