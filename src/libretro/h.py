from ctypes import c_int, c_uint64, c_int64, c_void_p, cast, c_uint

RETRO_API_VERSION = 1
RETRO_DEVICE_TYPE_SHIFT = 8
RETRO_DEVICE_MASK = ((1 << RETRO_DEVICE_TYPE_SHIFT) - 1)


def RETRO_DEVICE_SUBCLASS(base: int, id: int) -> int:
    return (((id + 1) << RETRO_DEVICE_TYPE_SHIFT) | base)


RETRO_DEVICE_NONE = 0
RETRO_DEVICE_JOYPAD = 1
RETRO_DEVICE_MOUSE = 2
RETRO_DEVICE_KEYBOARD = 3
RETRO_DEVICE_LIGHTGUN = 4
RETRO_DEVICE_ANALOG = 5
RETRO_DEVICE_POINTER = 6

RETRO_DEVICE_ID_JOYPAD_B = 0
RETRO_DEVICE_ID_JOYPAD_Y = 1
RETRO_DEVICE_ID_JOYPAD_SELECT = 2
RETRO_DEVICE_ID_JOYPAD_START = 3
RETRO_DEVICE_ID_JOYPAD_UP = 4
RETRO_DEVICE_ID_JOYPAD_DOWN = 5
RETRO_DEVICE_ID_JOYPAD_LEFT = 6
RETRO_DEVICE_ID_JOYPAD_RIGHT = 7
RETRO_DEVICE_ID_JOYPAD_A = 8
RETRO_DEVICE_ID_JOYPAD_X = 9
RETRO_DEVICE_ID_JOYPAD_L = 10
RETRO_DEVICE_ID_JOYPAD_R = 11
RETRO_DEVICE_ID_JOYPAD_L2 = 12
RETRO_DEVICE_ID_JOYPAD_R2 = 13
RETRO_DEVICE_ID_JOYPAD_L3 = 14
RETRO_DEVICE_ID_JOYPAD_R3 = 15
RETRO_DEVICE_ID_JOYPAD_MASK = 256

RETRO_DEVICE_INDEX_ANALOG_LEFT = 0
RETRO_DEVICE_INDEX_ANALOG_RIGHT = 1
RETRO_DEVICE_INDEX_ANALOG_BUTTON = 2

RETRO_DEVICE_ID_ANALOG_X = 0
RETRO_DEVICE_ID_ANALOG_Y = 1

RETRO_DEVICE_ID_MOUSE_X = 0
RETRO_DEVICE_ID_MOUSE_Y = 1
RETRO_DEVICE_ID_MOUSE_LEFT = 2
RETRO_DEVICE_ID_MOUSE_RIGHT = 3
RETRO_DEVICE_ID_MOUSE_WHEELUP = 4
RETRO_DEVICE_ID_MOUSE_WHEELDOWN = 5
RETRO_DEVICE_ID_MOUSE_MIDDLE = 6
RETRO_DEVICE_ID_MOUSE_HORIZ_WHEELUP = 7
RETRO_DEVICE_ID_MOUSE_HORIZ_WHEELDOWN = 8
RETRO_DEVICE_ID_MOUSE_BUTTON_4 = 9
RETRO_DEVICE_ID_MOUSE_BUTTON_5 = 10

