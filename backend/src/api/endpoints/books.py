from fastapi import APIRouter


books_router = APIRouter(
    prefix='/books',
    tags=['books']
)

# @router.get(
#     '/{operation_id}',
#     response_model=models.Operation,
# )
# def get_operation(
#     operation_id: int,
#     user: models.User = Depends(get_current_user),
#     operations_service: OperationsService = Depends(),
# ):
#     return operations_service.get(
#         user.id,
#         operation_id,
#     )

# посмотреть логику как проходить валидация schemas  и как ее прикрутить
# начать тестить