import sys
import os
import json
from cudatext import *
from .json_stringify import *

sys.path.append(os.path.dirname(__file__))
import jsbeautifier
import format_proc

format_proc.INI = 'cuda_js_format.json'
format_proc.MSG = '[JS Format] '

def options():

    op = jsbeautifier.default_options()
    fn = format_proc.ini_filename()
    if not os.path.isfile(fn):
        return op

    with open(fn) as f:
        d = json.load(f)    
        op.indent_size               = d.get('indent_size', 4)
        op.indent_char               = d.get('indent_char', ' ')
        op.indent_with_tabs          = d.get('indent_with_tabs', False)
        op.preserve_newlines         = d.get('preserve_newlines', True)
        op.max_preserve_newlines     = d.get('max_preserve_newlines', 10)
        op.space_in_paren            = d.get('space_in_paren', False)
        op.e4x                       = d.get('e4x', False)
        op.jslint_happy              = d.get('jslint_happy', False)
        op.brace_style               = d.get('brace_style', 'collapse')
        op.keep_array_indentation    = d.get('keep_array_indentation', False)
        op.keep_function_indentation = d.get('keep_function_indentation', False)
        op.eval_code                 = d.get('eval_code', False)
        op.unescape_strings          = d.get('unescape_strings', False)
        op.wrap_line_length          = d.get('wrap_line_length', 0)
        op.break_chained_methods     = d.get('break_chained_methods', False)
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
