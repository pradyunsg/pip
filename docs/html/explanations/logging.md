# Logging

## On the console

pip offers {ref}`-v, --verbose <--verbose>` and {ref}`-q, --quiet <--quiet>` to
control the console log level. By default, some messages (error and warnings)
are colored in the terminal. If you want to suppress the colored output use
{ref}`--no-color <--no-color>`.

## In a file

pip offers the {ref}`--log <--log>` option for specifying a file where a
maximum verbosity log will be kept. This option is empty by default. This log
appends to previous logging.

Like all pip options, `--log` can also be set as an environment variable, or
placed into the pip configuration file. See the [Configuration](./configuration)
page for more details.
