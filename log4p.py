config = {
    'monitorInterval': 10,                         # auto reload time interval [secs]
    'loggers': {
        'LogDemo': {
            'level': "DEBUG",
            'additivity': False,
            'AppenderRef': ['LogDemo']
            },
        'root': {
            'level': "DEBUG",
            'AppenderRef': ['output_root']
        }
    },
    'appenders': {
        'output_root': {
            'type': "file",
            'FileName': "root_error.log",            # log file name
            'backup_count': 5,                       # files count use backup log
            'file_size_limit': 1024 * 1024 * 20,     # single log file size, default :20MB
            'PatternLayout': "[level:%(levelname)s-file:%(filename)s-lineno:%(lineno)d] %(asctime)s %(message)s"
        },
        'LogDemo': {
            'type': "file",
            'FileName': "LogDemo.log",
            'PatternLayout': "[level:%(levelname)s-file:%(filename)s-lineno:%(lineno)d] %(asctime)s %(message)s"
        },
        'console': {
            'type': "console",
            'target': "console",
            'PatternLayout': "[%(levelname)s] %(asctime)s %(message)s"
        }
    }
}
