from tree_sitter import Language


grammar_root = '/home/chail/data/grammar'
lang_list = ['python', 'java', 'go']
Language.build_library(
    'mmlang.so',
    [f'{grammar_root}/tree-sitter-{lang}' for lang in lang_list]
)
