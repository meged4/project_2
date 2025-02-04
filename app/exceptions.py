from fastapi import HTTPException, status


class BaseEx(HTTPException):
    detail = ""
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class NotTokenException(BaseEx):
    detail = "Отсутствует токен"
    status_code = status.HTTP_409_CONFLICT


class IncorrectTokenFormatException(BaseEx):
    detail = "Неверный токен"
    status_code = status.HTTP_409_CONFLICT


class TokenExpiredException(BaseEx):
    detail = "Токен истёк"
    status_code = status.HTTP_409_CONFLICT


class ClientAlreadyExistsException(BaseEx):
    detail = "Данный пользователь уже зарегистрирован"
    status_code = status.HTTP_409_CONFLICT


class MasterAlreadyExistsException(BaseEx):
    detail = "Данный мастер уже зарегистрирован"
    status_code = status.HTTP_409_CONFLICT


class NotRegisterClientException(BaseEx):
    detail = "Данной клиент не зарегистрирован"
    status_code = status.HTTP_409_CONFLICT


class NotRegisterMasterException(BaseEx):
    detail = "Вы не зарегистрированы как мастер"
    status_code = status.HTTP_409_CONFLICT


class IncorrectPasswordException(BaseEx):
    detail = "Неверный пароль"
    status_code = status.HTTP_409_CONFLICT


class MasterRegisterException(BaseEx):
    detail = "Только мастер может зарегистрировать другого мастера"
    status_code = status.HTTP_409_CONFLICT


class NotFindService(BaseEx):
    detail = "Такой услуги не найдено"
    status_code = status.HTTP_404_NOT_FOUND


class NotFindVacantEntriesException(BaseEx):
    detail = "На данную дату и время нет свободных записей"
    status_code = status.HTTP_404_NOT_FOUND