retro_key = c_int
RETROK_UNKNOWN = 0
RETROK_FIRST = 0
RETROK_BACKSPACE = 8
RETROK_TAB = 9
RETROK_CLEAR = 12
RETROK_RETURN = 13
RETROK_PAUSE = 19
RETROK_ESCAPE = 27
RETROK_SPACE = 32
RETROK_EXCLAIM = 33
RETROK_QUOTEDBL = 34
RETROK_HASH = 35
RETROK_DOLLAR = 36
RETROK_AMPERSAND = 38
RETROK_QUOTE = 39
RETROK_LEFTPAREN = 40
RETROK_RIGHTPAREN = 41
RETROK_ASTERISK = 42
RETROK_PLUS = 43
RETROK_COMMA = 44
RETROK_MINUS = 45
RETROK_PERIOD = 46
RETROK_SLASH = 47
RETROK_0 = 48
RETROK_1 = 49
RETROK_2 = 50
RETROK_3 = 51
RETROK_4 = 52
RETROK_5 = 53
RETROK_6 = 54
RETROK_7 = 55
RETROK_8 = 56
RETROK_9 = 57
RETROK_COLON = 58
RETROK_SEMICOLON = 59
RETROK_LESS = 60
RETROK_EQUALS = 61
RETROK_GREATER = 62
RETROK_QUESTION = 63
RETROK_AT = 64
RETROK_LEFTBRACKET = 91
RETROK_BACKSLASH = 92
RETROK_RIGHTBRACKET = 93
RETROK_CARET = 94
RETROK_UNDERSCORE = 95
RETROK_BACKQUOTE = 96
RETROK_a = 97
RETROK_b = 98
RETROK_c = 99
RETROK_d = 100
RETROK_e = 101
RETROK_f = 102
RETROK_g = 103
RETROK_h = 104
RETROK_i = 105
RETROK_j = 106
RETROK_k = 107
RETROK_l = 108
RETROK_m = 109
RETROK_n = 110
RETROK_o = 111
RETROK_p = 112
RETROK_q = 113
RETROK_r = 114
RETROK_s = 115
RETROK_t = 116
RETROK_u = 117
RETROK_v = 118
RETROK_w = 119
RETROK_x = 120
RETROK_y = 121
RETROK_z = 122
RETROK_LEFTBRACE = 123
RETROK_BAR = 124
RETROK_RIGHTBRACE = 125
RETROK_TILDE = 126
RETROK_DELETE = 127
RETROK_KP0 = 256
RETROK_KP1 = 257
RETROK_KP2 = 258
RETROK_KP3 = 259
RETROK_KP4 = 260
RETROK_KP5 = 261
RETROK_KP6 = 262
RETROK_KP7 = 263
RETROK_KP8 = 264
RETROK_KP9 = 265
RETROK_KP_PERIOD = 266
RETROK_KP_DIVIDE = 267
RETROK_KP_MULTIPLY = 268
RETROK_KP_MINUS = 269
RETROK_KP_PLUS = 270
RETROK_KP_ENTER = 271
RETROK_KP_EQUALS = 272
RETROK_UP = 273
RETROK_DOWN = 274
RETROK_RIGHT = 275
RETROK_LEFT = 276
RETROK_INSERT = 277
RETROK_HOME = 278
RETROK_END = 279
RETROK_PAGEUP = 280
RETROK_PAGEDOWN = 281
RETROK_F1 = 282
RETROK_F2 = 283
RETROK_F3 = 284
RETROK_F4 = 285
RETROK_F5 = 286
RETROK_F6 = 287
RETROK_F7 = 288
RETROK_F8 = 289
RETROK_F9 = 290
RETROK_F10 = 291
RETROK_F11 = 292
RETROK_F12 = 293
RETROK_F13 = 294
RETROK_F14 = 295
RETROK_F15 = 296
RETROK_NUMLOCK = 300
RETROK_CAPSLOCK = 301
RETROK_SCROLLOCK = 302
RETROK_RSHIFT = 303
RETROK_LSHIFT = 304
RETROK_RCTRL = 305
RETROK_LCTRL = 306
RETROK_RALT = 307
RETROK_LALT = 308
RETROK_RMETA = 309
RETROK_LMETA = 310
RETROK_LSUPER = 311
RETROK_RSUPER = 312
RETROK_MODE = 313
RETROK_COMPOSE = 314
RETROK_HELP = 315
RETROK_PRINT = 316
RETROK_SYSREQ = 317
RETROK_BREAK = 318
RETROK_MENU = 319
RETROK_POWER = 320
RETROK_EURO = 321
RETROK_UNDO = 322
RETROK_OEM_102 = 323
RETROK_LAST = (RETROK_OEM_102 + 1)
RETROK_DUMMY = 0x7fffffff

