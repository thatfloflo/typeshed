import threading
from _typeshed import Incomplete
from collections import MutableMapping as DictMixin
from collections.abc import Generator
from functools import update_wrapper as update_wrapper
from io import TextIOWrapper
from re import Pattern
from typing import Callable, TypeVar, Any, Sequence
from collections.abc import Iterator


_T = TypeVar("_T")

__author__: str
__version__: str
__license__: str

py: tuple[int, int, int, str, int]
py3k: bool
py25: bool
py31: bool

def getargspec(func: Callable[..., Any]) -> tuple[list[str], list[str] | None, list[str] | None, list[Any] | None]: ...

def json_dumps(data: Any) -> str: ...
def json_loads(str: str | bytes | bytearray) -> Any: ...
json_lds = json_loads

basestring = str
unicode = str
bytes = str
callable: Callable[[object], bool]
imap = map
msg: str

def next(it: Iterator[_T]) -> _T: ...
def tob(s: str, enc: str = "utf-8") -> bytes: ...
def touni(s: bytes | bytearray, enc: str = "utf-8", err: str = "strict") -> str: ...

tonat = touni

class NCTextIOWrapper(TextIOWrapper):
    def close(self) -> None: ...

def depr(message: str, hard: bool = False) -> None: ...
def makelist(data: Sequence[_T] | _T) -> list[_T]: ...

class DictProperty:
    def __init__(self, attr: object, key: str | None = None, read_only: bool = False) -> None: ...
    def __call__(self, func: Callable[..., Any]) -> DictProperty: ...
    def __get__(self, obj: object, cls: type) -> DictProperty | Any: ...
    def __set__(self, obj: object, value: Any) -> None: ...
    def __delete__(self, obj: object) -> None: ...

class cached_property:
    __doc__: str
    func: Callable[..., Any]
    def __init__(self, func: Callable[..., Any]) -> None: ...
    def __get__(self, obj: object, cls: type) -> Any: ...

# CONTINUE HERE

class lazy_attribute:
    getter: Incomplete
    def __init__(self, func: Callable[..., Any]) -> None: ...
    def __get__(self, obj: object, cls: type): ...

class BottleException(Exception): ...
class RouteError(BottleException): ...
class RouteReset(BottleException): ...
class RouterUnknownModeError(RouteError): ...
class RouteSyntaxError(RouteError): ...
class RouteBuildError(RouteError): ...

def _re_flatten(p: str): ...

class Router:
    default_pattern: str
    default_filter: str
    rules: list[Incomplete]
    builder: dict[Incomplete, Incomplete]
    static: dict[str, Incomplete]
    dyna_routes: dict[Incomplete, Incomplete]
    dyna_regexes: dict[Incomplete, Incomplete]
    strict_order: bool
    filters: dict[str, Callable[[str], tuple[str, Callable[[str], Any] | None, Callable[[Any], str] | None]]]
    def __init__(self, strict: bool = False) -> None: ...
    def add_filter(self, name: str, func: Callable[[str], tuple[str, Callable[[str], Any] | None, Callable[[Any], str] | None]]) -> None: ...
    rule_syntax: Pattern[str]
    def add(self, rule: str, method: str, target: Callable[..., Any], name: str | None = ...): ...
    def build(self, _name: str, *anons: Callable[..., Any], **query: dict[str, Any]): ...
    def match(self, environ: dict[str, Incomplete]) -> tuple[str, str]: ...

class Route:
    app: Bottle
    rule: str
    method: str
    callback: Callable[..., Any]
    name: str | None
    plugins: list[Callable[[Callable[..., Any]], Any]]
    skiplist: list[Incomplete]
    config: ConfigDict
    def __init__(
        self,
        app: Bottle,
        rule: str,
        method: str,
        callback: Callable[..., Any],
        name: str | None = None,
        plugins: list[Callable[[Callable[..., Any]], Any]] | None = None,
        skiplist: list[bool | type | Callable[[Callable[..., Any]], Any]] | None = None,
        **config: dict[str, Any],
    ) -> None: ...
    def __call__(self, *a: Any, **ka: Any) -> Any: ...
    def call(self) -> Any: ...
    def reset(self) -> None: ...
    def prepare(self) -> None: ...
    def all_plugins(self) -> Iterator[Callable[[Callable[..., Any]], Any]]: ...
    def get_undecorated_callback(self) -> Callable[..., Any]: ...
    def get_callback_args(self) -> list[str]: ...
    def get_config(self, key: str, default: Any = None) -> Any: ...

