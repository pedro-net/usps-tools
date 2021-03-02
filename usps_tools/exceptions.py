import traceback
from typing import Optional
from .i18n import _


class UspsToolsException(Exception):
    """
    Base class for all errors.
    """
    def __init__(self, message: Optional[str] = None, origin: Exception = None):
        """
        :param message:
        :param origin:
        """
        super().__init__(message or _("An error happened in UspsTools."))
        self.origin = origin

    @property
    def traceback_msg(self) -> str:
        """
        :return:
        """
        return traceback.format_exc()


class ConnectionFail(UspsToolsException):
    """
    Erro de conexão com o servidor.
    """
    def __init__(self, message: str = None, origin: Exception = None):
        """
        :param message:
        :param origin:
        """
        msg = str(origin) if origin else message if message else "Erro de conexão."
        super().__init__(msg, origin)


class XmlLoadError(UspsToolsException):
    """
    Não foi possível criar o objeto com o XML da resposta.
    """
    def __init__(self, message: str = None, origin: Exception = None):
        """
        :param message:
        :param origin:
        """
        msg = str(origin) if origin else message if message else "Não foi possível instanciar o JSON da resposta."
        super().__init__(msg, origin)


class XmlResponseError(UspsToolsException):
    """
    Resposta não retornou um XML válido.
    """
    def __init__(self, message: str = None, origin: Exception = None):
        """
        :param message:
        :param origin:
        """
        msg = str(origin) if origin else message if message else "Resposta não retornou um JSON válido."
        super().__init__(msg, origin)


class Timeout(UspsToolsException):
    """
    Servidor demorou muito para responder a requisição.
    """
    def __init__(self, message: str = None, origin: Exception = None):
        """
        :param message:
        :param origin:
        """
        msg = str(origin) if origin else message if message else "Erro de esgotamento (timeout)."
        super().__init__(msg, origin)


class ValidationError(UspsToolsException):
    """
    Erro de validação (marshmallow.exceptions.ValidationError).
    """
    def __init__(self, message: str = None, origin: Exception = None):
        """
        :param message:
        :param origin:
        """
        msg = str(origin) if origin else message if message else _("Validation error.")
        super().__init__(msg, origin)


class NotFoundError(UspsToolsException):
    """
    Procura não encontrou o objeto.
    """
    def __init__(self, message: str = None, origin: Exception = None):
        """
        :param message:
        :param origin:
        """
        msg = str(origin) if origin else message if message else "Erro de validação."
        super().__init__(msg, origin)
