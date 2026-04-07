#Sistema de Universidad
"""Relación entre clases
Persona es clase padre.
Estudiante y Profesor heredan de Persona → herencia.
Curso tiene estudiantes → agregación.
Curso crea sus evaluaciones → composición.
"""
from abc import ABC, abstractmethod
class persona (ABC):
    def __init__ (self, nombre,edad):
        self: f.nombre = nombre
        self.edad = edad