# CONTINUE HERE

class Bottle:
    config: Incomplete
    resources: Incomplete
    routes: Incomplete
    router: Incomplete
    error_handler: Incomplete
    plugins: Callable[[Callable[..., Any]], Any]
    def __init__(self, catchall: bool = True, autojson: bool = True) -> None: ...
    catchall: Incomplete
    def add_hook(self, name, func) -> None: ...
    def remove_hook(self, name, func): ...
    def trigger_hook(self, __name, *args, **kwargs): ...
    def hook(self, name): ...
    def mount(self, prefix, app, **options): ...
    def merge(self, routes) -> None: ...
    def install(self, plugin): ...
    def uninstall(self, plugin): ...
    def reset(self, route: Incomplete | None = ...) -> None: ...
    stopped: bool
    def close(self) -> None: ...
    def run(self, **kwargs) -> None: ...
    def match(self, environ): ...
    def get_url(self, routename, **kargs): ...
    def add_route(self, route) -> None: ...
    def route(
        self,
        path: Incomplete | None = ...,
        method: str = ...,
        callback: Incomplete | None = ...,
        name: Incomplete | None = ...,
        apply: Incomplete | None = ...,
        skip: Incomplete | None = ...,
        **config,
    ): ...
    def get(self, path: Incomplete | None = ..., method: str = ..., **options): ...
    def post(self, path: Incomplete | None = ..., method: str = ..., **options): ...
    def put(self, path: Incomplete | None = ..., method: str = ..., **options): ...
    def delete(self, path: Incomplete | None = ..., method: str = ..., **options): ...
    def error(self, code: int = ...): ...
    def default_error_handler(self, res): ...
    def wsgi(self, environ, start_response): ...
    def __call__(self, environ, start_response): ...

class BaseRequest:
    MEMFILE_MAX: int
    environ: Incomplete
    def __init__(self, environ: Incomplete | None = ...) -> None: ...
    def app(self) -> None: ...
    def route(self) -> None: ...
    def url_args(self) -> None: ...
    @property
    def path(self): ...
    @property
    def method(self): ...
    def headers(self): ...
    def get_header(self, name, default: Incomplete | None = ...): ...
    def cookies(self): ...
    def get_cookie(self, key, default: Incomplete | None = ..., secret: Incomplete | None = ...): ...
    def query(self): ...
    def forms(self): ...
    def params(self): ...
    def files(self): ...
    def json(self): ...
    @property
    def body(self): ...
    @property
    def chunked(self): ...
    GET = query
    def POST(self): ...
    @property
    def url(self): ...
    def urlparts(self): ...
    @property
    def fullpath(self): ...
    @property
    def query_string(self): ...
    @property
    def script_name(self): ...
    def path_shift(self, shift: int = ...) -> None: ...
    @property
    def content_length(self): ...
    @property
    def content_type(self): ...
    @property
    def is_xhr(self): ...
    @property
    def is_ajax(self): ...
    @property
    def auth(self): ...
    @property
    def remote_route(self): ...
    @property
    def remote_addr(self): ...
    def copy(self): ...
    def get(self, value, default: Incomplete | None = ...): ...
    def __getitem__(self, key): ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def keys(self): ...
    def __setitem__(self, key, value) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...

class HeaderProperty:
    __doc__: Incomplete
    def __init__(self, name, reader: Incomplete | None = ..., writer: Incomplete | None = ..., default: str = ...) -> None: ...
    def __get__(self, obj, cls): ...
    def __set__(self, obj, value) -> None: ...
    def __delete__(self, obj) -> None: ...