retro_mod = c_int
RETROKMOD_NONE = 0x0000
RETROKMOD_SHIFT = 0x01
RETROKMOD_CTRL = 0x02
RETROKMOD_ALT = 0x04
RETROKMOD_META = 0x08
RETROKMOD_NUMLOCK = 0x10
RETROKMOD_CAPSLOCK = 0x20
RETROKMOD_SCROLLOCK = 0x40
RETROKMOD_DUMMY = 0x7fffffff

RETRO_DEVICE_ID_LIGHTGUN_SCREEN_X = 13
RETRO_DEVICE_ID_LIGHTGUN_SCREEN_Y = 14
RETRO_DEVICE_ID_LIGHTGUN_IS_OFFSCREEN = 15
RETRO_DEVICE_ID_LIGHTGUN_TRIGGER = 2
RETRO_DEVICE_ID_LIGHTGUN_RELOAD = 16
RETRO_DEVICE_ID_LIGHTGUN_AUX_A = 3
RETRO_DEVICE_ID_LIGHTGUN_AUX_B = 4
RETRO_DEVICE_ID_LIGHTGUN_START = 6
RETRO_DEVICE_ID_LIGHTGUN_SELECT = 7
RETRO_DEVICE_ID_LIGHTGUN_AUX_C = 8
RETRO_DEVICE_ID_LIGHTGUN_DPAD_UP = 9
RETRO_DEVICE_ID_LIGHTGUN_DPAD_DOWN = 10
RETRO_DEVICE_ID_LIGHTGUN_DPAD_LEFT = 11
RETRO_DEVICE_ID_LIGHTGUN_DPAD_RIGHT = 12
RETRO_DEVICE_ID_LIGHTGUN_X = 0
RETRO_DEVICE_ID_LIGHTGUN_Y = 1
RETRO_DEVICE_ID_LIGHTGUN_CURSOR = 3
RETRO_DEVICE_ID_LIGHTGUN_TURBO = 4
RETRO_DEVICE_ID_LIGHTGUN_PAUSE = 5

RETRO_DEVICE_ID_POINTER_X = 0
RETRO_DEVICE_ID_POINTER_Y = 1
RETRO_DEVICE_ID_POINTER_PRESSED = 2
RETRO_DEVICE_ID_POINTER_COUNT = 3

RETRO_REGION_NTSC = 0
RETRO_REGION_PAL = 1




retro_language = c_int
RETRO_LANGUAGE_ENGLISH = 0
RETRO_LANGUAGE_JAPANESE = 1
RETRO_LANGUAGE_FRENCH = 2
RETRO_LANGUAGE_SPANISH = 3
RETRO_LANGUAGE_GERMAN = 4
RETRO_LANGUAGE_ITALIAN = 5
RETRO_LANGUAGE_DUTCH = 6
RETRO_LANGUAGE_PORTUGUESE_BRAZIL = 7
RETRO_LANGUAGE_PORTUGUESE_PORTUGAL = 8
RETRO_LANGUAGE_RUSSIAN = 9
RETRO_LANGUAGE_KOREAN = 10
RETRO_LANGUAGE_CHINESE_TRADITIONAL = 11
RETRO_LANGUAGE_CHINESE_SIMPLIFIED = 12
RETRO_LANGUAGE_ESPERANTO = 13
RETRO_LANGUAGE_POLISH = 14
RETRO_LANGUAGE_VIETNAMESE = 15
RETRO_LANGUAGE_ARABIC = 16
RETRO_LANGUAGE_GREEK = 17
RETRO_LANGUAGE_TURKISH = 18
RETRO_LANGUAGE_SLOVAK = 19
RETRO_LANGUAGE_PERSIAN = 20
RETRO_LANGUAGE_HEBREW = 21
RETRO_LANGUAGE_ASTURIAN = 22
RETRO_LANGUAGE_FINNISH = 23
RETRO_LANGUAGE_INDONESIAN = 24
RETRO_LANGUAGE_SWEDISH = 25
RETRO_LANGUAGE_UKRAINIAN = 26
RETRO_LANGUAGE_CZECH = 27
RETRO_LANGUAGE_CATALAN_VALENCIA = 28
RETRO_LANGUAGE_CATALAN = 29
RETRO_LANGUAGE_BRITISH_ENGLISH = 30
RETRO_LANGUAGE_HUNGARIAN = 31
RETRO_LANGUAGE_BELARUSIAN = 32
RETRO_LANGUAGE_LAST = (RETRO_LANGUAGE_BELARUSIAN + 1)
RETRO_LANGUAGE_DUMMY = 0x7fffffff

