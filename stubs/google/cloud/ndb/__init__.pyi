from .context import Context as Context
from .query import (
    AND as AND, OR as OR, Query as Query, Node as Node,
    ConjunctionNode as ConjunctionNode, DisjunctionNode as DisjunctionNode,
    FilterNode as FilterNode)
from google.cloud import datastore
from redis import StrictRedis

from typing import (
    Any, Callable, Dict, Generic, Iterable, Iterator, List, Optional, Sequence,
    Type, TypeVar, Tuple, Union, overload)
from typing_extensions import Literal

TYPE_MODEL = TypeVar('TYPE_MODEL', bound='Model')

class Client:
    def context(
        self,
        namespace: Optional[str],
        global_cache: Optional[RedisCache]
    ) -> Context: ...

# Model Stubs
class Model(type):
    key: Key = ...
    _key: Key = ...
    _values: Dict[str, Any] = ...
    _properties: Dict[str, Any] = ...
    def __init__(*args: Any, **kwds: Any) -> None: ...
    def populate(self, **constructor_options: Any) -> None: ...
    def to_dict(
        self, exclude: Optional[List[str]] = None
    ) -> Dict[str, Any]: ...
    @classmethod
    def query(cls: Type[TYPE_MODEL], *args: Any, **kwds: Any) -> Query: ...
    def put(self, **ctx_options: Any) -> None: ...
    @classmethod
    def get_by_id(
        cls: Type[TYPE_MODEL], id: str, **ctx_options: Any
    ) -> TYPE_MODEL:...
    def _pre_put_hook(self) -> None: ...
    @classmethod
    def _lookup_model(cls, kind: Optional[str]) -> TYPE_MODEL: ...
    @classmethod
    def _get_kind(cls) -> str: ...


def get_context(**kwds: Any) -> Context: ...
def get_multi(
    keys: List[Key], **ctx_options: Any) -> List[Optional[TYPE_MODEL]]: ...
def put_multi(
    entities: (List[TYPE_MODEL]), **ctx_options: Any) -> List[str]: ...
def delete_multi(keys: Sequence[Key], **ctx_options: Any) -> List[None]: ...


# Property Stubs
class Property(object):
    def __init__(
        self, name: Optional[str] = ..., indexed: Optional[bool] = ...,
        repeated: Optional[bool] = ..., required: Optional[bool] = ...,
        default: Optional[Any] = ...,
        choices: Union[List[Any], Tuple[Any, ...], None] = ...,
        validator: Optional[Callable[..., Any]] = ...,
        verbose_name: Optional[str] = ...
    ) -> None: ...
    def __eq__(self, value: Any) -> bool: ...
    def __ne__(self, value: Any) -> bool: ...
    def __lt__(self, value: Any) -> bool: ...
    def __le__(self, value: Any) -> bool: ...
    def __gt__(self, value: Any) -> bool: ...
    def __ge__(self, value: Any) -> bool: ...
    IN: Any = ...
    def __neg__(self) -> Any: ...
    def __pos__(self) -> Any: ...
    def __get__(self, entity: Any, unused_cls: Optional[Any] = ...) -> Any: ...
    def __set__(self, entity: Any, value: Any) -> None: ...
    def __delete__(self, entity: Any) -> None: ...

class BooleanProperty(Property): ...

class DateTimeProperty(Property):
    def __init__(
        self, name: Optional[str] = ..., auto_now: bool = ...,
        auto_now_add: bool = ..., **kwds: Any
    ) -> None: ...

class DateProperty(DateTimeProperty): ...

class ComputedProperty(Property): ...

class IntegerProperty(Property): ...

class FloatProperty(Property): ...

class JsonProperty(Property):
    def __init__(
        self, name: Optional[str] = ..., compressed: bool = ...,
        json_type: Optional[Any] = ..., **kwds: Any
    ) -> None: ...

class UserProperty(Property):
    def __init__(
        self, name: Optional[str] = ..., auto_current_user: bool = ...,
        auto_current_user_add: bool = ..., **kwds: Any
    ) -> None: ...

class TextProperty(Property): ...

class StringProperty(TextProperty): ...

class Cursor:
    def __init__(
        self, urlsafe: Optional[str]
    ) -> None: ...
    def urlsafe(self) -> bytes: ...

# Key Stubs
class Key:
    def __new__(cls, *_args: Any, **kwargs: Any) -> Key: ...
    def namespace(self) -> Optional[str]: ...
    def app(self) -> Optional[str]: ...
    def project(self) -> Optional[str]: ...
    def id(self) -> str: ...
    def flat(self) -> Optional[Iterable[Union[str, int]]]: ...
    def kind(self) -> Optional[str]: ...
    def get(self, **ctx_options: Any) -> Optional[Model]: ...
    def delete(self, **ctx_options: Any) -> None: ...
    @classmethod
    def _from_ds_key(cls, ds_key: datastore.Key) -> Key: ...

class RedisCache:
    def __init__(self, redis_instance: StrictRedis[str]): ...

# Transaction Options Stubs
class TransactionOptions(object):
    NESTED = 1  # join=False
    MANDATORY = 2  # join=True
    ALLOWED = 3  # join=True
    INDEPENDENT = 4  # join=False