class BaseResponse:
    default_status: int
    default_content_type: str
    bad_headers: Incomplete
    body: Incomplete
    status: Incomplete
    def __init__(
        self, body: str = ..., status: Incomplete | None = ..., headers: Incomplete | None = ..., **more_headers
    ) -> None: ...
    def copy(self, cls: Incomplete | None = ...): ...
    def __iter__(self): ...
    def close(self) -> None: ...
    @property
    def status_line(self): ...
    @property
    def status_code(self): ...
    @property
    def headers(self): ...
    def __contains__(self, name) -> bool: ...
    def __delitem__(self, name) -> None: ...
    def __getitem__(self, name): ...
    def __setitem__(self, name, value) -> None: ...
    def get_header(self, name, default: Incomplete | None = ...): ...
    def set_header(self, name, value) -> None: ...
    def add_header(self, name, value) -> None: ...
    def iter_headers(self): ...
    @property
    def headerlist(self): ...
    content_type: Incomplete
    content_length: Incomplete
    expires: Incomplete
    @property
    def charset(self, default: str = ...): ...
    def set_cookie(self, name, value, secret: Incomplete | None = ..., **options) -> None: ...
    def delete_cookie(self, key, **kwargs) -> None: ...

def local_property(name: Incomplete | None = ...): ...

class LocalRequest(BaseRequest):
    bind: Incomplete
    environ: Incomplete

class LocalResponse(BaseResponse):
    bind: Incomplete
    body: Incomplete

Request = BaseRequest
Response = BaseResponse

class HTTPResponse(Response, BottleException):
    def __init__(
        self, body: str = ..., status: Incomplete | None = ..., headers: Incomplete | None = ..., **more_headers
    ) -> None: ...
    def apply(self, response) -> None: ...

class HTTPError(HTTPResponse):
    default_status: int
    exception: Incomplete
    traceback: Incomplete
    def __init__(
        self,
        status: Incomplete | None = ...,
        body: Incomplete | None = ...,
        exception: Incomplete | None = ...,
        traceback: Incomplete | None = ...,
        **options,
    ) -> None: ...

class PluginError(BottleException): ...

class JSONPlugin:
    name: str
    api: int
    json_dumps: Incomplete
    def __init__(self, json_dumps=...) -> None: ...
    def apply(self, callback, route): ...

class TemplatePlugin:
    name: str
    api: int
    def apply(self, callback, route): ...

class _ImportRedirect:
    name: Incomplete
    impmask: Incomplete
    module: Incomplete
    def __init__(self, name, impmask) -> None: ...
    def find_module(self, fullname, path: Incomplete | None = ...): ...
    def load_module(self, fullname): ...

class MultiDict(DictMixin):
    dict: Incomplete
    def __init__(self, *a, **k) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __contains__(self, key) -> bool: ...
    def __delitem__(self, key) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def allitems(self): ...
    def iterkeys(self): ...
    def itervalues(self): ...
    def iteritems(self): ...
    def iterallitems(self): ...
    def get(self, key, default: Incomplete | None = ..., index: int = ..., type: Incomplete | None = ...): ...
    def append(self, key, value) -> None: ...
    def replace(self, key, value) -> None: ...
    def getall(self, key): ...
    getone = get
    getlist = getall

class FormsDict(MultiDict):
    input_encoding: str
    recode_unicode: bool
    def decode(self, encoding: Incomplete | None = ...): ...
    def getunicode(self, name, default: Incomplete | None = ..., encoding: Incomplete | None = ...): ...
    def __getattr__(self, name, default=...): ...

class HeaderDict(MultiDict):
    dict: Incomplete
    def __init__(self, *a, **ka) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __delitem__(self, key) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def append(self, key, value) -> None: ...
    def replace(self, key, value) -> None: ...
    def getall(self, key): ...
    def get(self, key, default: Incomplete | None = ..., index: int = ...): ...
    def filter(self, names) -> None: ...

class WSGIHeaderDict(DictMixin):
    cgikeys: Incomplete
    environ: Incomplete
    def __init__(self, environ) -> None: ...
    def raw(self, key, default: Incomplete | None = ...): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self): ...
    def keys(self): ...
    def __len__(self) -> int: ...
    def __contains__(self, key) -> bool: ...

class ConfigDict(dict):
    class Namespace(DictMixin):
        def __init__(self, config, namespace) -> None: ...
        def __getitem__(self, key): ...
        def __setitem__(self, key, value) -> None: ...
        def __delitem__(self, key) -> None: ...
        def __iter__(self): ...
        def keys(self): ...
        def __len__(self) -> int: ...
        def __contains__(self, key) -> bool: ...
        def __getattr__(self, key): ...
        def __setattr__(self, key, value) -> None: ...
        def __delattr__(self, key) -> None: ...
        def __call__(self, *a, **ka): ...

    def __init__(self, *a, **ka) -> None: ...
    def load_config(self, filename): ...
    def load_dict(self, source, namespace: str = ..., make_namespaces: bool = ...): ...
    def update(self, *a, **ka) -> None: ...
    def setdefault(self, key, value): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key) -> None: ...
    def clear(self) -> None: ...
    def meta_get(self, key, metafield, default: Incomplete | None = ...): ...
    def meta_set(self, key, metafield, value) -> None: ...
    def meta_list(self, key): ...
    def __getattr__(self, key): ...
    def __setattr__(self, key, value): ...
    def __delattr__(self, key) -> None: ...
    def __call__(self, *a, **ka): ...