RETRO_MEMORY_MASK = 0xff
RETRO_MEMORY_SAVE_RAM = 0
RETRO_MEMORY_RTC = 1
RETRO_MEMORY_SYSTEM_RAM = 2
RETRO_MEMORY_VIDEO_RAM = 3

RETRO_ENVIRONMENT_EXPERIMENTAL = 0x10000
RETRO_ENVIRONMENT_PRIVATE = 0x20000
RETRO_ENVIRONMENT_SET_ROTATION = 1
RETRO_ENVIRONMENT_GET_OVERSCAN = 2
RETRO_ENVIRONMENT_GET_CAN_DUPE = 3
RETRO_ENVIRONMENT_SET_MESSAGE = 6
RETRO_ENVIRONMENT_SHUTDOWN = 7
RETRO_ENVIRONMENT_SET_PERFORMANCE_LEVEL = 8
RETRO_ENVIRONMENT_GET_SYSTEM_DIRECTORY = 9
RETRO_ENVIRONMENT_SET_PIXEL_FORMAT = 10
RETRO_ENVIRONMENT_SET_INPUT_DESCRIPTORS = 11
RETRO_ENVIRONMENT_SET_KEYBOARD_CALLBACK = 12
RETRO_ENVIRONMENT_SET_DISK_CONTROL_INTERFACE = 13
RETRO_ENVIRONMENT_SET_HW_RENDER = 14
RETRO_ENVIRONMENT_GET_VARIABLE = 15
RETRO_ENVIRONMENT_SET_VARIABLES = 16
RETRO_ENVIRONMENT_GET_VARIABLE_UPDATE = 17
RETRO_ENVIRONMENT_SET_SUPPORT_NO_GAME = 18
RETRO_ENVIRONMENT_GET_LIBRETRO_PATH = 19
RETRO_ENVIRONMENT_SET_FRAME_TIME_CALLBACK = 21
RETRO_ENVIRONMENT_SET_AUDIO_CALLBACK = 22
RETRO_ENVIRONMENT_GET_RUMBLE_INTERFACE = 23
RETRO_ENVIRONMENT_GET_INPUT_DEVICE_CAPABILITIES = 24
RETRO_ENVIRONMENT_GET_SENSOR_INTERFACE = (25 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_CAMERA_INTERFACE = (26 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_LOG_INTERFACE = 27
RETRO_ENVIRONMENT_GET_PERF_INTERFACE = 28
RETRO_ENVIRONMENT_GET_LOCATION_INTERFACE = 29
RETRO_ENVIRONMENT_GET_CONTENT_DIRECTORY = 30
RETRO_ENVIRONMENT_GET_CORE_ASSETS_DIRECTORY = 30
RETRO_ENVIRONMENT_GET_SAVE_DIRECTORY = 31
RETRO_ENVIRONMENT_SET_SYSTEM_AV_INFO = 32
RETRO_ENVIRONMENT_SET_PROC_ADDRESS_CALLBACK = 33
RETRO_ENVIRONMENT_SET_SUBSYSTEM_INFO = 34
RETRO_ENVIRONMENT_SET_CONTROLLER_INFO = 35
RETRO_ENVIRONMENT_SET_MEMORY_MAPS = (36 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_SET_GEOMETRY = 37
RETRO_ENVIRONMENT_GET_USERNAME = 38
RETRO_ENVIRONMENT_GET_LANGUAGE = 39
RETRO_ENVIRONMENT_GET_CURRENT_SOFTWARE_FRAMEBUFFER = (40 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_HW_RENDER_INTERFACE = (41 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_SET_SUPPORT_ACHIEVEMENTS = (42 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_SET_HW_RENDER_CONTEXT_NEGOTIATION_INTERFACE = (43 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_SET_SERIALIZATION_QUIRKS = 44
RETRO_ENVIRONMENT_SET_HW_SHARED_CONTEXT = (44 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_VFS_INTERFACE = (45 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_LED_INTERFACE = (46 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_AUDIO_VIDEO_ENABLE = (47 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_MIDI_INTERFACE = (48 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_FASTFORWARDING = (49 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_TARGET_REFRESH_RATE = (50 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_INPUT_BITMASKS = (51 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_CORE_OPTIONS_VERSION = 52
RETRO_ENVIRONMENT_SET_CORE_OPTIONS = 53
RETRO_ENVIRONMENT_SET_CORE_OPTIONS_INTL = 54
RETRO_ENVIRONMENT_SET_CORE_OPTIONS_DISPLAY = 55
RETRO_ENVIRONMENT_GET_PREFERRED_HW_RENDER = 56
RETRO_ENVIRONMENT_GET_DISK_CONTROL_INTERFACE_VERSION = 57
RETRO_ENVIRONMENT_SET_DISK_CONTROL_EXT_INTERFACE = 58
RETRO_ENVIRONMENT_GET_MESSAGE_INTERFACE_VERSION = 59
RETRO_ENVIRONMENT_SET_MESSAGE_EXT = 60
RETRO_ENVIRONMENT_GET_INPUT_MAX_USERS = 61
RETRO_ENVIRONMENT_SET_AUDIO_BUFFER_STATUS_CALLBACK = 62
RETRO_ENVIRONMENT_SET_MINIMUM_AUDIO_LATENCY = 63
RETRO_ENVIRONMENT_SET_FASTFORWARDING_OVERRIDE = 64
RETRO_ENVIRONMENT_SET_CONTENT_INFO_OVERRIDE = 65
RETRO_ENVIRONMENT_GET_GAME_INFO_EXT = 66
RETRO_ENVIRONMENT_SET_CORE_OPTIONS_V2 = 67
RETRO_ENVIRONMENT_SET_CORE_OPTIONS_V2_INTL = 68
RETRO_ENVIRONMENT_SET_CORE_OPTIONS_UPDATE_DISPLAY_CALLBACK = 69
RETRO_ENVIRONMENT_SET_VARIABLE = 70
RETRO_ENVIRONMENT_GET_THROTTLE_STATE = (71 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_SAVESTATE_CONTEXT = (72 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_HW_RENDER_CONTEXT_NEGOTIATION_INTERFACE_SUPPORT = (73 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_JIT_CAPABLE = 74
RETRO_ENVIRONMENT_GET_MICROPHONE_INTERFACE = (75 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_SET_NETPACKET_INTERFACE = 76
RETRO_ENVIRONMENT_GET_DEVICE_POWER = (77 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_PLAYLIST_DIRECTORY = 79

RETRO_VFS_FILE_ACCESS_READ = (1 << 0)
RETRO_VFS_FILE_ACCESS_WRITE = (1 << 1)
RETRO_VFS_FILE_ACCESS_READ_WRITE = (RETRO_VFS_FILE_ACCESS_READ | RETRO_VFS_FILE_ACCESS_WRITE)
RETRO_VFS_FILE_ACCESS_UPDATE_EXISTING = (1 << 2)

RETRO_VFS_FILE_ACCESS_HINT_NONE = 0
RETRO_VFS_FILE_ACCESS_HINT_FREQUENT_ACCESS = (1 << 0)

RETRO_VFS_SEEK_POSITION_START = 0
RETRO_VFS_SEEK_POSITION_CURRENT = 1
RETRO_VFS_SEEK_POSITION_END = 2

RETRO_VFS_STAT_IS_VALID = (1 << 0)
RETRO_VFS_STAT_IS_DIRECTORY = (1 << 1)
RETRO_VFS_STAT_IS_CHARACTER_SPECIAL = (1 << 2)

retro_hw_render_interface_type = c_int
RETRO_HW_RENDER_INTERFACE_VULKAN = 0
RETRO_HW_RENDER_INTERFACE_D3D9 = 1
RETRO_HW_RENDER_INTERFACE_D3D10 = 2
RETRO_HW_RENDER_INTERFACE_D3D11 = 3
RETRO_HW_RENDER_INTERFACE_D3D12 = 4
RETRO_HW_RENDER_INTERFACE_GSKIT_PS2 = 5
RETRO_HW_RENDER_INTERFACE_DUMMY = 0x7fffffff

retro_log_level = c_int
RETRO_LOG_DEBUG = 0
RETRO_LOG_INFO = (RETRO_LOG_DEBUG + 1)
RETRO_LOG_WARN = (RETRO_LOG_INFO + 1)
RETRO_LOG_ERROR = (RETRO_LOG_WARN + 1)
RETRO_LOG_DUMMY = 0x7fffffff

RETRO_SIMD_SSE = (1 << 0)
RETRO_SIMD_SSE2 = (1 << 1)
RETRO_SIMD_VMX = (1 << 2)
RETRO_SIMD_VMX128 = (1 << 3)
RETRO_SIMD_AVX = (1 << 4)
RETRO_SIMD_NEON = (1 << 5)
RETRO_SIMD_SSE3 = (1 << 6)
RETRO_SIMD_SSSE3 = (1 << 7)
RETRO_SIMD_MMX = (1 << 8)
RETRO_SIMD_MMXEXT = (1 << 9)
RETRO_SIMD_SSE4 = (1 << 10)
RETRO_SIMD_SSE42 = (1 << 11)
RETRO_SIMD_AVX2 = (1 << 12)
RETRO_SIMD_VFPU = (1 << 13)
RETRO_SIMD_PS = (1 << 14)
RETRO_SIMD_AES = (1 << 15)
RETRO_SIMD_VFPV3 = (1 << 16)
RETRO_SIMD_VFPV4 = (1 << 17)
RETRO_SIMD_POPCNT = (1 << 18)
RETRO_SIMD_MOVBE = (1 << 19)
RETRO_SIMD_CMOV = (1 << 20)
RETRO_SIMD_ASIMD = (1 << 21)
retro_perf_tick_t = c_uint64
retro_time_t = c_int64

retro_sensor_action = c_int
RETRO_SENSOR_ACCELEROMETER_ENABLE = 0
RETRO_SENSOR_ACCELEROMETER_DISABLE = (RETRO_SENSOR_ACCELEROMETER_ENABLE + 1)
RETRO_SENSOR_GYROSCOPE_ENABLE = (RETRO_SENSOR_ACCELEROMETER_DISABLE + 1)
RETRO_SENSOR_GYROSCOPE_DISABLE = (RETRO_SENSOR_GYROSCOPE_ENABLE + 1)
RETRO_SENSOR_ILLUMINANCE_ENABLE = (RETRO_SENSOR_GYROSCOPE_DISABLE + 1)
RETRO_SENSOR_ILLUMINANCE_DISABLE = (RETRO_SENSOR_ILLUMINANCE_ENABLE + 1)
RETRO_SENSOR_DUMMY = 0x7fffffff

RETRO_SENSOR_ACCELEROMETER_X = 0
RETRO_SENSOR_ACCELEROMETER_Y = 1
RETRO_SENSOR_ACCELEROMETER_Z = 2
RETRO_SENSOR_GYROSCOPE_X = 3
RETRO_SENSOR_GYROSCOPE_Y = 4
RETRO_SENSOR_GYROSCOPE_Z = 5
RETRO_SENSOR_ILLUMINANCE = 6

retro_camera_buffer = c_int
RETRO_CAMERA_BUFFER_OPENGL_TEXTURE = 0
RETRO_CAMERA_BUFFER_RAW_FRAMEBUFFER = (RETRO_CAMERA_BUFFER_OPENGL_TEXTURE + 1)
RETRO_CAMERA_BUFFER_DUMMY = 0x7fffffff

retro_rumble_effect = c_int
RETRO_RUMBLE_STRONG = 0
RETRO_RUMBLE_WEAK = 1
RETRO_RUMBLE_DUMMY = 0x7fffffff

RETRO_HW_FRAME_BUFFER_VALID = cast((-1), c_void_p)

retro_hw_context_type = c_int
RETRO_HW_CONTEXT_NONE = 0
RETRO_HW_CONTEXT_OPENGL = 1
RETRO_HW_CONTEXT_OPENGLES2 = 2
RETRO_HW_CONTEXT_OPENGL_CORE = 3
RETRO_HW_CONTEXT_OPENGLES3 = 4
RETRO_HW_CONTEXT_OPENGLES_VERSION = 5
RETRO_HW_CONTEXT_VULKAN = 6
RETRO_HW_CONTEXT_D3D11 = 7
RETRO_HW_CONTEXT_D3D10 = 8
RETRO_HW_CONTEXT_D3D12 = 9
RETRO_HW_CONTEXT_D3D9 = 10
RETRO_HW_CONTEXT_DUMMY = 0x7fffffff

retro_av_enable_flags = c_uint
RETRO_AV_ENABLE_VIDEO = (1 << 0),
RETRO_AV_ENABLE_AUDIO = (1 << 1),
RETRO_AV_ENABLE_FAST_SAVESTATES = (1 << 2),
RETRO_AV_ENABLE_HARD_DISABLE_AUDIO = (1 << 3),
RETRO_AV_ENABLE_DUMMY = 0x7fffffff

retro_hw_render_context_negotiation_interface_type = c_int
RETRO_HW_RENDER_CONTEXT_NEGOTIATION_INTERFACE_VULKAN = 0
RETRO_HW_RENDER_CONTEXT_NEGOTIATION_INTERFACE_DUMMY = 0x7fffffff

RETRO_SERIALIZATION_QUIRK_INCOMPLETE = (1 << 0)
RETRO_SERIALIZATION_QUIRK_MUST_INITIALIZE = (1 << 1)
RETRO_SERIALIZATION_QUIRK_CORE_VARIABLE_SIZE = (1 << 2)
RETRO_SERIALIZATION_QUIRK_FRONT_VARIABLE_SIZE = (1 << 3)
RETRO_SERIALIZATION_QUIRK_SINGLE_SESSION = (1 << 4)
RETRO_SERIALIZATION_QUIRK_ENDIAN_DEPENDENT = (1 << 5)
RETRO_SERIALIZATION_QUIRK_PLATFORM_DEPENDENT = (1 << 6)

RETRO_MEMDESC_CONST = (1 << 0)
RETRO_MEMDESC_BIGENDIAN = (1 << 1)
RETRO_MEMDESC_SYSTEM_RAM = (1 << 2)
RETRO_MEMDESC_SAVE_RAM = (1 << 3)
RETRO_MEMDESC_VIDEO_RAM = (1 << 4)
RETRO_MEMDESC_ALIGN_2 = (1 << 16)
RETRO_MEMDESC_ALIGN_4 = (2 << 16)
RETRO_MEMDESC_ALIGN_8 = (3 << 16)
RETRO_MEMDESC_MINSIZE_2 = (1 << 24)
RETRO_MEMDESC_MINSIZE_4 = (2 << 24)
RETRO_MEMDESC_MINSIZE_8 = (3 << 24)

RETRO_NETPACKET_UNRELIABLE = 0
RETRO_NETPACKET_RELIABLE = (1 << 0)
RETRO_NETPACKET_UNSEQUENCED = (1 << 1)
RETRO_NETPACKET_FLUSH_HINT = (1 << 2)
RETRO_NETPACKET_BROADCAST = 0xffff

retro_pixel_format = c_int
RETRO_PIXEL_FORMAT_0RGB1555 = 0
RETRO_PIXEL_FORMAT_XRGB8888 = 1
RETRO_PIXEL_FORMAT_RGB565 = 2
RETRO_PIXEL_FORMAT_UNKNOWN = 0x7fffffff

retro_savestate_context = c_int
RETRO_SAVESTATE_CONTEXT_NORMAL = 0
RETRO_SAVESTATE_CONTEXT_RUNAHEAD_SAME_INSTANCE = 1
RETRO_SAVESTATE_CONTEXT_RUNAHEAD_SAME_BINARY = 2
RETRO_SAVESTATE_CONTEXT_ROLLBACK_NETPLAY = 3
RETRO_SAVESTATE_CONTEXT_UNKNOWN = 0x7fffffff

retro_message_target = c_int
RETRO_MESSAGE_TARGET_ALL = 0
RETRO_MESSAGE_TARGET_OSD = (RETRO_MESSAGE_TARGET_ALL + 1)
RETRO_MESSAGE_TARGET_LOG = (RETRO_MESSAGE_TARGET_OSD + 1)

retro_message_type = c_int
RETRO_MESSAGE_TYPE_NOTIFICATION = 0
RETRO_MESSAGE_TYPE_NOTIFICATION_ALT = (RETRO_MESSAGE_TYPE_NOTIFICATION + 1)
RETRO_MESSAGE_TYPE_STATUS = (RETRO_MESSAGE_TYPE_NOTIFICATION_ALT + 1)
RETRO_MESSAGE_TYPE_PROGRESS = (RETRO_MESSAGE_TYPE_STATUS + 1)

RETRO_NUM_CORE_OPTION_VALUES_MAX = 128

RETRO_MEMORY_ACCESS_WRITE = (1 << 0)
RETRO_MEMORY_ACCESS_READ = (1 << 1)

RETRO_MEMORY_TYPE_CACHED = (1 << 0)

RETRO_THROTTLE_NONE = 0
RETRO_THROTTLE_FRAME_STEPPING = 1
RETRO_THROTTLE_FAST_FORWARD = 2
RETRO_THROTTLE_SLOW_MOTION = 3
RETRO_THROTTLE_REWINDING = 4
RETRO_THROTTLE_VSYNC = 5
RETRO_THROTTLE_UNBLOCKED = 6

RETRO_MICROPHONE_INTERFACE_VERSION = 1

retro_power_state = c_int
RETRO_POWERSTATE_UNKNOWN = 0
RETRO_POWERSTATE_DISCHARGING = (RETRO_POWERSTATE_UNKNOWN + 1)
RETRO_POWERSTATE_CHARGING = (RETRO_POWERSTATE_DISCHARGING + 1)
RETRO_POWERSTATE_CHARGED = (RETRO_POWERSTATE_CHARGING + 1)
RETRO_POWERSTATE_PLUGGED_IN = (RETRO_POWERSTATE_CHARGED + 1)
RETRO_POWERSTATE_NO_ESTIMATE = (-1)
