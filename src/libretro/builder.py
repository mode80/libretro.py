from collections.abc import Callable, Iterator, Iterable, Mapping
from ctypes import CDLL
from enum import Enum, auto
from logging import Logger
from os import PathLike
from typing import Self, Literal, TypedDict, AnyStr
from zipfile import Path as ZipPath

from .api.audio import AudioDriver, ArrayAudioDriver
from .api.av import AvEnableFlags
from .api.content import *
from .api.environment.composite import CompositeEnvironmentDriver
from .api.input import *
from .api.led import LedDriver, DictLedDriver
from .api.location import LocationInputGenerator
from .api.location.driver import LocationDriver
from .api.log import LogDriver, UnformattedLogDriver
from .api.message import MessageInterface, LoggerMessageInterface
from .api.microphone import MicrophoneDriver
from .api.midi import MidiDriver
from .api.options import *
from .api.path import PathDriver, DefaultPathDriver
from .api.perf import PerfDriver, DefaultPerfDriver
from .api.power import DevicePower
from .api.savestate import SavestateContext
from .api.throttle import retro_throttle_state
from .api.user import UserDriver, DefaultUserDriver
from .api.vfs import FileSystemInterface, StandardFileSystemInterface
from .api.video import VideoDriver, ArrayVideoDriver, HardwareContext
from .core import Core
from .session import Session


type _RequiredFactory[T] = Callable[[], T]
type _OptionalFactory[T] = Callable[[], T | None]

type _RequiredArg[T] = T | _RequiredFactory[T]
type _OptionalArg[T] = T | _OptionalFactory[T] | Default | None


class _DefaultType(Enum):
    DEFAULT = auto()


DEFAULT = _DefaultType.DEFAULT
Default = Literal[_DefaultType.DEFAULT]
"""
A placeholder that indicates the default value for a SessionBuilder argument.
When passed to a SessionBuilder method, the method will use the default value for that argument.
"""

_nothing = lambda: None
CoreArg = Core | str | PathLike | CDLL | _RequiredFactory[Core]
AudioDriverArg = _RequiredArg[AudioDriver] | Default
InputDriverArg = _RequiredArg[InputDriver] | InputStateGenerator | InputStateIterable | InputStateIterator | Default
VideoDriverArg = _RequiredArg[VideoDriver] | Default
ContentArg = _OptionalArg[Content | SubsystemContent]
ContentDriverArg = _OptionalArg[ContentDriver]
BoolArg = _OptionalArg[bool]
MessageDriverArg = _OptionalArg[MessageInterface] | Logger
OptionDriverArg = _OptionalArg[OptionDriver] | Mapping[AnyStr, AnyStr] | Literal[0, 1, 2]
PathDriverArg = _OptionalArg[PathDriver] | str | PathLike
LogDriverArg = _OptionalArg[LogDriver] | Logger
PerfDriverArg = _OptionalArg[PerfDriver]
LocationDriverArg = _OptionalArg[LocationDriver] | LocationInputGenerator
UserDriverArg = _OptionalArg[UserDriver]
FileSystemArg = _OptionalArg[FileSystemInterface] | Literal[1, 2, 3]
LedDriverArg = _OptionalArg[LedDriver]
AvEnableFlagsArg = _OptionalArg[AvEnableFlags]
MidiDriverArg = _OptionalArg[MidiDriver]
FloatArg = _OptionalArg[float]
HardwareContextArg = _OptionalArg[HardwareContext]
ThrottleStateArg = _OptionalArg[retro_throttle_state]
SavestateContextArg = _OptionalArg[SavestateContext]
MicDriverArg = _OptionalArg[MicrophoneDriver]
PowerDriverArg = _OptionalArg[DevicePower]


class RequiredError(RuntimeError):
    pass


def _raise_required_error(msg: str):
    raise RequiredError(msg)