class AppStack(list):
    def __call__(self): ...
    def push(self, value: Incomplete | None = ...): ...

class WSGIFileWrapper:
    def __init__(self, fp, buffer_size=...) -> None: ...
    def __iter__(self): ...

class _closeiter:
    iterator: Incomplete
    close_callbacks: Incomplete
    def __init__(self, iterator, close: Incomplete | None = ...) -> None: ...
    def __iter__(self): ...
    def close(self) -> None: ...

class ResourceManager:
    opener: Incomplete
    base: Incomplete
    cachemode: Incomplete
    path: Incomplete
    cache: Incomplete
    def __init__(self, base: str = ..., opener=..., cachemode: str = ...) -> None: ...
    def add_path(self, path, base: Incomplete | None = ..., index: Incomplete | None = ..., create: bool = ...): ...
    def __iter__(self): ...
    def lookup(self, name): ...
    def open(self, name, mode: str = ..., *args, **kwargs): ...

class FileUpload:
    file: Incomplete
    name: Incomplete
    raw_filename: Incomplete
    headers: Incomplete
    def __init__(self, fileobj, name, filename, headers: Incomplete | None = ...) -> None: ...
    content_type: Incomplete
    content_length: Incomplete
    def get_header(self, name, default: Incomplete | None = ...): ...
    def filename(self): ...
    def save(self, destination, overwrite: bool = ..., chunk_size=...) -> None: ...

def abort(code: int = ..., text: str = ...) -> None: ...
def redirect(url, code: Incomplete | None = ...) -> None: ...
def static_file(filename, root, mimetype: str = ..., download: bool = ..., charset: str = ...): ...
def debug(mode: bool = ...) -> None: ...
def http_date(value): ...
def parse_date(ims): ...
def parse_auth(header): ...
def parse_range_header(header, maxlen: int = ...) -> Generator[Incomplete, None, None]: ...
def cookie_encode(data, key): ...
def cookie_decode(data, key): ...
def cookie_is_encoded(data): ...
def html_escape(string): ...
def html_quote(string): ...
def yieldroutes(func) -> Generator[Incomplete, None, None]: ...
def path_shift(script_name, path_info, shift: int = ...): ...
def auth_basic(check, realm: str = ..., text: str = ...): ...
def make_default_app_wrapper(name): ...

route: Incomplete
get: Incomplete
post: Incomplete
put: Incomplete
delete: Incomplete
error: Incomplete
mount: Incomplete
hook: Incomplete
install: Incomplete
uninstall: Incomplete
url: Incomplete

class ServerAdapter:
    quiet: bool
    options: Incomplete
    host: Incomplete
    port: Incomplete
    def __init__(self, host: str = ..., port: int = ..., **options) -> None: ...
    def run(self, handler) -> None: ...

class CGIServer(ServerAdapter):
    quiet: bool
    def run(self, handler): ...

class FlupFCGIServer(ServerAdapter):
    def run(self, handler) -> None: ...

class WSGIRefServer(ServerAdapter):
    def run(self, app): ...

class CherryPyServer(ServerAdapter):
    def run(self, handler) -> None: ...

class CherootServer(ServerAdapter):
    def run(self, handler) -> None: ...

class WaitressServer(ServerAdapter):
    def run(self, handler) -> None: ...

class PasteServer(ServerAdapter):
    def run(self, handler) -> None: ...

class MeinheldServer(ServerAdapter):
    def run(self, handler) -> None: ...

class FapwsServer(ServerAdapter):
    def run(self, handler): ...

class TornadoServer(ServerAdapter):
    def run(self, handler) -> None: ...

class AppEngineServer(ServerAdapter):
    quiet: bool
    def run(self, handler): ...

