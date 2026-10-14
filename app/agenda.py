"""Agenda del médico: las citas de cada día."""
from dataclasses import dataclass
from datetime import date, datetime


@dataclass(frozen=True)
class Appointment:
    doctor: str
    patient: str
    start: datetime


class Agenda:
    def __init__(self):
        self._appointments = []

    def add(self, appointment):
        self._appointments.append(appointment)

    def for_day(self, doctor, day: date):
        day_appointments = [a for a in self._appointments
                            if a.doctor == doctor and a.start.date() == day]
        return sorted(day_appointments, key=lambda a: a.start)

    def available_slots(self, doctor, day: date, hours=range(8, 17)):
        taken = {a.start.hour for a in self.for_day(doctor, day)}
        return [datetime(day.year, day.month, day.day, h) for h in hours if h not in taken]

    def book(self, doctor, patient, start: datetime):
        appointment = Appointment(doctor, patient, start)
        self.add(appointment)
        return appointment