class _SessionBuilderArgs(TypedDict):
    core: _RequiredFactory[Core]
    audio: _RequiredFactory[AudioDriver]
    input: _RequiredFactory[InputDriver]
    video: _RequiredFactory[VideoDriver]
    content: _OptionalFactory[Content | SubsystemContent]
    content_driver: _OptionalFactory[ContentDriver]
    overscan: _OptionalFactory[bool] # TODO: Replace with some driver (not sure what yet)
    message: _OptionalFactory[MessageInterface]
    options: _OptionalFactory[OptionDriver]
    path: _OptionalFactory[PathDriver]
    log: _OptionalFactory[LogDriver]
    perf: _OptionalFactory[PerfDriver]
    location: _OptionalFactory[LocationDriver]
    user: _OptionalFactory[UserDriver]
    vfs: _OptionalFactory[FileSystemInterface]
    led: _OptionalFactory[LedDriver]
    av_mask: _OptionalFactory[AvEnableFlags]
    midi: _OptionalFactory[MidiDriver]
    target_refresh_rate: _OptionalFactory[float] # TODO: Replace with TimingDriver
    preferred_hw: _OptionalFactory[HardwareContext] # TODO: Replace with a method in VideoDriver
    driver_switch_enable: _OptionalFactory[bool] # TODO: Replace with a method in VideoDriver
    throttle: _OptionalFactory[retro_throttle_state] # TODO: Replace with TimingDriver
    savestate_context: _OptionalFactory[SavestateContext] # TODO: Replace with some driver (not sure what yet)
    jit_capable: _OptionalFactory[bool] # TODO: Replace with some driver (not sure what yet)
    mic: _OptionalFactory[MicrophoneDriver]
    power: _OptionalFactory[DevicePower] # TODO: Replace with PowerDriver


