from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __str__(self):
        return self.name


class TipoEmail(AutoName):
    REGISTRO_EXITOSO = auto()
    POSTULACION_APROBADA_ENTIDAD = auto()
    RESETEO_PASSWORD = auto()
    POSTULACION_APROBADA_INDIVIDUAL = auto()
    POSTULACION_APROBADA_CONSOLIDADO = auto()
    POSTULACION_ENESPERA_INDIVIDUAL = auto()
    POSTULACION_ENESPERA_CONSOLIDADO = auto()
    
    
class EstadoBoleto(AutoName):
    ASIGNADO = auto()
    RESERVADO = auto()
    VENDIDO = auto()
