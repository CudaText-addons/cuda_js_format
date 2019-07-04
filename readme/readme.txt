Plugin "JS Format" for CudaText.
It allows to format source code for lexers JavaScript and JSON, using Python engine from jsbeautifier.org. If selection is made (only normal selection supported) then only selection is formatted, otherwise entire file is formatted.

It also gives command "Minify".

It also gives command "JSON Stringify" which is taken from https://github.com/Nadock/json_stringify

Plugin has configuration file, which can be edited using two "Configure" commands:
- Configure: opens config-file from "settings" folder, which is used when local file doesn't exist.
- Configure (local): opens config-file from the folder of current editor file. If local file doesn't exist, command suggests to copy global file into local name, and then opens it. 

Options [default]

- "indent_size"                Indentation size [4]
- "indent_char"                Indentation character [" "]
- "indent_with_tabs"           Indent with tabs
- "preserve_newlines"          Preserve line-breaks
- "max_preserve_newlines"      Number of line-breaks to be preserved in one chunk [10]
- "space_in_paren"             Add padding spaces within paren, ie. f( a, b )
- "e4x"                        Pass E4X XML literals through untouched
- "jslint_happy"               Enable jslint-stricter mode
- "brace_style"                Possible values: "collapse", "expand", "end-expand" ["collapse"]
- "keep_array_indentation"     Preserve array indentation
- "keep_function_indentation"  Preserve function indentation
- "unescape_strings"           Decode printable characters encoded in xNN notation
- "wrap_line_length"           Wrap lines at next opportunity after N characters [0]
- "break_chained_methods"      Break chained method calls across subsequent lines


Author: Alexey Torgashin (CudaText)
License: MIT
