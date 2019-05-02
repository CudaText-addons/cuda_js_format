import sys
import os
from cudatext import *
from .json_stringify import *

sys.path.append(os.path.dirname(__file__))
import jsbeautifier
import format_proc

format_proc.INI = 'cuda_js_format.py'
format_proc.MSG = '[JS Format] '

def options():
    op = jsbeautifier.default_options()
    ini = format_proc.ini_filename()
    if os.path.isfile(ini):
        d = eval(open(ini).read())
        op.indent_size               = d["indent_size"]
        op.indent_char               = d["indent_char"]
        op.indent_with_tabs          = d["indent_with_tabs"]
        op.preserve_newlines         = d["preserve_newlines"]
        op.max_preserve_newlines     = d["max_preserve_newlines"]
        op.space_in_paren            = d["space_in_paren"]
        op.e4x                       = d["e4x"]
        op.jslint_happy              = d["jslint_happy"]
        op.brace_style               = d["brace_style"]
        op.keep_array_indentation    = d["keep_array_indentation"]
        op.keep_function_indentation = d["keep_function_indentation"]
        op.eval_code                 = d["eval_code"]
        op.unescape_strings          = d["unescape_strings"]
        op.wrap_line_length          = d["wrap_line_length"]
        op.break_chained_methods     = d["break_chained_methods"]
    return op

def do_format(text):
    return jsbeautifier.beautify(text, options())

def do_stringify(text):

    #if ed.get_prop(PROP_TAB_SPACES):
    #    indent = ' '*ed.get_prop(PROP_TAB_SIZE)
    #else:
    #    indent = '\t'
    return invert_json_string(text)


class Command:
    def config_global(self):
        format_proc.config_global()

    def config_local(self):
        format_proc.config_local()

    def run(self):
        format_proc.run(do_format)

    def string(self):
        format_proc.run(do_stringify)
