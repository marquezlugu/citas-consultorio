"""Correo de confirmación que recibe el paciente al agendar."""


def confirmation_email(appointment):
    when = appointment.start.strftime("%d/%m/%Y a las %I:%M %p")
    return (f"Hola, {appointment.patient}. Tu cita con {appointment.doctor} "
            f"quedó agendada para el {when}.")