class SessionBuilder:
    """
    A builder class for constructing Session objects.

    A Session requires a Core, an AudioDriver, an InputDriver, and a VideoDriver;
    each ``with_`` method sets an argument (mostly drivers) for the Session.
    """
    def __init__(self):
        self._args = _SessionBuilderArgs(
            core=lambda: _raise_required_error("A Core is required"),
            audio=lambda: _raise_required_error("An AudioDriver is required"),
            input=lambda: _raise_required_error("An InputDriver is required"),
            video=lambda: _raise_required_error("A VideoDriver is required"),
            content=_nothing,
            content_driver=_nothing,
            overscan=_nothing,
            message=_nothing,
            options=_nothing,
            path=_nothing,
            log=_nothing,
            perf=_nothing,
            location=_nothing,
            user=_nothing,
            vfs=_nothing,
            led=_nothing,
            av_mask=_nothing,
            midi=_nothing,
            target_refresh_rate=_nothing,
            preferred_hw=_nothing,
            driver_switch_enable=_nothing,
            throttle=_nothing,
            savestate_context=_nothing,
            jit_capable=_nothing,
            mic=_nothing,
            power=_nothing
        )

    def with_core(self, core: CoreArg) -> Self:
        """
        Sets the core to use for the session.

        ``core`` may be one of the following:

        - A :class:`Core` that will be used as-is.
        - A :class:`str` or :class:`PathLike` that represents a path to the core.
          It will be loaded as a :class:`Core` when the session is built.
        - A :class:`CDLL` object that represents a loaded binary.
          It will be loaded into a :class:`Core` when the session is built.
        - A :class:`Callable` that returns one of the above types.
          It will be evaluated when the session is built.

        :param core: The core to use for the session.
        :return: This builder object.
        :raises ValueError: If ``core`` is :py:const:`Default`.
        :raises TypeError: If ``core`` is not one of the permitted types.
        """
        match core:
            case Core():
                self._args["core"] = lambda: core
            case str() | PathLike() | CDLL():
                self._args["core"] = lambda: Core(core)
            case func if callable(func):
                self._args["core"] = func
            case _DefaultType.DEFAULT:
                raise ValueError("Core does not have a default value")
            case _:
                raise TypeError(f"Expected Core, str, PathLike, a CDLL, or a callable that returns one of them; got {type(core).__name__}")

        return self

    def with_content(self, content: ContentArg) -> Self:
        """
        Sets the content to use for this session.

        ``content`` may be one of the following:

        TODO
        """
        match content:
            case PathLike() | ZipPath() | str() | bytes() | bytearray() | memoryview() | SubsystemContent() | retro_game_info() | None:
                self._args["content"] = lambda: content
            case func if callable(func):
                self._args["content"] = func
            case _DefaultType.DEFAULT:
                raise ValueError("Content does not have a default value (if you wanted None, provide it explicitly)")
            case _:
                raise TypeError(f"Expected a path, content buffer, None, SubsystemContent, or a callable that returns one of them; got {type(content).__name__}")

        return self

    def with_audio(self, audio: AudioDriverArg) -> Self:
        match audio:
            case AudioDriver():
                self._args["audio"] = lambda: audio
            case func if callable(func):
                self._args["audio"] = func
            case _DefaultType.DEFAULT:
                self._args["audio"] = ArrayAudioDriver
            case None:
                raise ValueError("An audio driver is required")
            case _:
                raise TypeError(f"Expected AudioDriver, a callable that returns one, or DEFAULT; got {type(audio).__name__}")

        return self

    def with_input(self, input: InputDriverArg) -> Self:
        match input:
            case InputDriver():
                self._args["input"] = lambda: input
            case func if callable(func):
                # Either a generator or a driver type
                self._args["input"] = func
            case it if isinstance(it, (Iterator, Iterable)):
                # Arguments to a generator
                self._args["input"] = lambda: GeneratorInputDriver(it)
            case _DefaultType.DEFAULT:
                self._args["input"] = GeneratorInputDriver # TODO: Set the rumble and sensor interfaces
            case None:
                raise ValueError("An input driver is required")
            case _:
                raise TypeError(f"Expected InputDriver or a callable that returns one, a callable or iterator that yields InputState, or DEFAULT; got {type(input).__name__}")

        return self

    def with_video(self, video: VideoDriverArg) -> Self:
        match video:
            case VideoDriver():
                self._args["video"] = lambda: video
            case func if callable(func):
                self._args["video"] = func
            case _DefaultType.DEFAULT:
                self._args["video"] = ArrayVideoDriver
            case None:
                raise ValueError("A video driver is required")
            case _:
                raise TypeError(f"Expected a VideoDriver, a callable that returns one, or DEFAULT; got {type(video).__name__}")

        return self

    def with_content_driver(self, content: ContentDriverArg) -> Self:
        match content:
            case ContentDriver():
                self._args["content_driver"] = lambda: content
            case func if callable(func):
                self._args["content_driver"] = func
            case _DefaultType.DEFAULT:
                self._args["content_driver"] = StandardContentDriver
            case None:
                self._args["content_driver"] = _nothing
            case _:
                raise TypeError(f"Expected ContentDriver, a callable that returns one, DEFAULT, or None; got {type(content).__name__}")

        return self

    def with_overscan(self, overscan: BoolArg) -> Self:
        match overscan:
            case bool():
                self._args["overscan"] = lambda: overscan
            case func if callable(func):
                self._args["overscan"] = func
            case _DefaultType.DEFAULT:
                self._args["overscan"] = lambda: False
            case None:
                self._args["overscan"] = _nothing
            case _:
                raise TypeError(f"Expected bool, a callable that returns one, DEFAULT, or None; got {type(overscan).__name__}")

        return self

    def with_message(self, message: MessageDriverArg) -> Self:
        match message:
            case MessageInterface():
                self._args["message"] = lambda: message
            case Logger() as logger:
                self._args["message"] = lambda: LoggerMessageInterface(logger=logger)
            case func if callable(func):
                self._args["message"] = func
            case _DefaultType.DEFAULT:
                self._args["message"] = LoggerMessageInterface
            case None:
                self._args["message"] = _nothing
            case _:
                raise TypeError(f"Expected MessageInterface, a callable that returns one, DEFAULT, or None; got {type(message).__name__}")

        return self

    def with_options(self, options: OptionDriverArg) -> Self:
        _types = (str, bytes)
        match options:
            case OptionDriver(driver):
                driver: OptionDriver
                self._args["options"] = lambda: driver
            case dict(vars) if all(isinstance(k, _types) and isinstance(v, _types) for k, v in vars.items()):
                vars: Mapping[AnyStr, AnyStr]
                self._args["options"] = lambda: DictOptionDriver(2, True, vars)
            case 0 | 1 | 2 as version:
                self._args["options"] = lambda: DictOptionDriver(version)
            case func if callable(func):
                self._args["options"] = func
            case _DefaultType.DEFAULT:
                self._args["options"] = DictOptionDriver
            case None:
                self._args["options"] = _nothing
            case _:
                raise TypeError(f"Expected OptionDriver, a dict, a callable that returns one, DEFAULT, or None; got {type(options).__name__}")

        return self

    def with_paths(self, path: PathDriverArg) -> Self:
        match path:
            case PathDriver():
                self._args["path"] = lambda: path
            case func if callable(func):
                self._args["path"] = func
            case _DefaultType.DEFAULT:
                self._args["path"] = DefaultPathDriver # TODO: How to pass core path?
            case None:
                self._args["path"] = _nothing
            case _:
                raise TypeError(f"Expected PathDriver, a callable that returns one, DEFAULT, or None; got {type(path).__name__}")

        return self

    def with_log(self, log: LogDriverArg) -> Self:
        match log:
            case LogDriver():
                self._args["log"] = lambda: log
            case Logger() as logger:
                self._args["log"] = lambda: UnformattedLogDriver(logger=logger)
            case func if callable(func):
                self._args["log"] = func
            case _DefaultType.DEFAULT:
                self._args["log"] = UnformattedLogDriver
            case None:
                self._args["log"] = _nothing
            case _:
                raise TypeError(f"Expected LogDriver, a callable that returns one, DEFAULT, or None; got {type(log).__name__}")

        return self

    def with_perf(self, perf: PerfDriverArg) -> Self:
        match perf:
            case PerfDriver():
                self._args["perf"] = lambda: perf
            case func if callable(func):
                self._args["perf"] = func
            case _DefaultType.DEFAULT:
                self._args["perf"] = DefaultPerfDriver
            case None:
                self._args["perf"] = _nothing
            case _:
                raise TypeError(f"Expected PerfDriver, a callable that returns one, DEFAULT, or None; got {type(perf).__name__}")

        return self

    def with_location(self, location: LocationDriverArg) -> Self:
        match location:
            case LocationDriver():
                self._args["location"] = lambda: location
            case func if callable(func):
                self._args["location"] = func
            case None:
                self._args["location"] = _nothing
            case _:
                raise TypeError(f"Expected LocationDriver, a callable that returns one, DEFAULT, or None; got {type(location).__name__}")

        return self

    def with_user(self, user: UserDriverArg) -> Self:
        match user:
            case UserDriver():
                self._args["user"] = lambda: user
            case func if callable(func):
                self._args["user"] = func
            case _DefaultType.DEFAULT:
                self._args["user"] = DefaultUserDriver
            case None:
                self._args["user"] = _nothing
            case _:
                raise TypeError(f"Expected UserDriver, a callable that returns one, DEFAULT, or None; got {type(user).__name__}")

        return self

    def with_vfs(self, vfs: FileSystemArg) -> Self:
        match vfs:
            case FileSystemInterface():
                interface: FileSystemInterface
                self._args["vfs"] = lambda: interface
            case func if callable(func):
                self._args["vfs"] = func
            case 1 | 2 | 3 as version:
                self._args["vfs"] = lambda: StandardFileSystemInterface(version)
            case _DefaultType.DEFAULT:
                self._args["vfs"] = StandardFileSystemInterface
            case None:
                self._args["vfs"] = _nothing
            case _:
                raise TypeError(f"Expected FileSystemInterface, a callable that returns one, DEFAULT, or None; got {type(vfs).__name__}")

        return self

    def with_led(self, led: LedDriverArg) -> Self:
        match led:
            case LedDriver():
                self._args["led"] = lambda: led
            case func if callable(func):
                self._args["led"] = func
            case _DefaultType.DEFAULT:
                self._args["led"] = DictLedDriver
            case None:
                self._args["led"] = _nothing
            case _:
                raise TypeError(f"Expected LedDriver, a callable that returns one, or None; got {type(led).__name__}")

        return self

    def with_av_mask(self, av_mask: AvEnableFlagsArg) -> Self:
        match av_mask:
            case AvEnableFlags():
                self._args["av_mask"] = lambda: av_mask
            case func if callable(func):
                self._args["av_mask"] = func
            case None:
                self._args["av_mask"] = _nothing
            case _:
                raise TypeError(f"Expected AvEnableFlags, a callable that returns one, or None; got {type(av_mask).__name__}")

        return self

    def with_midi(self, midi: MidiDriverArg) -> Self:
        match midi:
            case MidiDriver():
                self._args["midi"] = lambda: midi
            case func if callable(func):
                self._args["midi"] = func
            case None:
                self._args["midi"] = _nothing
            case _:
                raise TypeError(f"Expected MidiDriver, a callable that returns one, or None; got {type(midi).__name__}")

        return self

    def build(self) -> Session:
        """
        Constructs a Session object with the provided arguments.
        """
        core = self._args["core"]()
        content = self._args["content"]()
        envargs = CompositeEnvironmentDriver.Args(
            audio=self._args["audio"](),
            input=self._args["input"](),
            video=self._args["video"](),
            content=self._args["content_driver"](),
            overscan=self._args["overscan"](),
            message=self._args["message"](),
            options=self._args["options"](),
            path=self._args["path"](),
            log=self._args["log"](),
            perf=self._args["perf"](),
            location=self._args["location"](),
            user=self._args["user"](),
            vfs=self._args["vfs"](),
            led=self._args["led"](),
            av_enable=self._args["av_mask"](),
            midi=self._args["midi"](),
            target_refresh_rate=self._args["target_refresh_rate"](),
            preferred_hw=self._args["preferred_hw"](),
            driver_switch_enable=self._args["driver_switch_enable"](),
            throttle_state=self._args["throttle"](),
            savestate_context=self._args["savestate_context"](),
            jit_capable=self._args["jit_capable"](),
            mic_interface=self._args["mic"](),
            device_power=self._args["power"](),
        )

        environment = CompositeEnvironmentDriver(envargs)
        return Session(core, content, environment)


def defaults(core: CoreArg) -> SessionBuilder:
    return SessionBuilder() \
        .with_core(core) \
        .with_audio(DEFAULT) \
        .with_input(DEFAULT) \
        .with_video(DEFAULT) \



__all__ = [
    "SessionBuilder",
    "DEFAULT",
    "defaults",
]