class TwistedServer(ServerAdapter):
    def run(self, handler) -> None: ...

class DieselServer(ServerAdapter):
    def run(self, handler) -> None: ...

class GeventServer(ServerAdapter):
    def run(self, handler): ...

class GeventSocketIOServer(ServerAdapter):
    def run(self, handler) -> None: ...

class GunicornServer(ServerAdapter):
    def run(self, handler): ...

class EventletServer(ServerAdapter):
    def run(self, handler) -> None: ...

class RocketServer(ServerAdapter):
    def run(self, handler) -> None: ...

class BjoernServer(ServerAdapter):
    def run(self, handler) -> None: ...

class AutoServer(ServerAdapter):
    adapters: Incomplete
    def run(self, handler): ...

server_names: Incomplete

def load(target, **namespace): ...
def load_app(target): ...
def run(
    app: Incomplete | None = ...,
    server: str = ...,
    host: str = ...,
    port: int = ...,
    interval: int = ...,
    reloader: bool = ...,
    quiet: bool = ...,
    plugins: Incomplete | None = ...,
    debug: Incomplete | None = ...,
    **kargs,
) -> None: ...

class FileCheckerThread(threading.Thread):
    status: Incomplete
    def __init__(self, lockfile, interval) -> None: ...
    def run(self): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...

class TemplateError(HTTPError):
    def __init__(self, message) -> None: ...

class BaseTemplate:
    extensions: Incomplete
    settings: Incomplete
    defaults: Incomplete
    name: Incomplete
    source: Incomplete
    filename: Incomplete
    lookup: Incomplete
    encoding: Incomplete
    def __init__(
        self, source: Incomplete | None = ..., name: Incomplete | None = ..., lookup=..., encoding: str = ..., **settings
    ) -> None: ...
    @classmethod
    def search(cls, name, lookup=...): ...
    @classmethod
    def global_config(cls, key, *args): ...
    def prepare(self, **options) -> None: ...
    def render(self, *args, **kwargs) -> None: ...

class MakoTemplate(BaseTemplate):
    tpl: Incomplete
    def prepare(self, **options) -> None: ...
    def render(self, *args, **kwargs): ...

class CheetahTemplate(BaseTemplate):
    context: Incomplete
    tpl: Incomplete
    def prepare(self, **options) -> None: ...
    def render(self, *args, **kwargs): ...

class Jinja2Template(BaseTemplate):
    env: Incomplete
    tpl: Incomplete
    def prepare(self, filters: Incomplete | None = ..., tests: Incomplete | None = ..., globals=..., **kwargs) -> None: ...
    def render(self, *args, **kwargs): ...
    def loader(self, name): ...

class SimpleTemplate(BaseTemplate):
    cache: Incomplete
    syntax: Incomplete
    def prepare(self, escape_func=..., noescape: bool = ..., syntax: Incomplete | None = ..., **ka): ...
    def co(self): ...
    encoding: Incomplete
    def code(self): ...
    def execute(self, _stdout, kwargs): ...
    def render(self, *args, **kwargs): ...

class StplSyntaxError(TemplateError): ...

class StplParser:
    default_syntax: str
    paren_depth: int
    def __init__(self, source, syntax: Incomplete | None = ..., encoding: str = ...) -> None: ...
    def get_syntax(self): ...
    def set_syntax(self, syntax) -> None: ...
    syntax: Incomplete
    def translate(self): ...
    offset: Incomplete
    def read_code(self, multiline) -> None: ...
    def flush_text(self) -> None: ...
    def process_inline(self, chunk): ...
    def write_code(self, line, comment: str = ...) -> None: ...
    source: Incomplete
    encoding: Incomplete
    def fix_backward_compatibility(self, line, comment): ...

def template(*args, **kwargs): ...

mako_template: Incomplete
cheetah_template: Incomplete
jinja2_template: Incomplete

def view(tpl_name, **defaults): ...

mako_view: Incomplete
cheetah_view: Incomplete
jinja2_view: Incomplete
TEMPLATE_PATH: Incomplete
TEMPLATES: Incomplete
DEBUG: bool
NORUN: bool
HTTP_CODES: Incomplete
ERROR_PAGE_TEMPLATE: Incomplete
request: Incomplete
response: Incomplete
local: Incomplete
app: Incomplete
default_app: Incomplete
ext: Incomplete
