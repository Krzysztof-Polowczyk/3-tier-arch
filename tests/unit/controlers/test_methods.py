from unittest.mock import Mock
from unittest.mock import call

from pytest import fixture
from pytest import raises

from app.repositoris import persitance
from app.controlers import controlers


@fixture
def repository() -> Mock:
    return Mock(persitance)

@fixture
def controller(repository: Mock) -> controlers:
    return controlers(repository)

@fixture
def data_user() -> dict:
    return {
            "firstName":"mike",
            "lastName":"zizka",
            "birthYear": 123,
            "group": "user"
        }

def test_calls_repository_on_get_method(
    controller: controlers,
    repository: Mock,
) -> None:
    book_id = 1
    controller.get(book_id)
    repository.get.assert_called_with(book_id)


def test_calls_repository_on_get_all_method(
    controller: controlers,
    repository: Mock,
) -> None:

    controller.get_all()
    repository.get_all.assert_called_with()


def test_calls_repository_on_put_method(
    controller: controlers,
    repository: Mock,
    data_user: dict

) -> None:

    controller.put(data_user)
    repository.add.assert_called_with(data_user)

def test_calls_repository_on_patch_method(
    controller: controlers,
    repository: Mock,
    data_user: dict

) -> None:
    id = 2
    controller.patch(id, data_user)
    repository.patch.assert_called_with(id, data_user)

def test_calls_repository_on_delete_method(
    controller: controlers,
    repository: Mock,


) -> None:
    id = 1
    controller.dellete(id)
    repository.dell.assert_called_with(id)





